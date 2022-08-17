from config import Stockpiles, Outputs, Inputs, Objective
from model.problem import Problem
from mip import Model, Var, LinExpr, xsum
from typing import Optional, Tuple, Dict
import random
import os


class LinModel:
    """This class represents a Linear Model that is built using the Python-MIP 
    package.

    To instantiate this class, you must install and import the Python-MIP 
    package first. Python-MIP requires Python 3.5 or newer. Since Python-MIP is 
    included in the Python Package Index, once you have a Python installation, 
    installing it is as easy as entering in the command prompt:
    
        $ pip install mip

    Python-MIP is a collection of Python tools for the modeling and solution of 
    Mixed-Integer Linear programs (MIPs). The package also provides access to 
    advanced solver features like cut generation, lazy constraints, MIP starts 
    and solution pools. For more information, access https://www.python-mip.com.
    """

    def __init__(self: 'LinModel', problem: Problem):
        """Instanciates a new Linear Model.

        Args:
            problem (Problem): Problem considered.
        """

        self._omp: Model = Model('Ore Mixing Problem')

        # Problem data used to solve the model
        self._info: str = problem.info[0]
        self._stockpiles: Stockpiles = problem.stockpiles
        self._outputs: Outputs = problem.outputs
        self._inputs: Inputs = problem.inputs

        # set of stockpiles, quality parameters, requests and ore inputs
        self._p: int = len(problem.stockpiles)  
        self._t: int = len(problem.outputs[0].quality)
        self._r: int = len(problem.outputs)
        self._e: int = len(problem.inputs)

        # variables for the Ore Mixing Problem
        self._x: Optional[Var] = None
        self._y: Optional[Var] = None

        # weights of the restrictions in the objective function
        self._w_1: int = problem.info[1]
        self._w_2: int = problem.info[2]

        # variable weights for the Ore Mixing Problem
        self._w_x: Dict[Tuple[int, int], int] = {
            (i, k): 1 for i in range(self._p) for k in range(self._r)
        }

        self._w_y: Dict[Tuple[int, int], int] = {
            (h, i): 1 for h in range(self._e) for i in range(self._p)
        }

        # deviation variables for the Ore Mixing Problem
        self._a_max: Optional[Var] = None
        self._a_min: Optional[Var] = None
        self._b_max: Optional[Var] = None
        self._b_min: Optional[Var] = None

        # control flags
        self.__has_vars: bool = False
        self.__has_constrs: bool = False
        self.__has_objective: bool = False

        # assigns variable values, creates constraints and objective function
        self.__add_vars()
        self.__add_constrs()
        self.__add_objective()

    def resolve(self: 'LinModel') -> Objective:
        """This method resolves the linear model and write the its details 
        in a .lp file (in CPLEX or Gurobi lp format).

        Returns:
            Tuple[Optional[float], Dict[str, List[float]], Dict[str, List[float]]]:
                A tuple whose first element is the objective value of the
                model, the second element is a dictionary of entries whose keys 
                are the stockpiles IDs and values ​​are lists with the stacked 
                weights, the last element is a dictionary of recoveries whose
                keys are the IDs of each request and the values ​​are lists with
                the reclaimed weights.
        """

        assert self.__has_objective, \
            'calling the resolve() before mandatory call to __add_objective().'

        # solving the model
        os.makedirs(os.path.dirname(f'./out/logs/'), exist_ok=True)
        self._omp.write(f'./out/logs/{self._info}.lp')
        self._omp.optimize()

        if self._omp.num_solutions > 0:

            # output weights taken from each stockpile i for each request k
            reclaims = {
                f'id: {self._outputs[k].id}': [
                    self._x[i, k].x for i in range(self._p)
                ] for k in range(self._r)
            }

            # input weights taken from each input j for each stockpile k
            inputs = {
                f'id: {self._stockpiles[i].id}': [
                    self._y[h, i].x for h in range(self._e)
                ] for i in range(self._p)
            }

            return self._omp.objective_value, reclaims, inputs

        else:
            return None, {}, {}

    def add_weights(
        self: 'LinModel', 
        variable: str, 
        weights: Dict[Tuple[int, int], int]
    ) -> None:
        """This method assigns weights to the variables. It must be called 
        whenever it is necessary to send to send feedback to this model.
        
        Args:
            variable (str): Indicator of which variable weights are defined. 
                It must be 'x' or 'y'.
            weights (Dict[Tuple[int, int], int]): Dict of weights reclaimed or 
                stacked resulting from a previous execution of this model.
        """

        assert variable == 'x' or variable == 'y', (
            'the variable \'x\' or \'y\' to which the weights '
            'will be applied must be defined.'
        )

        assert weights, \
            'calling add_weights with an empty matrix of weights.'

        if variable == 'x':
            # resets the previous list of weights, if any
            self._w_x = {
                (i, k): 1 for i in range(self._p) for k in range(self._r)
            }

            # sets a new list of weights with random values
            for k, lin in enumerate(weights):
                for i, col in enumerate(lin):
                    self._w_x[i, k] = random.randint(1, 1e3) if col > 0 else 1

        elif variable == 'y':
            # resets the previous list of weights, if any
            self._w_y = {
                (h, i): 1 for h in range(self._e) for i in range(self._p)
            }

            # sets a new list of weights with random values
            for i, lin in enumerate(weights):
                for h, col in enumerate(lin):
                    self._w_y[h, i] = random.randint(1, 1e3) if col > 0 else 1

    def __add_vars(self: 'LinModel') -> None:
        """This method assigns values ​​to variables. It is automatically called 
        on the class instantiation and there is no need to use it latter.
        """

        assert not self.__has_vars, (
            'calling the __add_vars() private method that was already ' 
            'executed when instantiating the class.'
        )
        
        self.__has_vars = True

        # x_ik is the quantity of ore removed from stockpile i for request k
        self._x = {(i, k): self._omp.add_var(name=f'x_{i}{k}')
            for i in range(self._p) for k in range(self._r)}

        # y_hk is the quantity of ore removed from input h for stockpile i
        self._y = {(h, i): self._omp.add_var(name=f'y_{h}{i}')
            for h in range(self._e) for i in range(self._p)}

        # var_jk is the deviation from the quality parameter j of the request k
        self._a_max = {(j, k): self._omp.add_var(name=f'a_max_{j}{k}')
            for j in range(self._t) for k in range(self._r)}
        self._a_min = {(j, k): self._omp.add_var(name=f'a_min_{j}{k}')
            for j in range(self._t) for k in range(self._r)}
        self._b_max = {(j, k): self._omp.add_var(name=f'b_max_{j}{k}')
            for j in range(self._t) for k in range(self._r)}
        self._b_min = {(j, k): self._omp.add_var(name=f'b_min_{j}{k}')
            for j in range(self._t) for k in range(self._r)}

    def __add_constrs(self: 'LinModel') -> None:
        """This method creates constraints for the model. It is automatically 
        called on the class instantiation and there is no need to use it latter.
        """

        assert self.__has_vars, \
            'calling the __add_constrs() before mandatory call to __add_vars().'

        assert not self.__has_constrs, (
            'calling the __add_constrs() private method that was already ' 
            'executed when instantiating the class.'
        )
        
        self.__has_constrs = True

         # capacity constraint of inputs
        for h in range(self._e):
            self._omp += xsum(self._y[h, i] for i in range(self._p)) \
                      <= self._inputs[h].weight, f'input_weight_constr_{h}'

        # stockpile capacity constraints
        for i in range(self._p):
            self._omp += xsum(self._y[h, i] for h in range(self._e)) \
                      + self._stockpiles[i].weight_ini \
                      <= self._stockpiles[i].capacity, f'capacity_constr_{i}'

            for h in range(self._e):
                self._omp += xsum(self._x[i, k] for k in range(self._r)) \
                          <= self._stockpiles[i].weight_ini + self._y[h, i], \
                          f'weight_constr_{i}{h}'

        for k in range(self._r):
            # demand constraint
            self._omp += xsum(self._x[i, k] for i in range(self._p)) \
                      == self._outputs[k].weight, f'demand_constr_{k}'

            # quality constraints
            for j in range(self._t):

                # minimum quality deviation constraint
                q_1: LinExpr = xsum(
                    self._x[i, k] * (self._stockpiles[i].quality_ini[j].value -
                    self._outputs[k].quality[j].minimum) for i in range(self._p)
                )

                self._omp += q_1 + self._a_min[j, k] * self._outputs[k].weight \
                          >= 0, f'min_quality_constr_{j}{k}'

                # maximum quality deviation constraint
                q_2: LinExpr = xsum(
                    self._x[i, k] * (self._stockpiles[i].quality_ini[j].value -
                    self._outputs[k].quality[j].maximum) for i in range(self._p)
                )

                self._omp += q_2 - self._a_max[j, k] * self._outputs[k].weight \
                          <= 0, f'max_quality_constr_{j}{k}'

                # deviation constraint from the quality goal
                q_3: LinExpr = xsum(
                    self._x[i, k] * (self._stockpiles[i].quality_ini[j].value -
                    self._outputs[k].quality[j].goal) for i in range(self._p)
                )

                self._omp += q_3 + (self._b_min[j, k] - self._b_max[j, k]) \
                          * self._outputs[k].weight == 0, \
                          f'goal_quality_constr_{j}{k}'

    def __add_objective(self: 'LinModel') -> None:
        """This method creates a objective function for the model. It is 
        automatically called on the class instantiation and there is no need 
        to use it latter.
        """

        assert self.__has_constrs, (
            'calling the __add_objective() before mandatory '
            'call to __add_constrs().'
        )

        assert not self.__has_objective, (
            'calling the __add_objective() private method that was '
            'already executed when instantiating the class.'
        )
        
        self.__has_objective = True

        # deviation from limits
        d_limit: LinExpr = xsum(
            self._outputs[k].quality[j].importance *
            self._a_min[j, k] / self.__normalize(j, k, 'lb') +
            self._outputs[k].quality[j].importance *
            self._a_max[j, k] / self.__normalize(j, k, 'ub')
            for j in range(self._t) for k in range(self._r)
        )

        # goal deviation
        d_goal: LinExpr = xsum(
            (self._b_min[j, k] + self._b_max[j, k]) /
            min(self.__normalize(j, k, 'lb'), self.__normalize(j, k, 'ub'))
            for j in range(self._t) for k in range(self._r)
        )

        # scheduling reclaims
        r_scheduling: LinExpr = xsum(
            self._w_x[i, k] * self._x[i, k]
            for i in range(self._p) for k in range(self._r)
        )

        # scheduling inputs
        i_scheduling: LinExpr = xsum(
            self._w_y[h, i] * self._y[h, i]
            for h in range(self._e) for i in range(self._p)
        )

        # objective function
        self._omp += self._w_1 * d_limit \
                  + self._w_2 * d_goal \
                  + r_scheduling + i_scheduling

    def __normalize(self: 'LinModel', j: int, k: int, bound: str) -> float:
        """This method helps to calculate the units of deviation and avoids 
        division by zero. It is called within __add_objective() to help build 
        the objective function and there is no need to use it afterwards.

        Args:
            j (int): The index of the quality parameter considered.
            k (int): The index of the request considered.
            bound (str): Indicator if the calculation should be made by the 
                upper bound or the lower bound. This argument must be defined
                as 'ub' for the upper bound or 'lb' for the lower bound.

        Returns:
            float: The result of subtracting the quality goal by the 
                indicated limit. If this result is zero, then the value 
                1e-6 will be returned.
        """

        assert bound == 'ub' or bound == 'lb', \
            'the upper or lower bound indicator must be defined.'

        # outputs[k].quality[j] is the quality parameter j of the request k
        ans: float = 0

        # ub indicates that the calculation should be normalized by the maximum
        if bound == 'ub':
            ans = self._outputs[k].quality[j].maximum \
                - self._outputs[k].quality[j].goal

        # lb indicates that the calculation should be normalized by the minimum
        elif bound == 'lb':
            ans = self._outputs[k].quality[j].goal \
                - self._outputs[k].quality[j].minimum

        return ans if ans != 0 else 1e-6

from algorithm.constructive import SimpleConstructive
from algorithm.neighborhood import Move
from model.problem import Problem
from model.solution import Solution
from typing import List, Optional
import random


class Heuristic:
    """This class represents a Heuristic (or Local Search method). The basic 
    methods and neighborhood selection are included.
    """

    def __init__(
        self: 'Heuristic', 
        problem: Problem,
        name: str):
        """Instantiates a new Heuristic.
     
        Args:
            problem (Problem): The problem reference.
            name (str): The name of the heuristic.
        """

        self._problem: Problem = problem
        self._name: str = name

        self._moves: List[Move] = []
        self._best_solution: Optional[Solution] = None
        self._iters: int = 0

    def add_move(self: 'Heuristic', move: Move) -> None:
        """This method adds a move to the heuristic.
        
        Args:
            move (int): The move to be added.
        """

        self._moves.append(move)
    
    def accept_move(self: 'Heuristic', move: Move) -> None:
        """This method accepts a move. 

        Args:
            move (Move): The move to be accepted.
        """
    
        move.accept()

    def reject_move(self: 'Heuristic', move: Move) -> None:
        """This method rejects a move.

        Args:
            move (Move): The move to be rejected.
        """

        move.reject()

    def select_move(self: 'Heuristic', solution: Solution) -> Move:
        """This method selects a move.

        Args:
            solution (Solution): The solution.

        Returns:
            Move: a randomly selected move (neighborhood).
        """

        size: int = len(self._moves)
        move: Move = self._moves[random.randrange(0, size)]

        while not move.has_move(solution):
            move = self._moves[(random.randrange(0, size))]

        return move

    # region simple getters and setters
    @property
    def problem(self: 'Heuristic') -> Problem:
        """Problem: The problem reference."""
        return self._problem

    @problem.setter
    def problem(self: 'Heuristic', value: Problem) -> None:
        self._problem = value

    @property
    def name(self: 'Heuristic') -> str:
        """str: The name of the heuristic."""
        return self._name

    @name.setter
    def name(self: 'Heuristic', value: str) -> None:
        self._name = value

    @property
    def moves(self: 'Heuristic') -> List[Move]:
        """List[Move]: List with all the movements present in this heuristic."""
        return self._moves

    @moves.setter
    def moves(self: 'Heuristic', value: List[Move]) -> None:
        self._moves = value
    
    @property
    def best_solution(self: 'Heuristic') -> Optional[Solution]:
        """Optional[Solution]: Best solution found by the heuristic."""
        return self._best_solution

    @best_solution.setter
    def best_solution(self: 'Heuristic', value: Optional[Solution]) -> None:
        self._best_solution = value

    @property
    def iters(self: 'Heuristic') -> int:
        """int: Iteration counter."""
        return self._iters

    @iters.setter
    def iters(self: 'Heuristic', value: int) -> None:
        self._iters = value

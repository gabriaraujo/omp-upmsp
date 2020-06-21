from classes import Stockpile, Engine, Input, Output
from typing import List, Dict, Tuple, Union, Any, Optional


# type aliases para os dados de entrada
Stockpiles = List[Stockpile]
Engines = List[Engine]
Inputs = List[Input]
Outputs = List[Output]
Travels = List[List[float]]
Information = Union[str, Stockpiles, Engines, Inputs, Outputs, Travels]
Data = Dict[str, Union[Information, Any]]

# type aliases para os dados de saída
Works = List[Dict[str, Union[int, float]]]
Qualities = List[Dict[str, Union[str, int, float]]]
Deliveries = List[Dict[str, Union[float, Qualities]]]
Result = Dict[str, Union[str, float, Works, Deliveries]]

# type aliases para o modelo linear
Weights = Dict[str, List[float]]
Solution = Tuple[Optional[float], Weights, Weights]

# type aliases para o solver
Route = List[Tuple[float, int, int, str]]
Routes = List[List[Tuple[int, str]]]

# type aliases para os dados do gerador de instâncias
QualityIni = List[Dict[str, Union[str, float]]]
Stock = List[Dict[str, Union[int, float, List[int], QualityIni]]]
Eng = List[Dict[str, Union[int, float, List[int]]]]
Inp = List[Dict[str, Union[int, float, QualityIni]]]
Out = List[Dict[str, Union[int, float, Qualities]]]
Instance = Dict[str, Union[str, Stock, Eng, Inp, Out, Travels]]

# type aliases para as informações do arquivo .json
Info = Dict[str, Union[Result, Instance]]

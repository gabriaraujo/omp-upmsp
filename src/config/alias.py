from classes import Stockpile, Engine, Input, Output
from typing import List, Dict, Tuple, Union

# type aliases para os dados de entrada
Stockpiles = List[Stockpile]
Engines = List[Engine]
Inputs = List[Input]
Outputs = List[Output]
Datas = Dict[str, Union[Stockpiles, Engines, Inputs, Outputs, List[float]]]

# type aliases para os dados de saída
Works = List[Dict[str, Union[int, float]]]
Qualities = List[Dict[str, Union[str, int, float]]]
Deliveries = List[Dict[str, Union[float, Qualities]]]
Result = Dict[str, Union[str, float, Works, Deliveries]]

# type aliases para o modelo linear
Weitghs = Dict[str, List[float]]
Solution = Tuple[float, Weitghs, Weitghs]

#type aliases para o solver
Route = List[Tuple[float, int, int]]
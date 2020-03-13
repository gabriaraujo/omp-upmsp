from classes.stockpile import *
from classes.engine import *
from classes.input import *
from classes.output import *
import ujson, sys

with open(sys.argv[1], "r") as file:
    data_store = ujson.loads(file.read())

stockpile = []
for data in data_store["stockpiles"]:
    sp = Stockpile(data["id"], data["position"], data["capacity"], data["engines"])
    stockpile.append(sp)

engine = []
for data in data_store["engines"]:
    eng = Engine(data["id"], data["speedStack"], data["speedReclaim"], data["stockpiles"])
    engine.append(eng)

input = []
for data in data_store["inputs"]:
    inp = Input(data["id"], data["source"], data["weight"], data["quality"], data["time"])
    input.append(inp)

output = []
for data in data_store["outputs"]:
    out = Output(data["id"], data["destination"], data["weight"], data["qualityGoal"],
    data["qualityUpperLimit"], data["qualityLowerLimit"], data["time"])
    output.append(out)

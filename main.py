import json


name = input("What is your name?: ")
clan = input("What is your clan?: ")

route = "./explicacion/data/coder.json"

#newline: para saltos de linea
#encoding: cualquier caracter especial el archivo pueda identificarlo
with open(route, "w", newline="", encoding="utf-8") as fileCoders:
    json.dump({ "name": name, "clan": clan}, fileCoders, indent = 4)

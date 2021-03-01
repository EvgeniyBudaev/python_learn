import json
import requests

class Tournament:
  def __init__(self, name, year):
    self.name = name
    self.year = year

  @classmethod
  def from_json(cls, json_data):
    return cls(**json_data)  


tournaments = {
  "Aeroflot Open": 2010,
  "FIDE WORLD Cup": 2018,
  "FIDE Grand Prix": 2016
}

# dumps - возвращает строчку в виде json
# dump - строчку складывает в файл на диске
# indent - управляет отступами в json

json_data = json.dumps(tournaments, indent = 2) # serialization
print(json_data) # {
  # "Aeroflot Open": 2010,
  # "FIDE WORLD Cup": 2018,
  # "FIDE Grand Prix": 2016
# }

loaded = json.loads(json_data) # deserialization
print(loaded) # {'Aeroflot Open': 2010, 'FIDE WORLD Cup': 2018, 'FIDE Grand Prix': 2016}

t1= Tournament("Aeroflot Open", 2010)
# json_data1 = json.dumps(t1) # error
json_data2 = json.dumps(t1.__dict__)
print(json_data2)
t = Tournament(**json.loads(json_data2))
print(f"name={t.name}, year={t.year}") # name=Aeroflot Open, year=2010


class ChessPlayer:
  def __init__(self, tournaments):
    self.tournaments = tournaments

  @classmethod
  def from_json(cls, json_data):
    tournaments = list(map(Tournament.from_json, json_data["tournaments"]))
    return cls(tournaments)  

tour1 = Tournament("Aeroflot Open", 2010)
tour2 = Tournament("FIDE WORLD Cup", 2018)  
tour3 = Tournament("FIDE Grand Prix", 2016)  
p1 = ChessPlayer([tour1, tour2, tour3])
json_data3 = json.dumps(p1, default = lambda obj: obj.__dict__)
print(json_data3) # {"tournaments": [{"name": "Aeroflot Open", "year": 2010}, {"name": "FIDE WORLD Cup", "year": 2018}, {"name": "FIDE Grand Prix", "year": 2016}]

json_data4 = json.dumps(p1, default=lambda obj: obj.__dict__, indent=4, sort_keys=True)
print('json_data4: ', json_data4)
# json_data4:  {
    # "tournaments": [
        # {
            # "name": "Aeroflot Open",
            # "year": 2010
        # },
        # {
            # "name": "FIDE WORLD Cup",
            # "year": 2018
        # },
        # {
            # "name": "FIDE Grand Prix",
            # "year": 2016
        # }
    # ]
# }

decoded_player = ChessPlayer.from_json(json.loads(json_data4))
print('decoded_player: ', decoded_player) # <__main__.ChessPlayer object at 0x7fe348034c70>
print('decoded_player.tournaments: ', decoded_player.tournaments)

# ===
with open("player.json", "w") as file:
  json.dump(p1, file, default=lambda obj: obj.__dict__)

with open("player.json", "r") as read_file:
  data = json.load(read_file)

# ===
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
print(todos)    



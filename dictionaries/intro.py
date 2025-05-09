from typing import List, Dict

def create_dict(name: str, age: int) -> Dict[str, int]:
  return {name: age}

def list_to_dict(words: List[str]) -> Dict[str, int]:
  myDicts = {}

  for i in range(len(words)):
    curr = words[i]
    myDicts[curr] = i

  return myDicts


print(create_dict("Ferri", 25))
print(create_dict("Ari", 35))
print(create_dict("Anna", 45))

print(list_to_dict(["Ferri", "Ari", "Anna"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))

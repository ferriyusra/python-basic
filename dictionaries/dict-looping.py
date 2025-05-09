from typing import Dict, List

def get_dict_keys(age_dict: Dict[str,int]) -> List[str]:
  keys = []
  for key in age_dict:
    keys.append(key)
  return keys

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
  val = []
  for key in age_dict:
    val.append(age_dict[key])

  return val

dict_1 = {"Ferri": 25, "Ari": 30, "Uw": 22}
dict_2 = {"Ferro": 24, "Ferro2": 25, "Ferro3": 26}

print(get_dict_keys(dict_1))
print(get_dict_keys(dict_2))

print(get_dict_values(dict_1))
print(get_dict_values(dict_2))
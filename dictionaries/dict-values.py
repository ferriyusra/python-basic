from typing import Dict, List


def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
  return list(age_dict.values())

print(get_dict_values({"Ferri": 25, "Beni": 30, "Auri": 35}))
print(get_dict_values({"Ferri": 25, "Beni": 30, "Auri": 35, "David": 40}))

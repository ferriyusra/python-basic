from typing import List, Set

def list_to_set(nums: List[int]) -> Set[int]:
  mySet = set()
  for num in nums:
    mySet.add(num)
  
  return mySet

print(list_to_set([1, 2, 3, 4, 5]))
print(list_to_set([1, 1, 2, 2, 3, 3]))
print(list_to_set([1, 2, 3, 4, 5, 5, 5, 3, 4, 5]))

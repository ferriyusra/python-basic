from typing import List

def contains_duplicate(words: List[str]) -> bool:
  mySet = set()
  for w in words:
    if w in mySet:
      return True

    mySet.add(w)
  
  return False

print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))

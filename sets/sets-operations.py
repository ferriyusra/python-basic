from typing import List

def count_unique_words(words: List[str]) -> int:
  mySet = set()
  for word in words:
    mySet.add(word)
  
  print(mySet)
  return len(mySet)

print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
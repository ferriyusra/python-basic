from typing import Dict

def count_characters(word: str) -> Dict[str, int]:
  charCount = {}
  for char in word:
    if char in charCount:
      charCount[char] += 1
    else:
      charCount[char] = 1
  
  return charCount


print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("tsiiiuuu siuuuuu"))
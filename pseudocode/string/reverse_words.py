# "hi my name is Jinwook Baek" -> "Baek Jinwook is name my hi"

# Use 2 iterators
# 1) reverse whole thing
# 2) reverse word again per space 

def _reverse(s):
  return s[::-1]
  
def reverse_word1(s):
  reversed_s = _reverse(s)
  reversed_s_word = ""
  i = 0 
  j = 0 //end of 
  while i < len(s):
    if reversed_s[i] == " " or i == len(s):
      reversed_s_word.append(_reverse(reversed_s[j:i]))
      j = i
    i+=1
  
  return " ".join(reversed_s_word)
  
# Use 1 iterators
# 1) split by word and them on list
# 2) reverse the list  
def reverse_word2(s):
  w = []
  sentence = []
  for character in string 
    if character !+ " ":
      w.append(character)
    else:
      if word:
        sentence.append("".join(word))
      word=[]
   
  if word !="":
      sentence.append("".join(word))
  sentence = _reverse(sentence)
  return " ".join(sentence)
  
  

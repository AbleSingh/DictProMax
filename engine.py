with open("words_alpha.txt", "r") as engWord:
  lines = engWord.readlines()

allword =[]

for l in lines:
  allword.append(l.replace("\n",""))
  
inputWord = input("enter the letters :: ")
inputWord = inputWord.lower()
listOfLetters = list(inputWord)
listOfLetters.sort()
listOfLetters = list(set(listOfLetters))
listOfLetters.sort()


selectedWords=[x for x in allword if len(x)==len(inputWord)]


def finalCode():
  for letter1 in listOfLetters:
    for word1 in selectedWords:
      if (word1.count(letter1) == inputWord.count(letter1)):
        continue
      else:
        selectedWords.remove(word1)
  return len(selectedWords)

len1 = finalCode()
len2 = finalCode()

k = False

while(k==False):
  if(len1 == len2):
    k = True
  else:
    len1 = len2
    len2 = finalCode()
    k = False

print(selectedWords)

from definition import meaningGet

for wordFound in selectedWords:
  print(wordFound + " :: ")
  meaningGet(wordFound)
  print("")
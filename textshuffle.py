from urllib.request import urlopen
import random

data = urlopen("https://raw.githubusercontent.com/aparrish/rwet/master/frost.txt")

input = ""

for line in data:
    input += line.decode("utf-8")

paragraphs = input.split("\n\n")

poem = []

for paragraph in paragraphs:
  sentences = paragraph.split("\n")
  poem.append([])
  for sentence in sentences:
      words = sentence.split(" ")
      poem[-1].append([])
      for word in words:
          poem[-1][-1].append(word)

random.shuffle(poem)

for paragraph in poem:
    random.shuffle(paragraph)
    for sentence in paragraph:
        random.shuffle(sentence)

output = ""

for paragraph in poem:
    for sentence in paragraph:
        for word in sentence:
            output += word
            output += " "
        output += "\n"
    output += "\n"

print(output)
    


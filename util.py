import random

# checks messages
def containsAny(searchIn, strings): 
  searchIn = searchIn.lower()
  for i in strings:
    if i in searchIn: return i
  return None

# turns file into list
def textRead(fname):
  with open(fname) as f:
    fList = f.readlines()
    for i in range(len(fList)):
      fList[i] = fList[i].strip("\n")
  return fList

# selects random joke from list
def randomYourMomJoke(victim=""):
  insultList = textRead("insults/yourMom.txt")

  if victim == "":
    return random.choice(insultList)
  else:
    return "Hey " + victim + ", " + random.choice(insultList)

# creates a random joke that usually makes no sense
def generateYourMomJoke(victim=""):
  verb = random.choice(textRead("insults/verbs.txt"))
  noun = random.choice(textRead("insults/nouns.txt"))
  adj = random.choice(textRead("insults/adjectives.txt"))
  joke_format = random.choice(textRead("insults/jokeTemplates.txt"))

  # creates joke from random template and random words
  insult = joke_format.format(verb = verb, noun = noun, adjective = adj)

  if victim == "":
    return insult
  else:
    return "Hey " + victim + ", " + insult

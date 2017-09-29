from random import choice

rolls = {
  0:"None",
  1: "Pair",
  2: "Two Pairs",
  3: "Three of a kind",
  4: "Four of a kind",
  5: "Yahtzee!",
  6: "Full House",
  7: "Large Straight"
}

dice = []

for x in range(5):
  dice.append(choice([1,2,3,4,5,6]))
  print "Dice %i: %i" % (x + 1, dice[x])

#find the number of repeated numbers in the roll
def numOfRepeats(dice):
  repeats = [0,0,0,0,0,0] # each rep. one number (1-6)
  for x in dice: #loop through the dice values
    repeats[x-1] += 1 #add one to repeats for that number
  return repeats

#find the number of groups of repeats in the roll (ex: 2:2 means 2 numbers are doubled aka 2 pairs)
def numOfGroups(repeats):
  groups = {1:0, 2:0, 3:0, 4:0, 5:0} # keys are the number of repeats, values are the number of each group of repeats
  for x in repeats: #loop through the number of repeats 
    if (x != 0): #as long as a number is repeated
      groups[x] += 1 #add one to the value under the appropriate key
  return groups

def rollResults(dice, groups, rolls):
  dice.sort() #sort helps with straights
  if groups[5] == 1: #if a Yahzee 
    return rolls[5]
  elif groups[4] == 1: #four of a kind 
    return rolls[4]
  elif groups[3] == 1 and groups[2] == 1: #Full house(1 group of 3, 1 group of 2)
    return rolls[6]
  elif groups[3] == 1: #three of a kind
    return rolls[3]
  elif groups[2] == 2: #two pairs
    return rolls[2]
  elif groups[2] == 1: #one pair
    return rolls[1]
  else: #when no repeats exist
    if dice[4] == 5 or dice[0] == 2:
      return rolls[7] # straight of 1,2,3,4,5 or 2,3,4,5,6
    else:
      return rolls[0] # no pattern

print rollResults(dice, numOfGroups(numOfRepeats(dice)), rolls)

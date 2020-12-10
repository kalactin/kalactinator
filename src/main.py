import random

# scan user input
print("Welcome to Kalactinator 1.0")
team1 = (input("Team 1 Name: "))
team2 = (input("Team 2 Name: "))
team1skill = float(input("Team 1 Skill: "))
team2skill = float(input("Team 2 Skill: "))
team1style = float(input("Team 1 Style: "))
team2style = float(input("Team 2 Style: "))
maxrank = float(input("Max Rank: "))

if maxrank < team1skill:
  print("SKILL EXCEEDS MAX RANK PLEASE REENTER YOUR TEAMS")
if maxrank < team2skill:
  print("SKILL EXCEEDS MAX RANK PLEASE REENTER YOUR TEAMS")
if team1style > 5.00:
  print("YOUR STYLE MODIFIERS HAVE BEEN INPUT WRONG. PLEASE RESCORINATE")
if team2style > 5.00: 
  print("YOUR STYLE MODIFIERS HAVE BEEN INPUT WRONG. PLEASE RESCORINATE")

if team1skill <= 1:
  team1skill = 1
if team2skill <= 1:
  team2skill = 1

# assign base values
baseAttacks = 40
ratioEffect = 0.5
randCoefficient = 0.4
rankCoefficient = 0.6
pGoalCeiling = 0.4
pGoalFloor = 0.05
chanceZeroToMaxRankVictory = 0.05
hcaEffect = 0.07
periods = 2
styleEffect = 0.008
periodModifier = 1/periods

# generate style Modification
overallStyle = team1style + team2style
styleValue = overallStyle * styleEffect

# find pGoal of Teams

factor1 = random.random() 
factor1comparator = .4
factor2 = random.random()
factor2comparator = .4

if factor1 > factor1comparator:
 factor1 = .350
if factor1 < .111111:
   factor1 = .15
   
if factor2 > factor2comparator:
 factor2 = .350
if factor2 < .111111:
   factor2 = .15

attackModifier1 = (factor1 * 15) + baseAttacks * periodModifier
attackModifier2 = (factor2 * 15) + baseAttacks * periodModifier

pGoal1 = (0.4 - factor1) * ((team1skill/team2skill * rankCoefficient)) + (hcaEffect) + styleValue
pGoal2 = (0.4 - factor2) * ((team2skill/team1skill * rankCoefficient)) + styleValue

if pGoal1 >= pGoalCeiling:
  pGoal1 = pGoalCeiling
if pGoal2 >= pGoalCeiling:
  pGoal2 = pGoalCeiling
  
if pGoal1 <= pGoalFloor:
  pGoal1 = pGoalFloor
if pGoal2 <= pGoalFloor:
  pGoal2 = pGoalFloor
  
periodScore1 = round((pGoal1 * attackModifier1 + random.randint(0,7))* periodModifier)
periodScore2 = round((pGoal2 * attackModifier2 + random.randint(0,7))* periodModifier)

score1 = periodScore1 * periods
score2 = periodScore2 * periods 

if score1 == score2:
  OTscore1 = score1 + random.randint(1,4)
  OTscore2 = score2 + random.randint(1,4)
  print("Game went to Overtime")
  print(team1, OTscore1, "-", OTscore2, team2)
print("")
print(team1, score1, "-", score2, team2)

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

if team1skill <= 1:
  team1skill = 1
if team2skill <= 1:
  team2skill = 1

# assign base values
baseAttacks = 29
randCoefficient = 0.3
rankCoefficient = 0.7
pGoalCeilingSuperior = 0.850
pGoalCeilingInferior = 0.850
pGoalFloorSuperior = 0.015
pGoalFloorInferior = 0.015
chanceZeroToMaxRankVictory = 0.05
hcaEffect = 0.07

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

attackModifier1 = (factor1 * 15) + baseAttacks
attackModifier2 = (factor2 * 15) + baseAttacks

pGoal1 = (1 - factor1) * ((team1skill/team2skill * rankCoefficient))

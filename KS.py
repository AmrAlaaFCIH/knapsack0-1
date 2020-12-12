from main import Swarm

knapsack=[(5, 10), (2, 2), (2, 2), (10, 2), (1, 1)]
weightLimit=6

space=Swarm(knapsack,weightLimit)
for _ in range(150):
    space.setGlobalAndPersonalBest()
    space.move()


for i,x in enumerate(space.globalBestPositions):
    if x==0:
        pass
    else:
        print(f"element Number {i+1} with value = {knapsack[i][0]}$ and weight = {knapsack[i][1]}kg")

print(f"SOLVED! with weight limit = {weightLimit}kg and with Maximum value of {space.globalBestValue}$")
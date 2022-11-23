# Given that the following numbers have been drawn 
drawn = [5, 11, 9, 42, 3, 49]
# given that you choose the following bets
bets = [3, 7, 11, 42, 34, 49]
# how many numbers did you hit?
hits_num = []
hits = 0

for i in drawn:
    for j in bets:
        if j != i:
            continue
        else:
            hits_num.append(j)
            hits += 1
            
print("Jackpots! ", hits_num, "\nTotal hits", hits)
# using 'in' and 'not in' operator for the same program
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)
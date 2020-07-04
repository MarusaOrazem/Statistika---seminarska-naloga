import csv
from random import sample
import statistics
import math

#a)

#first we gather the info. We only need the column "dohodek".
N = 43886
income = []
with open('Kibergrad.csv') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        income.append(int(row[3]))

#we need n = 400 units chosen random from income
n = 400
incomeSample = sample(income,n)

mean = statistics.mean(incomeSample)

#se
sum = 0
for i in range(n):
    sum += (incomeSample[i] - mean)**2

se = math.sqrt((N-n)/(n*N*(N-1))*sum)

#interval zaupanja X+-1.96*se(X)
lowest = mean-1.96*se
highest = mean+1.96*se

print("mean: " + str(mean))
print("se: " + str(se))
print("interval: [" + str(lowest) +", " + str(highest) + "]")

#b)

N1 = 10149
N2 = 10390
N3 = 13457
N4 = 9890

n1 = 92
n2 = 95
n3 = 123
n4 = 90

#we need to split the data
income_1 = income[:N1]
income_2 = income[N1:N1+N2]
income_3 = income[N1+N2:N1+N2+N3]
income_4 = income[N1+N2+N3:]

#we take samples from each one individualy
sample1 = sample(income_1, n1)
sample2 = sample(income_1, n2)
sample3 = sample(income_1, n3)
sample4 = sample(income_1, n4)

mean_strat = statistics.mean(sample1 + sample2 + sample3 + sample4)

#se
mean1 = statistics.mean(sample1)
mean2 = statistics.mean(sample2)
mean3 = statistics.mean(sample3)
mean4 = statistics.mean(sample4)
all_means = [mean1, mean2, mean3, mean4]

all_N = [N1, N2, N3, N4]
all_n = [n1, n2, n3, n4]
all_sample = [sample1, sample2, sample3, sample4]

varX = 0
for k in range(4):
    temp = (all_N[k]* (all_N[k] - all_n[k]) ) / (N**2 * all_n[k] *(all_n[k] - 1))
    temp2 = 0
    for j in range(all_n[k]):
        temp2 += (all_sample[k][j]-all_means[k])**2
    varX += temp*temp2
se_strat = math.sqrt(varX)

#interval X+-1.96 se
lowest_strat = mean_strat - 1.96* se_strat
highest_strat = mean_strat + 1.96 *se_strat

print("mean_strat: " + str(mean_strat))
print("se_strat: " + str(se_strat))
print("interval: [" + str(lowest_strat) +", " + str(highest_strat) + "]" )

print("mean of whole population: " + str( statistics.mean(income)))

#weighted mean
mean_w = 0
for i in range(4):
    mean_w += (all_N[i] / N )* all_means[i]

print("weighted mean: " + str(mean_w))












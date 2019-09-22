temperatures_arr = [21, 23, 26, 22, 25, 20, 19, 23]
i = 0
max = 0
while i < 8:
    temp = temperatures_arr[i]
    i = i +1
    if temp > max:
        max = temp

print(max)

temperatures_arr = [21, 23, 26, 22, 25, 20, 19, 23]

x = min(21, 23, 26, 22, 25, 20, 19, 23)
print(x)


import statistics

# list of positive integer numbers
data1 = [80, 90, 100, 150, 120, 110, 160, 110, 100]

x = statistics.mean(data1)

# Printing the mean
print("Mean is :", x)

import statistics

power_arr = [4, 5, 2, 6, 3, 7, 8, 9, 6, 5, 2]
print(statistics.median(power_arr))

import statistics

x = statistics.mode([1, 1, 2, 3, 3, 3, 4, 5])
print("The mode is", x)

import statistics
values = [8, 11, 9, 14, 9m 15, 18, 6, 9, 10]
mode = statistics.mode(values)

print(mode)

values = [8, 9, 10, 10, 10, 10, 11, 11, 11, 12, 13]
mode = statistics.mode(values)
print(mode)

x = range(1, 5, 9)

for n in x:
  print(n)

import statistics

x = statistics.stdev([1, 1, 2, 3, 3, 3, 4, 5])
print("The standard deviation is", x)

results = [1, 1, 2, 3, 3, 3, 4, 5]
x = sum(results) / len(results)
Jimmy_var_number = sum((xi - x) ** 2 for xi in results) / len(results)
print("The variance number is", Jimmy_var_number)

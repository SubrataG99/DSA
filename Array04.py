# You are given an array of priced where prices[i] is the price of the given stock on an "ith" day. You want to maximise your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can acheive from this transaction. If you cannot acheive any profit, return 0

n = int(input("Enter number of days : "))
price = []
profit = 0
key = 0
s = 0

for i in range(n) :
    price.append(int(input("Enter the price : ")))
print(price)

mini = price[0]
for i in range(n) :
    if (mini > price[i]) :
        mini = price[i]
        key = i
print("Buy stocks at", key+1, "day when price is", price[key])

for i in range(key, n) :
    if (price[i] - mini) > profit :
        profit = price[i] - mini
print("Total profit will be : ", profit)
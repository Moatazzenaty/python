total_budget = int ( input ("enter yout total budget = "))
first_item = int (input ( "first item cost = " ))
second_item = int ( input ("second item cost = "))
third_item = int (input ( "third item cost = " ))
cost = first_item + second_item + third_item
print("the cost of items = " , cost )
if cost > total_budget :
    print("the cost is more than the budget the cost is" , cost)
else:
    print("your budget is more than the cost your budget is", total_budget)

The_Difference = total_budget - cost 
if cost < total_budget:
    print("there is money left for you =" , The_Difference)
else:
    print("you need to be in the range of total budget" , The_Difference)
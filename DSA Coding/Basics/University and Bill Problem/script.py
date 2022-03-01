Cost_of_one_computer = float(input("Enter the cost of one computer : Rs."))
Number_of_computers = int(input("Enter the number of computers : "))
Cost_of_one_table = float(input("Enter the cost of one table : Rs."))
Number_of_tables = int(input("Enter the number of tables : "))
Cost_of_one_chair = float(input("Enter the cost of one chair : Rs."))
Number_of_chairs = int(input("Enter the number of chairs : "))
Number_of_hours_worked = float(input("Enter the number of hours labours worked : "))
Wages_per_hour = float(input("Enter the wages for labours per hour : Rs."))
Cost_of_computers = Cost_of_one_computer * Number_of_computers
Cost_of_furniture = (Cost_of_one_table * Number_of_tables) + (Cost_of_one_chair * Number_of_chairs)
Labour_Cost = Number_of_hours_worked * Wages_per_hour
Total_Cost = Cost_of_computers + Cost_of_furniture + Labour_Cost
print("Bill :")
print("Total cost of Computers : Rs.", Cost_of_computers)
print("Total cost of Furniture : Rs.", Cost_of_furniture)
print("Total Labour charges : Rs.", Labour_Cost)
print("Total cost : Rs.", Total_Cost)

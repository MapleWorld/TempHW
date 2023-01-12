
sales = [
    [[0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0]]
]

for i in range (0,39):
    year = int(input("Enter year number (0-4) \n"))
    while year < 0 or year > 4:
        print("Input not in range, try again")
        year = int(input("Enter a year from (0-4) \n"))
    quarter = int(input("Enter number (0-3) \n"))
    
    while quarter < 0 or quarter > 3:
        print("Input not in range, try again")
        quarter = int(input("Enter a quarter from (0-3) \n"))
    department = int(input("Enter number (0-1) \n"))
    
    while department < 0 or department > 1:
        print("Input not in range, try again")
        department = int(input("Enter a department from (0-1) \n"))
    profit = input("Enter profit \n")
    
    sales[year][quarter][department] = float(profit)

print (sales)

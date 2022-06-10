from datetime import datetime
 
my_string = str(input('Enter date(yyyy-mm-dd): '))
my_date = datetime.strptime(my_string, "%Y-%m-%d")
 
print(my_date)
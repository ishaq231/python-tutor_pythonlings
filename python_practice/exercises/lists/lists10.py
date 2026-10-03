# Exercise: Lists 10
# I AM NOT DONE
#
# You have a list of sales records. Each record is a dictionary with
# "product", "units" and "price_per_unit".
#
# Finish the code so that:
#   `revenue_list`  : a list of the money made for each record (units * price_per_unit),
#                     but ONLY for records where units is more than 10
#   `total_revenue` : all the numbers in `revenue_list` added together
#
# You should get:
#   revenue_list  == [270.0, 500.0, 880.0]
#   total_revenue == 1650.0

sales = [
    {"product": "apple",  "units": 5,  "price_per_unit": 1.20},
    {"product": "banana", "units": 15, "price_per_unit": 18.0},
    {"product": "cherry", "units": 8,  "price_per_unit": 3.50},
    {"product": "date",   "units": 20, "price_per_unit": 25.0},
    {"product": "elderberry", "units": 40, "price_per_unit": 22.0},
]

revenue_list = []
for record in sales:
    pass  # replace with filter + revenue calculation

total_revenue = ???

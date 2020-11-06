employees = {'Alice': 100000,
             'Bob': 99817,
             'Carol': 122908,
             'Frank': 88123,
             'Eve': 93121
             }

# Create a list of duples to contain people with the salary above 10000
employees_with_more_than_10000 = [(k, v)
                                  for k, v in employees.items() if v >= 100000]
print(employees_with_more_than_10000)

# Create a list of duples to contain people whose names are more than or equal to 4 characters
employees_with_name_more_than_4_charaters = [
    (k, v) for k, v in employees.items() if len(k) >= 4]
print(employees_with_name_more_than_4_charaters)

# Create a list of duples to contain people whose names are starting with "E"
employees_with_name_startswith_E = [
    (k, v) for k, v in employees.items() if k.startswith('E')]
print(employees_with_name_startswith_E)

# Create a list of duples to contain people whose names are ending with "k"
employees_with_name_end_with_k = [
    (k, v) for k, v in employees.items() if k[-1] == 'k']
print(employees_with_name_end_with_k)


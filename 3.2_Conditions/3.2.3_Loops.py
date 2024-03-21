################################
# Döngüler (LOOPS)
################################


# for loop

students = ["john", "mark", "venessa", "mariam"]

for student in students:
    print(student)

for student in students:
    print(student.upper())

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary)

for salary in salaries:
    print(int(salary * 20 / 100 + salary))


def new_salary(salary, rate):
    return int(salary * rate / 100 + salary)


new_salary(1500, 10)

for salary in salaries:
    print(new_salary(salary, 10))

salaries2 = [12000, 20004, 30005, 406500, 50700]

for salary in salaries2:
    print(new_salary(salary, 10))

for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 10))
    else:
        print(new_salary(salary, 20))

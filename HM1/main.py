import pprint


def task_1():

    companies = [
        {'name': 'Apple', 'hq': 'Cupertino, California'},
        {'name': 'Google', 'hq': 'Mountain View, California'},
        {'name': 'Netflix', 'hq': 'Los Gatos, California'}
    ]

    # Using for loop
    def task_1_1():
        for i in companies:
            print(i['name'])

    # Using list comprehension
    def task_1_2():
        comprehensions = [company['name'] for company in companies]
        for info in comprehensions:
            print(info)

    return task_1_1, task_1_2

nested_task_1_1, nested_task_1_2 = task_1()

print("Running task_1_1:")
nested_task_1_1()

print("Running task_1_2:")
nested_task_1_2()

def task_2():
     #remove dublicates
     companies = ['netflix', 'apple', 'apple', 'google']
     dedup_companies = list(dict.fromkeys(companies))
     print(dedup_companies)

print("Running task_2:")
task_2()

def task_3():
     keys = ['name', 'hq', 'no_employees', 'established']

     values = ['Apple', 'Cupertino, California', 161000, 1976]

     key_value = dict(zip(keys, values))
     pprint.pprint(key_value)

print("Running task_3:")
task_3()

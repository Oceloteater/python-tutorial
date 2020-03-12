# testing code
from typing import List

# friends = ['Adam', 'Catherine', 'Aaron']
# lads = [friend for friend in friends if friend.startswith('A')]
# print(lads)
# print('ID: '+str(id(friends))+' ID: '+str(id(lads)))

ages = [
    {'name': 'Adam', 'age': 31},
    {'name': 'Catherine', 'age': 27},
    {'name': 'Aaron', 'age': 25}
]
# for peeps in ages:
#     for name, age in peeps.items():
#         print(f'{name} : {age}')

# sequence = [1, 4, 6, 7]
# doubled = [double(x) for x in sequence]
# doubled = map(double, sequence)
# double = list(map(lambda x: x * 2, sequence))

# print(double)


def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)


def named(**kwargs):
    print(kwargs)


def print_nicely(*args, **kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f'{arg}: {value}')


#print_nicely(*ages, name='adam', age=31)
print(list_avg([12,33,13]))

# testing code

# friends = ['Adam', 'Catherine', 'Aaron']
# lads = [friend for friend in friends if friend.startswith('A')]
# print(lads)
# print('ID: '+str(id(friends))+' ID: '+str(id(lads)))

ages = [
    {'name': 'Adam', 'age': 31},
    {'name': 'Catherine', 'age': 27},
    {'name': 'Aaron', 'age': 25}
]

for whore in ages:
    for name, age in whore.items():
        print(f'{name} : {age}')

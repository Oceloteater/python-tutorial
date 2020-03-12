# first class function
def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f'Could not find an element with {expected}')


# func we pass in to be called by another function
def get_friends_name(friend):
    return friend['name']


friends = [
    {'name': 'Adam', 'age': 31},
    {'name': 'Catherine', 'age': 27},
    {'name': 'Aaron', 'age': 25}
]

print(search(friends, 'Adam', get_friends_name))

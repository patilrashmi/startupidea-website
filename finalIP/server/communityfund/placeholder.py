import random

lorem_ipsum = ('Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante '
               'sollicitudin commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra '
               'turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis '
               'in faucibus.')


def user(user_id):
    return {
        'id': user_id,
        'name': 'User ' + str(user_id)
    }


def idea(idea_id):
    goal = random.randint(0, 100000)
    funded = random.randint(0, goal)
    return {
        'id': idea_id,
        'name': "Idea " + str(idea_id),
        'description': lorem_ipsum,
        'goal': goal,
        'amount_funded': funded,
        'percent_funded': round((funded / goal) * 100)
    }


def category(category_id):
    return {
        'id': category_id,
        'name': "Category " + str(category_id),
        'description': lorem_ipsum,
        'subscribers': [user(i) for i in range(10)],
        'ideas': [idea(i) for i in range(5)],
        'comments': [comment(i) for i in range(5)]
    }


def comment(user_id):
    return {'user_id': user_id,
        'time': 'August 25, 2014 at 9:30 PM',
        'body': lorem_ipsum}
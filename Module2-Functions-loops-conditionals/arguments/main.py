# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, greeting='Hello, <name>!'):
    return greeting.replace('<name>', name)

print(greet('Doc'))
print(greet('Bob', "What's up, {name}"))


def force(mass, body='earth'):
    gravity_factors = {
        'mercury': 3.7,
        'venus': 8.9,
        'earth': 9.8,
        'moon': 1.6,
        'mars': 3.7,
        'jupiter': 23.1,
        'saturn': 9.0,
        'uranus': 8.7,
        'neptune': 11.0,
        'pluto': 0.7
        }
    gravity = gravity_factors.get(body)
    return mass * gravity

print(force(0.1,'moon'))

"""
#pull = G × ((m1×m2)/d2)
g = 6.674* 10 ** -11
m1= 0.1
m2 = 5.972*10**24
d = 6.371*10**6
pull = g * ((m1 * m2) / d ** 2)

print(pull)
"""

def pull(m1, m2, d):
    g = 6.674* 10 ** -11
    return (g * ((m1 * m2) / d ** 2))

print(pull(0.1,5.972*10**24,6.371*10**6))
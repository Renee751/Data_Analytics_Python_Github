import requests
import time
import math
import datetime
import sys

# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

###################################################################

url = 'https://en.wikipedia.org/wiki/Zen_of_Python'
request = requests.get(url)
print(request)

try:
    import requests
except ImportError:
    print('module url not found')

# Waarom krijg ik winphy "The Zen of Python is not imported."?
# Met Try krijg ik geen foutmelding + bij  print statement krijg ik URL terug

####################################################################


def wait(seconds):
    time.sleep(seconds)
    print(f'waited {seconds} seconds before printing this')


wait(1)

####################################################################


def my_sin(x):
    answer = math.sin(x)
    return (answer)


print(my_sin(10))
print(my_sin(math.pi / 2))

####################################################################


def iso_now():
    current_time = datetime.datetime.now()
    time_string = current_time.strftime("%Y-%m-%dT%H:%M")
    return (time_string)


print(iso_now())

####################################################################


def platform():
    return (sys.platform)


print(platform())

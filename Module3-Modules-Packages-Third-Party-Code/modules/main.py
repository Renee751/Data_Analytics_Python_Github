import requests
url = 'https://en.wikipedia.org/wiki/Zen_of_Python'
request = requests.get(url)
#print(request.text)

import time

import math

# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

   
def wait(seconds):
    time.sleep(seconds)
    print(f'waited {seconds} seconds before printing this')
    
    
wait(1)


def my_sin(float):
    answer = math.sin(float)
    print(f'sin is {answer}')
    
my_sin(10)
print(math.sin(10))


def iso_now():
    pass
    

"""

try: 
    import time
except ImportError:
    print('module not found')
    
# seconds passed since epoch
seconds = time.time()               #time()
local_time = time.ctime(seconds)    #ctime()
print('Local time:', local_time)

print('This is printed immediately')
#time.sleep(3)                       #sleep()
print('This is printed after 3 seconds')
#time.sleep(4)
print('This is printed after 4 more seconds')

    # time.struct_time
    # time.localtime()

result = time.localtime()
print('Result:', result)
print('\ntm_year:', result.tm_year)
print('tm_hour:', result.tm_hour)
print('tm_yday:', result.tm_yday)

    #gmtime()
current_time = time.gmtime()
print('Current Year:', current_time.tm_year)
print('Month of the year:', current_time.tm_mon)
print('Day of the month:', current_time.tm_mday)

"""
from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())

# unique_koala_facts 

"""
unique_koala_facts =[]
a= 0

if a > 0
random_koala_fact(a)

if fact not in unique_koala_facts:
    unique_koala_facts.append()
    

"""



def unique_koala_facts():
    list_facts = []
    number_unique_facts = 6
    iteration = 0
    interation_max = 1000
    
    while len(list_facts) < number_unique_facts:
        fact = random_koala_fact()
        if fact not in list_facts:
            list_facts.append(fact)
        if number_unique_facts == len(list_facts) or iteration == interation_max:
           break
        iteration += 1
    return list_facts    

print(unique_koala_facts())


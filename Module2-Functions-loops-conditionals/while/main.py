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

def unique_koala_facts(int):
    list_facts = []
    number_unique_facts = int
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

print(unique_koala_facts(1))





def num_joey_facts():
    joey_list_facts = []
    list_facts_total = []
    unique_count = 0
    
    while unique_count < 1000:
        joey_fact = random_koala_fact()
        if 'joey' in joey_fact.lower():
            if joey_fact not in joey_list_facts:
                joey_list_facts.append(joey_fact) 
                unique_count += 1 
            list_facts_total.append(joey_fact)
            if list_facts_total.count(joey_fact) == 10:
                break
    return unique_count
    
print(num_joey_facts())

###


weight_facts = []


def koala_weight():
    iteration_count = 0
    while iteration_count <= 100:
        fact_weight = random_koala_fact()
        if "kg" in fact_weight:
            iteration_count += 1
            break
    for word in fact_weight.split():
        if "kg" in word:
            return int(word[:-3])


print(koala_weight())



product = {
    "name": "tofu",
    "price": 2,
    "producer": {
        "name": "Tofu Company Limited",
        "country_of_origin": "France"
    },
}

print(product["producer"]["country_of_origin"])


students = [
    {
        "name": "Ali",
        "family_name": "Khan",
        "skills": {
            "Python": "beginner",
            "JavaScript": "expert",
        },
        "certificates": [
            {
                "name": "Back-end Development",
                "date_of_completion": "2022-01-17",
            },
            {
                "name": "Back-end Development",
                "date_of_completion": "2022-01-17",
            },
            {
                "name": "Data Analytics with Python",
                "date_of_completion": "",
            },
        ],
    },
    {
        "name": "Jessica",
        "family_name": "van Alphen",
        "skills": {
            "Python": "advanced beginner",
            "JavaScript": "beginner",
        },
        "certificates": [
            {
                "name": "Front-end Development",
                "date_of_completion": "",
            },
            {
                "name": "Back-end Development",
                "date_of_completion": "2022-01-17",
            },
            {
                "name": "Data Analytics with Python",
                "date_of_completion": "2020-01-17",
            },
        ],
    },
]

print(students[1]["skills"]["Python"])  
print(students[0]["certificates"][1]["name"])
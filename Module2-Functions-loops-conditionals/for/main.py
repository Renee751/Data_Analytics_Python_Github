from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """
# 1. function shortest_names:
def shortest_names(countries):
    found_shortest_names = []
    shortest_names_check = min(len(country_name) for country_name in countries)
    for country_name in countries:
        if len(country_name) == shortest_names_check:
            found_shortest_names.append(country_name)
    return found_shortest_names


# 2. function most_vowels:
""" mijn variant 

def most_vowels(countries):
    countries_lowercase = [x.lower() for x in countries] # alles omzetten naar kleine letters
    top3_countries = []
    most_vowels_check = max(x.count('a') + x.count('e') + x.count('i')+ x.count('o')+ x.count('u') for x in countries_lowercase)
    for x in countries_lowercase:
        if (x.count('a') + x.count('e') + x.count('i')+ x.count('o')+ x.count('u')) == most_vowels_check:
            if x not in top3_countries:
                if len(top3_countries)<3:
                    top3_countries.append(x)  
        lowercase.remove(x)
    return top3_countries
    
einde mijn vriant"""

def most_vowels(countries):
    countries_lowercase = [x.lower() for x in countries] # alles omzetten naar kleine letters
    letters_needed = ['a','e','i','o',]
    countries_checked = []
    for country in countries_lowercase:
        for letter in country:
            if letter in letters_needed:
                letters_needed.remove(letter)
            if country not in countries_checked:
                countries_checked.append(country)
            if letters_needed == "":
                break
    return countries_checked
                 

#Converteer de lijst met countries naar lowercase = DONE
#Maak een lijst aan met letters needed = DONE
#Maak een lege lijst aan met landen die je gehad hebt = DONE
#Loop door alle landen heen = DONE
#Loop door alLe letters van een individueel land heen (for letter in country) = DONE
#Als de letter van het land in de letters needed lijst zit, haal hem dan uit de lijst (letters_needed.remove(letter)) = DONE
#Als het land nog niet in de lijst zit met landen die je gehad hebt, voeg hem hier dan aan toe = DONE
#Als de lijst van letters_needed leeg is, return dan de lijst met countries_used = DONE

### waarom krijg ik maar 1 resultaat - en niet de top 3 terug? 

# 3. function alphabet_set
def check_countries_all_letters_alphabet(countries):
    countries_lowercase = [x.lower() for x in countries] 
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    found_countries = []
    for country in countries_lowercase: 
        for letter in country:
            if letter in alphabet:
                alphabet.remove(letter)
            if country not in found_countries:
                found_countries.append(country)
            if alphabet == list(""):
                break
    return(found_countries)
    


# 1. Converteer de lijst met countries naar lowercase 
# 2. Maak een lijst aan met letters needed
# 3. Maak een lege lijst aan met landen die je gehad hebt
# 4. Loop door alle landen heen
# 5. Loop door ale letters van een individueel land heen (for letter in country)
# 6. Als de letter van het land in de letters needed lijst zit, haal hem dan uit de lijst (letters_needed.remove(letter))
# 7. Als het land nog niet in de lijst zit met landen die je gehad hebt, voeg hem hier dan aan toe
# 8. Als de lijst van letters_needed leeg is, return dan de lijst met countries_used

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """


# 1. Call function shortest_names:
print(shortest_names(countries))

#2. Call function most_vowels:
print(most_vowels(countries))

# namen omzetten naar getallen - telling klinkers
## for x in lowercase // for count_vowels in x  // if x == max 3 van sort_count vowels  dan print x
# max 3 van sort_count_vowels

#### PRINT MEESTE VOWELS / voordat ik het in een def zet 
lowercase = [x.lower() for x in countries] # alles omzetten naar kleine letters
most_vowels = max(x.count('a') + x.count('e') + x.count('i')+ x.count('o')+ x.count('u') for x in lowercase)

for x in lowercase:
   if (x.count('a') + x.count('e') + x.count('i')+ x.count('o')+ x.count('u')) == most_vowels:
       print(x)


#3. ALPHABET_SET STAPPENPLAN
print(check_countries_all_letters_alphabet(countries))






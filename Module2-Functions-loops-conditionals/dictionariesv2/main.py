# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line


# Part 1: Create Passport
def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport_items = {'name': name,
                      'date_of_birth': date_of_birth,
                      'place_of_birth': place_of_birth,
                      'height': height,
                      'nationality': nationality}
    return passport_items
  

# Part 2: Add Stamps
def add_stamp(passport_items, country):
    if 'stamps' not in passport_items:
        passport_items['stamps'] = []
    if country != passport_items['nationality'] and country not in passport_items['stamps']:
        passport_items['stamps'].append(country)
    return passport_items


passport = create_passport("John Doe", "1990-01-01", "London", 1.75, "United States")
passport = add_stamp(passport, "Germany")
passport = add_stamp(passport, "Belgium")
print(passport)


# Part 3: Add biometric data
def add_biometric_data(passport_items, name_biometric_data, values_biometric_data, date_biometric_data_recorded):
    if 'biometric' not in passport_items:
        passport_items['biometric'] = {name_biometric_data :{'value': values_biometric_data,
                                                            'date': date_biometric_data_recorded}}
    else: 
        passport_items['biometric'][name_biometric_data] = {'value': values_biometric_data,
                                                            'date': date_biometric_data_recorded}
    return passport_items


omari = create_passport("Omari Muchumba", "1995-07-16", "Kampala", 184.31, "Uganda")
omari = add_biometric_data(omari, "eye_color_left", "blue", "2020-05-05")
omari = add_biometric_data(omari, "eye_color_right", "blue", "2020-05-05")
omari = add_biometric_data(omari, "eye_color_left", "brown", "2022-01-10")
print(omari)

fingerprint_data = {
    "left_pinky": "2378945",
    "left_ring": "2349081",
    "left_middle": "132890",
    "left_index": "9823234",
    "left_thumb": "0924131",
    "right_thumb": "6234923",
    "right_index": "13249734",
    "right_middle": "34023784",
    "right_ring": "12332538",
    "right_pinky": "32458970",
}
omari = add_biometric_data(omari, "finger_prints", fingerprint_data, "2022-01-12")
print(omari)
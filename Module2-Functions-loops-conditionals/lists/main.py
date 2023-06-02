# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line


#sorting with .sort - changes the order forever
def alphabetical_order(movies):
    movies.sort()
    return movies

print(alphabetical_order(['Jaws (1 en 2)','Midway - 1976','Star Wars (1 t/m 9) - 1977 t/m 2019','Close Encounters of the Third Kind - 1977','Superman - 1978','1941 - 1979','Indiana Jones (1 t/m 4) - 1981 t/m 2008','E.T. the Extra-Terrestrial - 1982','Born on the Fourth of July - 1989','Always - 1989','Presumed Innocent - 1990','Home Alone (1 en 2) - 1990 t/m 1993','Hook - 1991','JFK - 1991','Far and Away - 1992','Jurassic Park (1 en 2) - 1993 t/m 1997','Schindler List - 1993','Sleepers - 1996','Seven Years in Tibet - 1997','Saving Private Ryan - 1998','Stepmom - 1998','The Patriot - 2000','A.I.: Artificial Intelligence - 2001']))


###  Excercise = won golden globe award = true ###

# 1: Nominated work in lower cases
def nominated_work_lower(nominated_work):
    return [x.lower() for x in nominated_work]
print(nominated_work_lower(['The Poseidon Adventure', 'Cinderella Liberty', 'Tom Sawyer', 'Earthquake', 'Jaws', 'Close Encounters of the Third Kind', 'Star Wars: Episode IV A New Hope']))

# 2: films die een globe hebben gewonnen in kleine letters
"""
def won_golden_globe_lower(won_golden_globe_list):
    return [x.lower() for x in won_golden_globe_list]
print(won_golden_globe_lower(['Star Wars: Episode IV A New Hope','Jaws']))

def won_golden_globe(movie_lower):
    movie_lower.lower()
    return movie_lower
""" 

won_golden_globe_movie_list = ['star Wars: episode iv a new hope','jaws', 'memoirs of a geisha']
                       
def won_golden_globe(movie):
    if movie.lower() in won_golden_globe_movie_list:
        return True
    else: 
        return False
print(won_golden_globe('memoirs of a geisha'))


    

# 3: Wanneer genomineerde film een globe heeft gewonnen dan True: <film naam> , anders False: <film naam>

"""won_golden_globe2 = won_golden_globe_lower(['Star Wars: Episode IV A New Hope','Jaws'])
nominated_list = nominated_work_lower(['The Poseidon Adventure', 'Cinderella Liberty', 'Tom Sawyer', 'Earthquake', 'Jaws', 'Close Encounters of the Third Kind', 'Star Wars: Episode IV A New Hope'])

for x in nominated_list:
    if x in won_golden_globe2:
        print(True)
    else: 
        print(False)
"""        

# 4 remove toto albums
Toto_album = ['1986: Fahrenheit','1988: The Seventh One','1998: Toto XX (lead vocals on "Last Night" and “In A Word”)','2006: Falling in Between (co-lead vocals on "Bottom Of Your Soul")','2015: Toto XIV','2018: Old Is New']
Solo_albums_ruis = ['1986: Fahrenheit','1982: Joseph Williams (re-released 2002)','1996: I Am Alive','1997: 3','1999: Early Years','2006: Falling in Between (co-lead vocals on "Bottom Of Your Soul")','2003: Vertigo','2006: Two of Us','2006: Vertigo 2','2007: Smiles','2007: Tears','2008: This Fall','2021: Denizen Tenant[9]']
Solo_album_clean = ['1982: Joseph Williams (re-released 2002)','1996: I Am Alive','1997: 3','1999: Early Years','2003: Vertigo','2006: Two of Us','2006: Vertigo 2','2007: Smiles','2007: Tears','2008: This Fall','2021: Denizen Tenant[9]']

print(Toto_album)
print(Solo_albums_ruis)
print(Solo_album_clean)

#print(Solo_album_before.remove(Toto_album))
print(".......")

#per item checken
for album in Solo_albums_ruis:
    if album in Toto_album:
        Solo_albums_ruis.remove(album)
print(Solo_albums_ruis)

if Solo_albums_ruis == Solo_album_clean:
    print('check')
else: print('verbeteren')

Toto_album_s = ['1986: Fahrenheit','1988: The Seventh One','1998: Toto XX (lead vocals on "Last Night" and “In A Word”)','2006: Falling in Between (co-lead vocals on "Bottom Of Your Soul")','2015: Toto XIV','2018: Old Is New']
Solo_albums_ruis_s = ['1986: Fahrenheit','1982: Joseph Williams (re-released 2002)','1996: I Am Alive','1997: 3','1999: Early Years','2006: Falling in Between (co-lead vocals on "Bottom Of Your Soul")','2003: Vertigo','2006: Two of Us','2006: Vertigo 2','2007: Smiles','2007: Tears','2008: This Fall','2021: Denizen Tenant[9]']
Solo_album_clean_s = ['1982: Joseph Williams (re-released 2002)','1996: I Am Alive','1997: 3','1999: Early Years','2003: Vertigo','2006: Two of Us','2006: Vertigo 2','2007: Smiles','2007: Tears','2008: This Fall','2021: Denizen Tenant[9]']

print("..................")
print(Solo_albums_ruis_s)
def remove_toto_albums(albums):
    for titel in albums:
        if titel in Solo_albums_ruis_s:
            Solo_albums_ruis_s.remove(titel)
    return Solo_albums_ruis_s
remove_toto_albums(['1986: Fahrenheit','1988: The Seventh One','1998: Toto XX (lead vocals on "Last Night" and “In A Word”)','2006: Falling in Between (co-lead vocals on "Bottom Of Your Soul")','2015: Toto XIV','2018: Old Is New'])
print(Solo_albums_ruis_s)

if Solo_albums_ruis_s == Solo_album_clean_s:
    print('ready')
else:
    print('checken')


# wanneer in solo_album_before titels staan uit toto_album dan verwijderen. 
## a = solo_album_before
## a.pop() --> tussen haakjes is toto album lijst. 
## print resultaat



for i in range(10):
    print(i)

print(list(range(10)))

for i in reversed(range(900,1000,5)):
    print(i)
    
print('We have a long road ahead.')
for i in range(1000):
    print(i)
    if i == 10:
        break
    print('Almost there...')
print("That wasn't so bad after all.")


print('We have a long road ahead.')
for i in range(1000):
    if i % 2 == 0:
        print(i)
        continue
    print('Almost there...')
print("That wasn't half bad.")


print(iter('foobar'))

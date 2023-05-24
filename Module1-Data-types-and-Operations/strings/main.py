# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
goal_0= 32
goal_1= 54
player_goal0= 'Ruud Gullit'
player_goal1= 'Marco van Basten'

scorers = player_goal0 + " " + str(goal_0) +", "+ player_goal1 + " " + str(goal_1)
print(scorers)

report =f"{player_goal0} scored in the {goal_0}nd minute\n{player_goal1} scored in the {goal_1}th minute"
print(report)

player = 'Erwin Koeman'
first_name = player [player.find('E'):player.find(' ')]
last_name = player [player.find('K'):]
last_name_len = len(last_name) 
name_short = first_name[:1] +'. ' + last_name

print(first_name)
print(last_name)
print(name_short)

chant = (first_name + '! ')* (len(first_name)-1) +(first_name + '!')
print(chant)

# Volgens mij is dit een lelijke oplossing - is er een andere manier om een spatie na de laatste Erwin te verwijderen? 
good_chant=bool((first_name + '!=')* (len(first_name)-1) +(first_name + '!'))
print(good_chant)
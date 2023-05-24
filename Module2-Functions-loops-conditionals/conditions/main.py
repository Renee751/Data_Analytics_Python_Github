# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

# actions

#def farm_action(location_cows, weather, time_of_day, need_milking, tank_full, grass_long, season):
 #   if location_cows == 'pasture' and weather == 'rainy' and time_of_day == 'night':
  #      print("take cows to cowshed")
   # if need_milking == True and location_cows == 'cowshed':
    #    print('Milk cows')
    #if (tank_full == True) and (weather == (not ('sunny'or 'windy'))) and location_cows == 'pasture':
     #   print('Fertilize pasture')
    #if grass_long == True and season == 'spring' and weather == 'sunny':
     #   print('Mow grass')
    #else:
        #print('wait')

farm_action=('rainy', 'night', False, 'cowshed', 'winter', False, True)

def main():
    def farm_action(location_cows, weather, time_of_day, need_milking, tank_full, grass_long, season):
        if location_cows == 'pasture' and weather == 'rainy' and time_of_day == 'night':
            print("take cows to cowshed")
        if need_milking == True and location_cows == 'cowshed':
            print('Milk cows')
        if (tank_full == True) and (weather == (not ('sunny'or 'windy'))) and location_cows == 'pasture':
            print('Fertilize pasture')
        if grass_long == True and season == 'spring' and weather == 'sunny':
            print('Mow grass')
        else:
            print('wait')
        if __name__ == 'main':
            main()

 #if cows are on the pasture at night
 #if cows are standing in the rain
#def take_cows_to_cowshed (location_cows, weather, time_of_day):
 #   if location_cows == 'pasture' and weather == 'rainy' and time_of_day == 'night':
  #      return "take cows to cowshed"

# cows require  milking
# cows are in the cowshed 
# return "milk cows"

#def milk_cows(need_milking, location_cows):
 #   if need_milking == True and location_cows == 'cowshed':
  #      return 'Milk cows'

#slurry tan is full
#cows are in cowshed
# weather is nog sunny of windy
#return "fertilize pasture"

#def fertilize_pastures(tank_full,weather,location_cows):
 #   if (tank_full == True) and (weather == (not ('sunny'or 'windy'))) and location_cows == 'pasture':
  #      return 'Fertilize pasture'

# all is TRUE: grass is long / spring / sunny
# cows are not in the pasture
#return "mow grass"

# def mow_grass (grass_long, season, weather):
   # if grass_long == True and season == 'spring' and weather == 'sunny':
    #    return 'Mow grass'

# nothing else applies
# return "wait"

# else 'wait'
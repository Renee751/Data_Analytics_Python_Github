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

#farm_action=('rainy', 'night', False, 'cowshed', 'winter', False, True)

"""
def main():
    return farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)
    
def farm_action(weather, time_of_day, need_milking, location_cows, season , tank_full, grass_long):
        if (location_cows == 'pasture' and time_of_day == 'night') or (weather == 'rainy'):
            print("take cows to cowshed")
        if (need_milking == True) and (location_cows == 'cowshed'):
            print('Milk cows')
        if (tank_full == True) and (weather == ('rainy' or 'sunny')) and (location_cows == 'cowshed'):
            print('Fertilize pasture')
        if (grass_long == True) and (season == 'spring') and (weather == 'sunny'):
            print('Mow grass')
        else:
            print('wait')
        return
if __name__ == '__main__':
     main()
 #location_cows == 'pasture' and time_of_day == 'night') or (weather == 'rainy' and location_cows == 'pasture') or (location_cows == 'pasture' and need_milking == True):
    """
   
def main():
    return farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)

def farm_action(weather, time_of_day, need_milking, location_cows, season , tank_full, grass_long):
        if location_cows == 'pasture' and (time_of_day == 'night' or weather == 'rainy' or need_milking == True) and need_milking == True:
           return 'take cows to cowshed\nmilk cows\ntake cows back to pasture'
        if location_cows == 'pasture' and (time_of_day == 'night' or weather == 'rainy' or need_milking == True) and tank_full == True and (weather == 'rainy' or 'neutral'):
           return'take cows to cowshed\nfertilize pasture\ntake cows back to pasture' 
        if location_cows == 'pasture' and (time_of_day == 'night' or weather == 'rainy' or need_milking == True):
           return 'take cows to cowshed'           
        if need_milking == True and location_cows == 'cowshed':
            return'milk cows'
        if tank_full == True and (weather == 'rainy' or 'neutral') and location_cows == 'cowshed':
            return 'fertilize pasture'
        if grass_long == True and season == 'spring' and weather == 'sunny' and location_cows != 'pasture':
            return 'mow grass'  
        else: 
            return 'wait'
                
if __name__ == '__main__':
     print(main())

        
#print(farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True)) #fertilize pasture
#print(farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True)) #wait
#print(farm_action('windy', 'night', True, 'cowshed', 'winter', True, True)) # milk cows
#print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)) # take cows to cowshed + milk cows + take cows back to pasture


 
#def main():
 #   result = farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True)
  #  if result == 'wait':
   #     print('wait')
    #else:
#        print(result)
#
#def farm_action(weather, time_of_day, need_milking, location_cows, season, tank_full, grass_long):
 #   if (location_cows == 'pasture') and (weather == 'rainy') and (time_of_day == 'night'):
  #      return "Take cows to cowshed"
   # if (need_milking == True) and (location_cows == 'cowshed'):
    #    return 'Milk cows'
#    if (tank_full == True) and (weather != 'sunny' and weather != 'windy') and (location_cows == 'pasture'):
 #       return 'Fertilize pasture'
  #  if (grass_long == True) and (season == 'spring') and (weather == 'sunny'):
   #     return 'Mow grass'
    #else:
     #   return 'wait'

#if __name__ == '__main__':
 #   main()

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
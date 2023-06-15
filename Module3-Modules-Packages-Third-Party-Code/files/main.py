# Do not modify these lines
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Add your code after this line

import os

current_directory = (os.getcwd())
print(current_directory)

directory_list = os.listdir(current_directory)
print(directory_list)

def clean_cache():
    current_directory = (os.getcwd())
    cache_directory = os.path.join(current_directory, 'cache')
    list_cache_dir = os.listdir(cache_directory)
    
    if os.path.exists('cache') == True:
        for files in list_cache_dir:
            os.remove(os.path.join(cache_directory, files))
    else: 
        os.mkdir('cache')
    return
clean_cache()

directory_list = os.listdir(current_directory)
print(directory_list)


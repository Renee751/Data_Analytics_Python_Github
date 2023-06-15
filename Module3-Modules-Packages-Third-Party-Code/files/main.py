# Do not modify these lines
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Add your code after this line

import os
import zipfile

current_directory = (os.getcwd())
print(current_directory)

directory_list = os.listdir(current_directory)
print(directory_list)

print(os.path.exists('cache'))

def clean_cache():
    current_directory = os.getcwd()
    cache_directory = os.path.join(current_directory, 'cache')
    
    if os.path.exists('cache') == True:
        list_cache_dir = os.listdir(cache_directory)
        if list_cache_dir:
            for files in list_cache_dir:
                os.remove(os.path.join(cache_directory, files))
    else: 
        os.mkdir('cache')
    return


clean_cache()


directory_list = os.listdir(current_directory)
print(directory_list)

current_directory = (os.getcwd())
zip_file_path = os.path.join(current_directory, 'data.zip')
cache_dir_path = os.path.join(current_directory, 'cache')

with zipfile.ZipFile(zip_file_path,'r') as zip:
    zip.printdir()

print(cache_dir_path)

def cache_zip(zip_file_path, cache_dir_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip:
        zip.extractall(cache_dir_path)


def cached_files():
        list_absolute = []
        current_directory = os.getcwd()
        cache_directory = os.path.join(current_directory, 'cache')
        file_list = os.listdir(cache_directory)
        for file in file_list:
            abs_file = os.path.join(cache_directory, f'{file}')
            list_absolute.append(abs_file)
        return list_absolute

def find_password(list_absolute):
    text = 'password'
    password =[]
    for files in list_absolute:
        with open(files, 'r') as checking_file:
            lines = checking_file.readlines()
            for line in lines:
                if text in line:
                    password_line = line.strip()
                    password = (password_line[password_line.find(' ')+1:])
                    break
    return password

list_absolute = cached_files()
password = find_password(list_absolute)
print(find_password(list_absolute))
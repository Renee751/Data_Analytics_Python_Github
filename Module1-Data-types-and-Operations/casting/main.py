# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
leek_price =2
string = f'Leek is {leek_price} euro per kilo.'
print(string)

order = 'leek 8'
aantal_str =order.find('8')
print(order[aantal_str:])
aantal_int = int(order[aantal_str:])
sum_total = leek_price * aantal_int

broccoli_price = 2.34
broccoli_count = 1.6
total_price = round(broccoli_price*broccoli_count,2)
string_broccoli = f'{broccoli_count}kg broccoli costs {total_price}e'
print(string_broccoli)


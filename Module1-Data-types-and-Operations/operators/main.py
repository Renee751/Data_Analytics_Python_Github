# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
spain_language = "Castilian Spanish"
switzerland_language ="German"
print(spain_language == switzerland_language)

spain_religion = "Roman Catholic"
switzerland_religion= "Roman Catholic"
print(spain_religion == switzerland_religion)
#print(spain_religion is switzerland_religion)

spain_capital= len("madrid")
switzerland_capital= len("bern")
print(spain_capital != switzerland_capital)

spain_gdp= 1798000000000
switzerland_gdp=618228000000
print(switzerland_gdp > spain_gdp)

spain_growth= 0.12/100
switzerland_growth= 0.64/100
print((spain_growth and switzerland_growth)<(1/100))

spain_population=47222613
switzerland_population=8563760
pop_spain_10 = bool(spain_population >10000000)
pop_swizz_10 = bool(switzerland_population >10000000)

print((pop_spain_10 or pop_swizz_10) == True)


print(pop_swizz_10 != pop_spain_10)

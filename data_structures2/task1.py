
countries = {'Afghanistan': 'Kabul',
'Albania': 'Tirana',
'Algeria': 'Algiers',
'Andorra': 'Andorra la Vella',
'Angola': 'Luanda',
'Antigua and Barbuda': 'Saint John',
'Austria': 'Vienna',
'Azerbaijan': 'Baku',
'Bahamas': 'Nassau',
'Bahrain': 'Manama',
'Bangladesh': 'Dhaka',
'Barbados': 'Bridgetown',
'Belarus': 'Minsk',
'Belgium': 'Brussels',
'Belize': 'Belmopan',
'Benin': 'Porto-Novo',
'Bhutan': 'Thimphu',
'Bolivia': 'Sucre (de jure),',
'Bosnia and Herzegovina': 'Sarajevo',
'Botswana': 'Gaborone',
'Brazil': 'Brasilia'}

while True:
    
    input_country = input("Please enter a country name, or enter q to quit: ")
    
    if input_country == "q":
        break 
    if input_country in countries:
        print("Capital: ", countries[input_country])
    else:
        print("Country not found.")
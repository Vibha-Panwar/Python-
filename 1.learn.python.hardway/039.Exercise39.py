states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonvilla'
}
# Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-'*8)
print("NY State has:",cities['NY'])
# printout some State

print('-'*8)
print("Michigan's abbrevation is:",states['Michigan'])
print("Florida's abbrevation is:",states['Florida'])

# do it by using the state then cities dict
print('-'*8)
print("Michigan has:",cities[states['Michigan']])
print("Florida has:",cities[states['Florida']])

# print every state abbrevation
print('-'*8)
for state,abbrev in list(states.items()):
    print(f"{state} is abbrevated {abbrev}")

# print every city in state
print('-'*8)
for abbrev,city in list(cities.items()):
    print(f"{abbrev} has city {city}")

# now do both at the same time
print('-'*8)
for state,abbrev in list(states.items()):
    print(f"{state} state is abbrevated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-'*8)
# safely get a abbrevtiion by state that might not be there.
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value.
city = cities.get('TX','Does not exist')
print(f"The city for state 'TX' is : {city}")
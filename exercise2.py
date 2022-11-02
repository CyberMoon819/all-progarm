month = {
    'jan' : 2200,
    'feb' : 2350,
    'mar' : 2600,
    'apr' : 2130,
    'may' : 2190
}

print(month['feb'] -month['jan'])
print(month['jan']+month['feb']+month['mar'])
print(2000 in month)
month['jun'] = 1998
print(month)
month['apr'] = 1930
print(month)

heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
print(len(heros))
heros.append('black panther')
print(heros)
heros.remove('black panther')
heros.insert(3, 'black panther')
print(heros)
bri = set(['Бразилия', 'Россия', 'Индия'])
print('Индия' in bri)
True
print('США' in bri)
False
bric = bri.copy()
bric.add('Китай')
bric.issuperset(bri)
bri.remove('Россия')
print(bri & bric) # OR bri.intersection(bric)
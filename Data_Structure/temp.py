dict_1 = {
    'Name' : 'Kaustubh Sawant',
    'Subject' : 'Python Advanced'
}
dict_1['Name']  = 'Alisha'
y = {**dict_1,**{'cool':False}}
print(f'{dict_1.keys()} \n {dict_1.values()} \n {dict_1.items()} {dict_1.get('ages', 0 ) } {y}')

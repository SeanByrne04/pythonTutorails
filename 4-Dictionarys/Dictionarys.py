#can't join dictionarys

super_villains = {'Fiddler' : 'Isaac Bowin',
                  'Mirror master' : 'Sam Scudder',
                  'Pied Piper' : 'Thomas Peterson'} #defines the dictionary
                

print(super_villains['Fiddler'])#prints the text in corelation with the text in brackets

del super_villains['Pied Piper'] #delets certain sections
super_villains['Fiddler'] = 'Hartley Rathaway'#adds a string

print(len(super_villains))#prints the lengt of the dictionary

print(super_villains.get('Pied Piper'))

print(super_villains.keys())

print(super_villains.values())

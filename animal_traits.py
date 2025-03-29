animal_facts={
    'dog': {'type' : 'mammal','domesticated': True},
    'cat': {'type' : 'mammal','domesticated': True},
    'parrot':{'type' : 'bird','can_talk': True},
    'snake':{'type':'reptile'}
}
def is_warm_blooded(animal):
    return animal_facts.get(animal, {}).get('type') in ['mammal','bird']
def is_pet(animal):
   facts = animal_facts.get(animal,{})
   return facts.get('domesticated',False) if facts.get('type') == 'mammal' else facts.get('can_talk',False)

print(is_warm_blooded('dog'))

print(is_warm_blooded('snake'))
print(is_pet('CAT'))
print(is_pet('snake'))
print(is_pet('parrot'))

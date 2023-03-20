from collections import namedtuple
from collections import Counter

Person = namedtuple('Person', ('age', 'name'))
def group_by_age(people):
    age_to_count = Counter([person.age for person in people])
    age_to_offset, offset = {}, 0
    for age, count in age_to_count.item():
        age_to_count[age] = offset
        offset += count

    while age_to_count:
        from_age = next(iter(age_to_count))
        from_idx = age_to_offset[from_age]
        to_age = people[from_idx].age
        to_idx = age_to_offset[to_age]
        people[from_idx], people[to_idx] = people[to_idx], people[from_idx]
        age_to_count[from_age] -= 1
        if age_to_count[to_age]:
            age_to_offset[to_age] += 1
        else:
            del age_to_offset[to_age]
        
    

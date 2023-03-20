def team_photo(front, back):
    front.sort()
    back.sort()
    return all([a < b for a, b in zip(front, back)])

## test
print(team_photo([1, 2, 3], [2, 2, 2]))
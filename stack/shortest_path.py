def shortest_path(path):
    files = path.split('/')
    if path[0]=='/': l = ['/'] ## path is absolute path.
    else: l = []
    for file in files:
        if not file or file=='.': continue
        elif file=='..':
            if not l or l[-1]=='..': l.append(file)
            elif l[-1]=='/': raise ValueError
            else:
                l.pop()
        else:
            l.append(file+'/')
    return ''.join(l)

## test
print(shortest_path("scripts//./../scripts/awkscripts/././"))
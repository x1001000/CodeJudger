with open(input()) as f:
    old = input()
    new = input()
    outlines = []
    print('=== Before the replacement')
    for readline in f.readlines():
        print(readline.strip())
        outlines.append(readline.replace(old, new))
    print('=== After the replacement')
    for outline in outlines:
        print(outline.strip())
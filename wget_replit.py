import os
for x00 in range(100, 601, 100):
    for xxx in range(x00+2, x00+11, 2):
        os.system(f'wget https://replit.com/@x1001000/{xxx}.zip')
        os.system(f'unzip {xxx}.zip')
        os.system(f'mv main.py {xxx}.py')

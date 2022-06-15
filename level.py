def clear(max):
    leve = "p"
    for i in range(max): 
        leve += "."
    level = open("level.g", 'w')
    level.write(leve)
    level.close()
def ran(max,x):
    import random
    leve = "p"
    for i in range(max): 
        r = random.randrange(0,100)
        if r > x:
            leve += "."
        else:
            leve += "*"
    level = open("level.g", 'w')
    level.write(leve)
    level.close()
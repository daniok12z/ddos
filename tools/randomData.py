import random


# Searchs for a random IP
def random_IP():
    ip = []
    for _ in range(4):
        ip.append(str(random.randint(1, 255)))
    return ".".join(ip)


# Searchs for a random referer
def random_referer():
    with open("tools/L7/referers.txt", "r") as referers:
        referers = referers.readlines()
    return random.choice(referers)

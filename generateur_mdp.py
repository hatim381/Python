import random

longpass = int(input('donner la longueur du mdp : '))

s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
password = "".join(random.sample(s, longpass))
print(password)

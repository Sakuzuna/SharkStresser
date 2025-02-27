import random

def random_boolean():
    return random.random() < 0.5

def random_string(length):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    return "".join(random.choice(chars) for _ in range(length))

def random_integer(min_val, max_val):
    return random.randint(min_val, max_val)

def random_item(array):
    return random.choice(array)

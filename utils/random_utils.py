import random
import string

def random_string(length):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

def random_integer(min_val, max_val):
    return random.randint(min_val, max_val)

def random_item(items):
    return random.choice(items)

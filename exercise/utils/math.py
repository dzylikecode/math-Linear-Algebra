from IPython.display import display, Math

def mprint(str):
    display(Math(str))

def minform(name):
    prefix = "*"*10
    suffix = prefix
    mprint(prefix + name + suffix)
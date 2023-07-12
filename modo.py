DEBUG = False

def cambiar_modo():
    global DEBUG
    DEBUG = not DEBUG
    return DEBUG

def get_mode():
    return DEBUG


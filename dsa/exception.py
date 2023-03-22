# raise ZeroDivisionError("Number over Zero!")

class error(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)
    
raise error("errorrrr")
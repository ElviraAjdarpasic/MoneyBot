import logging

#Skapar och retunerar logger 
def setup_logger(name: str):
    logger = logging.getLogger(name)

    #Om logger redan finns så används den
    if logger.handlers:
        return logger 

    #Sätter loggnivån till INFO (Skriver info)
    logger.setLevel(logging.INFO)

    #Bestämmer VAR meddellandet ska visas
    handler = logging.StreamHandler()
    #Bestämmer HUR medleandet ska se ut
    formatter = logging.Formatter(" " * 18 +"[%(name)s] %(levelname)s: %(message)s")
        
    handler.setFormatter(formatter)

    logger.addHandler(handler)
        
    return logger
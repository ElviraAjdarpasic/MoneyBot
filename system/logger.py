import logging

#Skapar och retunerar logger 
def setup_logger(name: str):
    logger = logging.getLogger(name)

    #Om logger redan finns så används den
    if logger.handlers:
        return logger 

    #Sätter loggnivån till INFO (Skriver info)
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler(f"{name}.log")
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter("[%(name)s] %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    
    return logger
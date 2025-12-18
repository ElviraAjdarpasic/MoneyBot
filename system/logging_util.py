import logging

#Skapar och retunerar logger 
def setup_logger(name: str):
    logger = logging.getLogger(name)

    #Om logger redan finns så används den
    if logger.handlers:
        return logger 

        logger.setLevel(logging.INFO)

        handler = logging.StreamHnadler()
        formatter = logging.Formatter("[%(name)s] %(levelname)s: %(message)s")
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        return logger
import logging

def setup():
    logging.basicConfig(filename='./client.log',
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
def log_info(message):
    setup()
    logging.info(f"[CLIENT INFO]: {message}")

def log_error(message):
    setup()
    logging.error(f"[CLIENT ERROR]: {message}")

def log_warning(message):
    setup()
    logging.warning(f"[CLIENT WARNING]: {message}")

def log_debug(message):
    setup()
    logging.debug(f"[CLIENT DEBUG]: {message}")

def log_critical(message):
    setup()
    logging.critical(f"[CLIENT CRITICAL]: {message}")

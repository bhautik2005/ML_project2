import logging
import os
from datetime import datetime


LOG_FILE  = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
 
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(os.path.dirname(log_path), exist_ok=True)

# `log_path` already contains the directory + filename, so use it directly.
LOG_FILE_PATH = log_path

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[%(asctime)s] %(lineno)d %(name)s %(levelname)s - %(message)s')


if __name__ == "__main__":
    logging.info("Logger has been configured.")
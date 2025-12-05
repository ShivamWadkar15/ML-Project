import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Directory for logs
LOG_DIR = os.path.join(os.getcwd(), "logs")

# Create logs directory if not exists
os.makedirs(LOG_DIR, exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    level=logging.INFO
)



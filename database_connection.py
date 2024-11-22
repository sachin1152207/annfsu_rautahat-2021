import mysql.connector
from customLogger.logger import CustomLogger
import json

# Load database configuration from config.json
DB_CONFIG = json.load(open('config.json', 'r'))["DatabaseConfig"]

# Logging Config
logger = CustomLogger.get_logger()

def connection():
    try:
        # Establish the connection
        conn = mysql.connector.connect(
            host=DB_CONFIG["HOST"],
            user=DB_CONFIG["USER"],
            password=DB_CONFIG["PASSWORD"],
            database=DB_CONFIG["DATABASE"]
        )
        if conn.is_connected():
            logger.info(f"Connected to: {conn.server_host}")
            return conn
        else:
            logger.error("Connection failed")
    except mysql.connector.Error as err:
        logger.error(f"Error:  {err}")
    
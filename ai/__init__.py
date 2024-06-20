from loguru import logger
import sys
from dotenv.main import load_dotenv, find_dotenv

logger.info("hello stock ai agent.")
_ = load_dotenv(find_dotenv())

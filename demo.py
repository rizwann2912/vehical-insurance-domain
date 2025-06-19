from src.logger import logging
from src.exception import MyException
import sys

try:
    a = 1+'4'
except Exception as e:
    logging.error(e)
    raise MyException(e,sys) from e
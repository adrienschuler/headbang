from logging.config import dictConfig
import logging
from .core.logger import LogConfig

dictConfig(LogConfig().dict())

logger = logging.getLogger("headbang")

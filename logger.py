from loguru import logger


logger.add("marithmetic.log", rotation="10 MB", format="{time:YYYY-MM-DD HH:mm:ss} {message}")


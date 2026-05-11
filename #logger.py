#logger.py

import logging

def configurar_logger():
    logging.basicConfig(
        filename='logs.txt',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        encoding='utf-8'
    )
    return logging.getLogger(__name__)

logger = configurar_logger()
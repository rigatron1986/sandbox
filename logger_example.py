import logging

test = True

if test:
    level = logging.INFO
else:
    level = logging.WARNING

logging.basicConfig(level=level)
logger = logging.getLogger(__name__)
logger.error("this comes if there is an error")
logger.debug("this is a debug")
logger.info("this is a info")
logger.warning("this is a warning")


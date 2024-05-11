import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="p8logfile.log",
                    filemode="w",
                    format="we have logging message: %(asctime)s%(levelname)s:%(message)s")
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error('error')
logging.critical("critical")


try:
    print(10/0)
except Exception:
    logging.exception("Exception")


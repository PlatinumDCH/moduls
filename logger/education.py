import logging

# logging.warning('Warning logging')
# logging.info('info logging')



# CRITICAL ххх 50
# ERROR  ххх 40
# WARNING - с этого уровня и выше будет логирование в консль 30
# INFO 20
# DEBUG 10

logger = logging.getLogger(__name__)

logging.basicConfig(
    filename='exemple.log', 
    encoding='utf-8', 
    level=logging.DEBUG
    )

logger.debug('This is message shoul by go to the loo file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')
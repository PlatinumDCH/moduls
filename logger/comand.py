import argparse
import logging


parser = argparse.ArgumentParser(
    description='My python application'
)
parser.add_argument(
    '--log', 
    dest='loglevel', 
    default='INFO',
    help='Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL')

args = parser.parse_args()

numeric_level = getattr(logging, args.loglevel.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % args.loglevel)

# Настраиваем логгер
logging.basicConfig(
    filename='example_2.log',#файл в который будет созраняться логи
    encoding='utf-8',#формать кодировки
    level=numeric_level,#епередаваемый уровень логирования
    filemode='w',#перезапись файла
    format='%(asctime)s:%(levelname)s---%(message)s',#формат лога
    datefmt='%m/%d/%Y %I:%M:%S',#можно указывать формат времени
)

# Используем логгер
logger = logging.getLogger(__name__)
logger.info(args)
logger.info(numeric_level)
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
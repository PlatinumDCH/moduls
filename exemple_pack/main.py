from joke import get_rundom_joke
from logger.set_logger import obj_logger

obj_logger.debug('start funcion')
def main():

    while True:
        user_response = input('Go program?y/n: ').lower()
        if user_response == 'y':
            print(get_rundom_joke())
            continue
        obj_logger.debug('end function')
        break

if __name__ == '__main__':
    main()
    
        
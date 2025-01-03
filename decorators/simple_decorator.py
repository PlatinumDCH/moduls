import functools

def decorator(orig_func):
    @functools.wraps(orig_func)
    def wrapper(*args,**kwargs):
        #do_something before orig_func
        result = orig_func(*args,**kwargs)
        #do_something after orig_func
        return result
    return wrapper

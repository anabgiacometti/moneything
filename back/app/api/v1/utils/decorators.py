from functools import wraps


def login_required(f):
    @wraps(f)
    async def wrapper(*args, **kwargs):
        print("login required is working")
        return await f(*args, **kwargs)

    return wrapper

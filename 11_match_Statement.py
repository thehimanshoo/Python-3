'''                                                         Match Statement
                                                           -----------------
    A `match` statement checks a value against several patterns, similar to a `switch` statement in other languages like C or Java. 
    However, it's more advanced, as it can also pull out parts of the value into variables. Only the first matching pattern is used.
'''
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403:
            return "Not allowed"
        case 404:
            return "Not found"
        case 418:
            return "I'am a teapot"
        case _:
            return "Something's wrong with the internet"
        
print(http_error(418))


# Next Example

def check_point(point):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")

print(check_point((4,8)))
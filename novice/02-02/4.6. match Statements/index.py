def http_status(status):
    match status:
        case 400:
            return "bad riques"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

print(http_status(400))
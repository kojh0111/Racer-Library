import re


def letter_error(password):
    return re.search(r"[a-zA-Z]", password)


def symbol_error(password):
    return re.search(r"[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]", password)


def digit_error(password):
    return re.search(r"\d", password)


def passwordCheck(password):
    if (
        len(password) >= 8
        and letter_error(password)
        and symbol_error(password)
        and digit_error(password)
    ):
        return True
    elif len(password) >= 10 and (
        (letter_error(password) and (symbol_error(password) or digit_error(password)))
        or (
            (letter_error(password) or symbol_error(password)) and digit_error(password)
        )
        or (
            (letter_error(password) or digit_error(password)) and symbol_error(password)
        )
    ):
        return True
    else:
        return False


emailRegex = re.compile(
    r"""(([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+)(\.[a-zA-Z]{2,4}))""", re.VERBOSE
)


def emailCheck(email):
    emailbool = bool(re.fullmatch(emailRegex, email))
    return emailbool


def usernameCheck(username):
    ubool = bool(re.fullmatch(r"([a-zA-Z가-힣]+)", username))
    return ubool

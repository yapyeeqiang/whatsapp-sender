import re

def is_phone_valid(phone_number):
    MALAYSIA_PHONE_NUMBER_REGEX = '^(\+?6?01)[02-46-9]-*[0-9]{7}$|^(\+?6?01)[1]-*[0-9]{8}$'

    isValid = bool(re.search(MALAYSIA_PHONE_NUMBER_REGEX, phone_number))

    return isValid
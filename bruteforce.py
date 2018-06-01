
def bruteforce(start: str=None, min_len: int=1, max_len: int=15, digits: bool=False, lower: bool=False, upper: bool=False, custom_alphabet: str=None):
    alphabet = ''
    if custom_alphabet:
        alphabet = custom_alphabet
    else:
        if digits:
            alphabet += '0123456789'
        if lower:
            alphabet += 'abcdefghijklmnopqrstuvwxyz'
        if upper:
            alphabet += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    if not alphabet:
        raise RuntimeError('Please set alphabet')
    elif not isinstance(alphabet, str):
        raise RuntimeError('Incorrect alphabet type. Must be string')


    if start is not None:
        if not isinstance(start, str):
            raise RuntimeError('Incorrect start type')
        current_password = [alphabet.index(char) for char in start]
    else:
        current_password = [-1] * min_len

    last_char = len(alphabet) - 1

    while len(current_password) < max_len + 1:
        for i, char in enumerate(alphabet):
            if current_password[-1] > i:
                continue
            current_password[-1] = i
            yield ''.join((alphabet[index] for index in current_password))
        password_len = len(current_password)
        for i in range(password_len - 1, -1, -1):
            if current_password[i] == last_char:
                current_password[i] = 0
                if i - 1 == -1:
                    current_password = [0] + current_password
                    break
                elif current_password[i - 1] != last_char:
                    current_password[i - 1] += 1
                    break
            else:
                current_password[i] += 1
                break


import bcrypt


def my_salt():
    return ('$2b$12$tUimG74HOCBiAA7sm3QX9e').encode('utf-8')

if __name__ == '__main__':
    input_password = 'abcdefg1234'

    bytePwd = input_password.encode('utf-8')
    hash = bcrypt.hashpw(bytePwd, my_salt())
    new_password = hash.decode('utf-8')
    print(new_password)

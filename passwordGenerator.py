import sys
import random


def generatePassword(length):
    return "".join(random.sample(
        "abcdefghijklmnipqrstuvwxyz" + "ABCDEFGHIJKLMNOPRSTUVWXYZ" + "01234567890" + "!§$%&/()=?[]{},.-_",
         length))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        length = int(sys.argv[1])
        if length > 80:
            length = 80
            print('\nNote: Max allowed length is %s characters!' % length)
    else:
        length = 36

    print('\nPassword length in each line: %s\n' % length)
    for i in range(0, 10):
        print(generatePassword(length))

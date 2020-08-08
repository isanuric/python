import random

print("".join(random.sample(
    "abcdefghijklmnipqrstuvwxyz" + "ABCDEFGHIJKLMNOPRSTUVWXYZ" + "01234567890" + "!§$%&/()=?[]{},.-_",
     36)))
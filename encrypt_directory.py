import os
import glob
import gnupg
import sys
from threading import local
from os.path import splitext

status = ""
gpg_extention = '.gpg'
recipients = ['<your-mail>@gmx.de']

if sys.argv[1] == '.':
    path = os.getcwd()
else:
    path = sys.argv[1]    

gpg = gnupg.GPG()


def encrypt(recipients):
    for root, dirs, files in os.walk(path):
        for file in files:
            current_file = os.path.join(root, file)
            with open(current_file, 'rb') as cur_file:
                if (not current_file.endswith(gpg_extention)):
                    
                    status = gpg.encrypt_file(
                        cur_file,
                        recipients = recipients,
                        sign = True,
                        output = current_file + gpg_extention)

                    if len(sys.argv) == 3 and sys.argv[2] == '-d':
                        deleteOriginalFile(status, file, current_file)   
    os.system('tree')

def deleteOriginalFile(status, file, current_file):
    if status.ok == True and status.status == 'encryption ok':
        print('Encryption done. Deleting unencrypted file:', file)
        os.remove(current_file)
    else:
        print ('stderr: ', status.stderr)    

def help():
    print('usage: python3 encrypt_directory.py <path> [-d]\n')
    print('   -d  delete original file after successful encryption.\n')   


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == '--help':
        help()
    else:
        encrypt() 
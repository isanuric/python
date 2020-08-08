import os
import glob
import gnupg
import sys
from threading import local
from os.path import splitext
import configparser


config = configparser.RawConfigParser()
config.read(os.path.dirname(os.path.abspath(__file__))+ '/properties.conf')
my_repcipient = config.get('gpg', 'gpg.recipient')
recipient = [my_repcipient] # Set your git email here

status = ""
gpg_extention = '.gpg'

def encrypt():
    gpg = gnupg.GPG()
    for root, dirs, files in os.walk(getPath()):
        for file in files:
            current_file = os.path.join(root, file)
            with open(current_file, 'rb') as cur_file:
                if (not current_file.endswith(gpg_extention)):
                    
                    status = gpg.encrypt_file(
                        cur_file,
                        recipients = recipient,
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

def getPath():
    if sys.argv[1] == '.':
        path = os.getcwd()
    else:
        path = sys.argv[1]    
    return path

def help():
    print('usage: python3 encrypt_directory.py [<path> [-d]] [--help]\n')
    print('   -d  delete original file after successful encryption.\n')   



if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == '--help':
        help()
    else:
        encrypt() 

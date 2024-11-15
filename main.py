import sys

import decrypt
import encrypt
import generate

args = sys.argv

print("\n   __                                             \
       \n  / /____ __ _  ___  __ _________ ___ _____  ____ \
       \n / __/ -_)  ' \/ _ \/ // / __/ _ `/\ \ / _ \/ __/   {VERSION 1.0} \
       \n \__/\__/_/_/_/ .__/\_,_/_/  \_,_//_\_\\\___/_/    \
       \n             /_/                                  \
       \n \
       \n")

assert len(args) > 1, "Bad syntax, check main.py -h for help."
assert args[1].startswith("-"), "Bad syntax, check main.py -h for help."

if args[1] == "-h" and len(args) == 2:
    print(" => Basic options : \
         \nEncrypt : -e <file_to_encrypt> -k <keyfile> \
         \nDecrypt : -d <file_to_decrypt> -k <keyfile> \
         \nGenerate random key : -g \
         \nTransfer ouput in a file : -o <output_file> (optional)\
         \n \
         \n => Some examples : \
         \npython main.py -g -o mykey.txt : generates a key en write it in mykey.txt \
         \npython main.py -e somefile.txt -k mykey.txt : print the encrypted content of somefile.txt \
         \npython main.py -d encrypted_file.txt -k mykey.txt -o decrypted_file.txt : decrypt encryted_file.txt and write the result in decrypted_file.txt")


elif args[1] == "-d":
    assert len(args) > 2, "No file specified."
    assert len(args) > 3, "No key specified."
    assert args[3] == "-k", "Bad syntax, check main.py -h for help."
    assert len(args) > 4, "No key specified."
    try:
        f = open(args[2], "r")
        file = f.read()
    except:
        assert False, "Can't open specified file."
    try:
        f = open(args[4], "r")
        key = f.read()
        assert len(key) == 24, "Bad key size ! Key must be 128bits long !"
    except:
        assert False, "Can't open specified key."
    if len(args) > 5:
        assert args[5] == "-o", "No such options, check main.py -h for help."
        assert len(args) > 5, "No output file specified."
        try:
            f = open(args[6], "wb")
            f.write(decrypt.decrypt_data(file, key))
            f.close()
            print("Success !")
        except:
            assert False, "Couldn't create file " + args[6] + "."
    else:
        print(decrypt.decrypt_data(file, key))


elif args[1] == "-e":
    assert len(args) > 2, "No file specified."
    assert len(args) > 3, "No key specified."
    assert args[3] == "-k", "Bad syntax, check main.py -h for help."
    assert len(args) > 4, "No key specified."
    try:
        f = open(args[2], "rb")
        file = f.read()
        #print(file)
    except:
        assert False, "Can't open specified file."
    try:
        f = open(args[4], "r")
        key = f.read()
        assert len(key) == 24, "Bad key size ! Key must be 128bits long !"
    except:
        assert False, "Can't open specified key."
    if len(args) > 5:
        assert args[5] == "-o", "No such options, check main.py -h for help."
        assert len(args) > 5, "No output file specified."
        try:
            f = open(args[6], "w")
            f.write(encrypt.encrypt_data(file, key))
            f.close()
            print("Success !")
        except:
            assert False, "Couldn't create file " + args[6] + "."
    else:
        print(encrypt.encrypt_data(file, key))


elif args[1] == "-g":
    if len(args) > 2:
        assert args[2] == "-o", "-g doesn't accept any additionnal argument except -o."
        assert len(args) > 3, "No output file specified."
        try:
            f = open(args[3], "w")
            f.write(generate.generate_key())
            f.close()
            print("Success !")
        except:
            assert False, "Couldn't create file " + args[3] + "."
        
    else:
        print(generate.generate_key())


else:
    assert False, "No such options, check main.py -h for help."

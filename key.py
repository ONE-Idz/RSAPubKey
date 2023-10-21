from licensing.models import *
from licensing.methods import Key, Helpers


RSAPubKey = "<RSAKeyValue><Modulus>2EccSgxEF6LGppC/BaWMH+1LGj0dK1ED7VyMUV6exlIPFJRnhNzrUzdFsAi3uCDQjep+dou/jMvjFYNv3RERmGmEbVObPGp4vaRTSCSrV52yvw3vhwfZbfBih80Nvg7AZJXkYhIDJ36fIJ893RiKSPKbR0dJZKqO8HCsZt+VHQBtD855hOVblo/wr2YX2ZdFr8kciNs9jpvUNpnXCk/aZxGHJvt+gd0wJTITR4/ygXA4zXR5xYwthZzaXPHG9YF0YQ0q2x67EvkgStzuJvB+lMhCufytl+5wZS0kCywgsKnx7ZgtysSxz79iPuBS4Nu5lCsKjJ09vE8wx8nFMoOx4w==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
auth = "WyI2NDYyNzU3MyIsIlhKTDZ6U2pJVHo1ZUtuVVR4MHB2YTkxcE1jUFVTbkFyOVNKWll2emQiXQ=="
def Authkey():
         try:
             print('')
             print('Masukan Key Kamu Di Sini')
             key = str(input(f'*--> : '))
             result = Key.activate(token=auth,\
             rsa_pub_key=RSAPubKey,\
             product_id=22355, \
             key=key,\
             machine_code=Helpers.GetMachineCode(v=2))
             if result[0] == None or not Helpers.IsOnRightMachine(result[0], v=2):
    # an error occurred or the key is invalid or it cannot be activated
    # (eg. the limit of activated devices was achieved)
                  print("Key Kamu invlid..!".format(result[1]))
             else:
    # everything went fine if we are here!S
                  print("Key kamu valid..!")
         except:pass

if __name__=='__main__':
      Authkey()
import sys 
#getting the user to decide whether they want to encrypt or decrypt 
decide = int(input("Do you want to encrpyt the text(1) or decrypt the text(2)?")) 
if decide != 1 and decide !=2: 
  print("Your decision was invalid") 
  sys.exit() 
#getting the entry and changing it into a usable format 
entry= input("What piece of text would you like to encode?") 
entry = entry.lower() 
entry = entry.replace(" ","") 
#the length of the message without spaces 
length = len(entry) 
#empty list that will eventually have all the key inputs 
keyorder = [] 
#creating a list that has the position of each letter in the key in order 
def getkeylist (vigenerekey): 
  key = "" 
  for x in range (length): 
    if vigenerekey[x % len(vigenerekey)] in "1234567890": 
      print("you can't have numbers in your key") 
      sys.exit() 
    elif vigenerekey[x % len(vigenerekey)] not in "abcdefghijklmnopqrstuvwxyz":
      print("you can't have special characters in your key") 
      sys.exit() 
    else: 
      key = key + vigenerekey[x % len(vigenerekey)] 
      keyorder.append(((ord(key[x]) - 19) % 26)) 
  return keyorder 


#getting the key list
keyorder = getkeylist(input("What key do you want to have?").replace(" ","")) 


#changing the message by shifting the letters forward the amount of times the key says 
def encrypt(): 
  output = entry 
  for x in range (length): 
    output = (output[1 :length] + chr((((ord(entry[x]) + keyorder[x]) - 19) % 26) + 97)) 
  return output 

#changing the message by shifting the letters backward the amount of times the key says 
def decrypt(): 
  output = entry 
  for x in range (length): 
    output = (output[1 :length] + chr((((ord(entry[x]) - keyorder[x]) - 19) % 26) + 97)) 
  return output 


#output 
if decide == 1: 
  print(encrypt()) 
else: 
  print(decrypt()) 

#show the key list 
show = int(input("Do you want to see the key list? yes(1) no(2)"))
if show == 1: 
  print(keyorder) 
else: 
  print("")

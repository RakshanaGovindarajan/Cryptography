#  File: TestCipher.py

#  Description: Creating encoding and decoding algorithms for substitution and vigenere ciphers

#  Student Name: Rakshana Govindarajan

#  Student UT EID: rg38236

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: 27 March 2016

#  Date Last Modified: 30 March 2016


# Encoding text based on the substitution cipher
def substitution_encode ( strng ):

  # Saving the letters of the alphabet in a list of characters
  alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

  # Saving the cipher letters in a list of characters
  cipher = ["q", "a", "z", "w", "s", "x", "e", "d", "c", "r", "f", "v", "t", "g", "b", "y", "h", "n", "u", "j", "m", "i", "k", "o", "l", "p"]

  # Creating a list to store the result
  final = []

  # Going through the string
  for i in range(len(strng)):

    # If the character is not alphabetic, appending it to the list
    if(strng[i].isalpha() == False):
      final.append(strng[i])

    else:
      # Base index is the index of the letter "a"
      idx_base = alphabet.index("a")

      # Case index is the index of the letter in the iteration
      idx_case = alphabet.index((strng[i]).lower())

      # Finding the location
      idx = idx_case - idx_base

      # Using the location to find the cipher letter for encoding from the cipher array
      cipher_letter = cipher[idx]
      final.append(cipher_letter)

  # Making the result a string for ease of output
  result = ""
  for item in final:
    result += item

  return(result)

# Decoding text using the substitution cipher
def substitution_decode ( strng ):

  # Saving the letters of the alphabet in a list of characters
  alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

  # Saving the cipher letters in a list of characters
  cipher = ["q", "a", "z", "w", "s", "x", "e", "d", "c", "r", "f", "v", "t", "g", "b", "y", "h", "n", "u", "j", "m", "i", "k", "o", "l", "p"]

  final = []

  # Going through the string
  for i in range(len(strng)):

    # If the character is not alphabetic, then appending it to the list
    if(strng[i].isalpha() == False):
      final.append(strng[i])

    else:
      # Base index is the index of the letter "a"
      idx_base = alphabet.index("a")

      # Case index is the index of the letter in the iteration
      idx_case = cipher.index((strng[i]).lower())

      # Finding the location
      idx = idx_case - idx_base

      # Using the location to find the cipher letter for encoding from the cipher array
      cipher_letter = alphabet[idx]
      final.append(cipher_letter)

  result = ""
  for item in final:
    result += item

  return(result)
   

# Encoding text based on the vigenere cipher
def vigenere_encode ( strng, passwd ):

  # Saving the letters of the alphabet in a list of characters
  alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  
  final = []
  counter = 0
  alert = 0
  for i in range(len(strng)):

    # If the character is not alphabetic, then appending it to the list
    if(strng[i].isalpha() == False):
      final.append(strng[i])
      # Adding to the alert variable to keep track that non-alphabetic characters have come up in the string traversal
      alert += 1
      

    
    if(strng[i].isalpha() == True):
    
      # If the string is longer than the pass phrase given
      if(i > len(passwd) - 1):
        
        # If the counter variable is greater than pass phrase length and non-alphabetic character(s) have already come up in the string
        if((counter > len(passwd) - 1) and (alert > 0)):
          counter = 0
          # Index of pass phrase character is one less to account for conditions
          idx1 = alphabet.index((passwd[counter - 1]).lower())
          idx2 = alphabet.index((strng[i]).lower())
          counter += 1

        # If the counter is greater than the pass phrase length and there are only alphabetic character so far
        elif((counter > len(passwd) - 1) and (alert == 0)):
          counter = 0
          idx1 = alphabet.index((passwd[counter]).lower())
          idx2 = alphabet.index((strng[i]).lower())
          counter += 1

        # If the counter is less than the pass phrase length and only alphabetic characters so far
        elif((counter <= len(passwd) - 1) and (alert == 0)):
          
          idx1 = alphabet.index((passwd[counter]).lower())
          idx2 = alphabet.index((strng[i]).lower())
          counter += 1

        # If the counter is less than the pass phrase length and non-alphabetic characters have been found
        elif((counter <= len(passwd) - 1) and (alert > 0)):
          
          idx1 = alphabet.index((passwd[counter - 1]).lower())
          idx2 = alphabet.index((strng[i]).lower())
          counter += 1


        
      # If there are non-alphabetic characters or not, and i is still less than length of pass phrase
      else:
        if(alert > 0):
          idx1 = alphabet.index((passwd[i - 1]).lower())
          idx2 = alphabet.index((strng[i]).lower())

      

        elif(alert == 0):
          idx1 = alphabet.index((passwd[i]).lower())
          idx2 = alphabet.index((strng[i]).lower())


        

      # Calculating encoding character by adding indexes of pass phrase character and string character, accounting for large indexes
      idx_case = idx1 + idx2
      if(idx_case > 25):
        idx_case = idx_case - 26
        
      case_letter = alphabet[idx_case]
      
      final.append(case_letter)
      
    
  # Returning result
  result = ""
  for item in final:
    result += item

  return(result)
      
    
  
# Decoding text using the vigenere cipher
def vigenere_decode ( strng, passwd ):

  # Saving the letters of the alphabet in a list of characters
  alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  
 # Saving the letters of the alphabet in a list of characters
  alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  
  final = []
  counter = 0
  alert = 0
  for i in range(len(strng)):
    # Adding to alert variable and appending character is non-alphabetic
    if(strng[i].isalpha() == False):
      final.append(strng[i])
      alert += 1
      

    
    if(strng[i].isalpha() == True):
      # If i is greater than pass phrase length
      if(i > len(passwd) - 1):
        # If counter is larger than length of pass phrase and non-alphabetic characters found
        if((counter > len(passwd) - 1) and (alert > 0)):
          counter = 0
          idx1 = alphabet.index((passwd[counter - 1]).lower())
          idx2 = alphabet.index((strng[i]).lower())
          counter += 1

        # If counter is larger than length of pass phrase and non-alphabetic characters not found

        elif((counter > len(passwd) - 1) and (alert == 0)):
          counter = 0
          idx1 = alphabet.index((passwd[counter]).lower())
          idx2 = alphabet.index((strng[i]).lower())
          
          
          counter += 1

        # If counter is less than length of pass phrase and non-alphabetic characters not found

        elif((counter <= len(passwd) - 1) and (alert == 0)):
          
          idx1 = alphabet.index((passwd[counter]).lower())
          idx2 = alphabet.index((strng[i]).lower())
          counter += 1

        # If counter is larger than length of pass phrase and non-alphabetic characters found

        elif((counter <= len(passwd) - 1) and (alert > 0)):
          
          idx1 = alphabet.index((passwd[counter - 1]).lower())
          idx2 = alphabet.index((strng[i]).lower())
          counter += 1


        
      # If i within range of length of pass phrase, then if non-alphabetic characters are found or not
      else:
        if(alert > 0):
          idx1 = alphabet.index((passwd[i - 1]).lower())
          idx2 = alphabet.index((strng[i]).lower())

        elif(alert == 0):
          idx1 = alphabet.index((passwd[i]).lower())
          idx2 = alphabet.index((strng[i]).lower())


        

      # Finding index of decoding character by subtracting indexes of pass phrase character from encoded text character
      idx_case = idx2 - idx1
      if(idx_case < 0):
        idx_case = idx_case + 26
        
      case_letter = alphabet[idx_case]
      
      final.append(case_letter)
      
    
  # Returning the result
  result = ""
  for item in final:
    result += item

  return(result)
      

def main():
  # open file for reading
  in_file = open ("./cipher.txt", "r")

  
  # print header for substitution cipher
  print ("Substitution Cipher")
  print ()

  # read line to be encoded
  line = in_file.readline()
  line = line.strip()

  # encode using substitution cipher
  encoded_str = substitution_encode (line)

  
  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Encoded Text: " + encoded_str)
  print ()

  
  # read line to be decoded
  line = in_file.readline()
  line = line.strip()

  # decode using substitution cipher
  decoded_str = substitution_decode (line)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

 

  # print header for vigenere cipher
  print ("Vigenere Cipher")
  print ()

  # read line to be encoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  passwd = in_file.readline()
  passwd = passwd.strip()

  # encode using vigenere cipher
  encoded_str = vigenere_encode (line, passwd)

  
  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Encoded Text: " + encoded_str)
  print ()

  
  
  
  # read line to be decoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  passwd = in_file.readline()
  passwd = passwd.strip()

  # decode using vigenere cipher
  decoded_str = vigenere_decode (line, passwd)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Decoded Plain Text: " + decoded_str)
  print ()
  

  # close file
  in_file.close()

main()

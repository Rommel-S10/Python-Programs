# Python-Programs

This is the Vigenère cipher method for encryption. It was strong during its time until modern cryptographic. 

# The way that it works:

1. Message: The text you want to encrypt
  - Example: "coding is a power few can understand"

2. Key: There must be word (Keyword) that is repeated or cycled through the length of the message. Each letter in the keyword will tell how much to shift to the correponding letter in the message 
    - Example of Keyword: "Software"

3. The Alphabet Shift: Each Letter in the message is shifted by a certain number of position in the alphabet. Each number is assigned by the corresponding letter in the keyword. The shift as mentioned in the previous sentences, is based on the alpahbetical index of the key letter
('a' = 0, 'b' = 1,... unitl 'z' = 25). 
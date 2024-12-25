alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

again = False

while not again:
    dir = input("encode or decode \n")
    text = input("enter text u want to encode or decode ").lower()
    shift = int(input("how many no to shift "))
    wordlen = len(text)
    def encodeme(text,shift):
        encoded_text =""
        for i in text:
            updated_index = alphabets.index(i)+shift
        # for index out of bound error , 0-25 range always
            updated_index = updated_index % len(alphabets)
            
            encoded_text += alphabets[updated_index]
        
        return encoded_text

        # if i.isalpha():
        #     encoded_text += chr((ord(i)-ord('a')+shift)% 26 + ord('a'))
        # else:
        #     encoded_text += i
        # 
        # 
    def decryptme(text,shift):
        decoded_text = ""
        for i in text:
            updated_index = alphabets.index(i)-shift
            
            updated_index = updated_index % len(alphabets)
            
            decoded_text += alphabets[updated_index]
            
        return decoded_text
    if dir =="encode":
        print(encodeme(text,shift))
    elif dir == "decode":
        print(decryptme(text,shift))
    
    else:
        print("invalid option")
        
    again = input("Do you want to process another text? (yes or no): ").lower()

    if again=="no":
        again = True
    else:
        again=False
print("thankyou")

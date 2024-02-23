# 2) call the instance method, which should internally call the classmethod you prepared for the conversion, 
# pass the string data to classmethod and do the conversion. 
# No need to consider special characters for now. 
# Expected output for the string "ABcD1293Z" is "cdEf2304b"

class Cypher:
    def __init__(self, input_string):
        self.input_string = input_string

    @classmethod
    def convert_string(cls, input_string):
        cypher_string = ''
        for char in input_string:
            if char.isdigit():
                cypher_string += str((int(char) + 1) % 10)  
            elif char.isalpha():
                shifted_char = chr(((ord(char.lower()) - ord('a') + 2) % 26) + ord('a'))
                cypher_string += shifted_char.lower() if char.islower() else shifted_char
            else:
                cypher_string += char  
        return cypher_string

    def invoke_conversion(self):
        return self.convert_string(self.input_string)

input_string = input("enter the string :")
cypher = Cypher(input_string)

print("Original String:", input_string)
print("Cypher String:", cypher.invoke_conversion())

class Recursion: 
    @classmethod
    def FindUppercaseRecursive(cls,input_str,idx=0):
        if input_str[idx].isupper():
            return input_str[idx]
        if idx == len(input_str) -1:
            return "No uppercase char found."
        return FindUppercaseRecursive(input_str,idx+1)
    
    @classmethod
    def lenRecursive(cls,data):
        if data == '':
            return 0
        return 1 + lenRecursive(data[1:])
    
    vowels = "aeiou"
    @classmethod
    def CountConsonants(cls,data):
        if data == '':
            return 0
        if data[0].lower() not in vowels and data[0].isalpha():
            return 1+ CountConsonants(data[1:])
        else:
            return CountConsonants(data[1:])
        
    @classmethod
    def MultiplayRecursive(cls,x,y):
        if x<y:
            return MultiplayRecursive(y,x)
        if y==0:
            return 0
        return 1+ MultiplayRecursive(x,y-1)
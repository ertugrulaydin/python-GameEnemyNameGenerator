import random

vowels = ("A","E","I","O","U")
consonants = ("B","C","D","F","G","H","J","K","L","M","N","P","R","Q","S","T","V","W","X","Y","Z")

nameLong = 4
name = ""

for i in range(nameLong):
    
    a=random.randint(0,1)
    
    randomConsonant = random.randint(0,len(consonants)-1)
    randomVowel = random.randint(0,len(vowels)-1)

    
    if(a==0):
        
        letter = consonants[randomConsonant]
        name = name + letter

        
    else:
        
        letter = vowels[randomVowel]
        name = name + letter

        
print(name)
waitInput = input()

print("Assalomu Alaykum !")

#Userdan matn olindi 
matn = input("matnni kiriting ")

#So'zlar ajratib olindi 
words = matn.split()

#Eng uzun so'z 1 chi so'z deb olindi 
max_words = words[0]

# For loop yordamida eng uzun so'z if yordamida aniqlandi 
for i in range (len(words)):
    if len(words[i]) > len(max_words):
        max_words = words[i]
print(max_words)              # Natija chqiarildi 
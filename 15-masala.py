print("Assalomu Alaykum !")

#Userdan qancha son kiritishi soraldi va olindi
number_count = int(input("Qancha son kiritmoqchisiz!"))

for i in range( 1 , number_count + 1) :
    number = int(input(f"{i}-Sonni kiriting!"))
    if number % 2 == 1 and number % 3 == 0 :     # Agar user kiritgan son toq hamda 3 ga bo'linsa 
       print(f"{number}")          # Shart bajariladi va natija chiqadi 
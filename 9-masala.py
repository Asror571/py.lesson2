print("Assalomu Alaykum Bratim Qandaysiz!")

#Userdan raqam olindi 
son = int(input("Raqamni kiriting !"))

#Yig'indini hisoblash uchun o'zgaruvchi olindi
sum = 0

# For loop yordamida hisoblab chiqarildi 
for i in range(1,son+1):       # son+1   sabab oxirgi sonni ham olishi uchun
    sum+=i                # Har loop aylanganda sonlarni hisoblab ketadi 
print(sum)
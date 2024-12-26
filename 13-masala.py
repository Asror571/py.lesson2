print("Assalomu Alaykum !")

#userdan ma'lumot olindi
number = int(input("Sonni kiriting !"))

# For 2 boshlab aylanadi chunki 1 tub son emas 
for i in range(2,number+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count+=1
    if count == 2:
        print(i, end = ' ')
    

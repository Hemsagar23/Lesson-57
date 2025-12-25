big_num = int(input("Enter your number: "))
small_num = int(input("Enter your sec number: "))

while(small_num):
    numberStore = small_num
    small_num = big_num%small_num
    big_num = numberStore

print(f"HCF of these numbers are {big_num}")

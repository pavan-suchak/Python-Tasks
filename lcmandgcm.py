num_one_fact=[]
num_two_fact=[]

common = []

first_num = int(input('Enter Number:'))

second_num = int(input('Enter Number:'))

# Factors of first_num
for i in range(1,first_num+1):
    if first_num%i==0:
        num_one_fact.append(i)

# Factors of second_num
for i in range(1,second_num+1):
    if second_num%i==0:
        num_two_fact.append(i)

for i in num_one_fact:
    if i in num_two_fact:
        common.append(i)

gcm = max(common)
lcm = (first_num * second_num) // gcm

print(f'LCM: {lcm}')
print(f'GCM: {gcm}')
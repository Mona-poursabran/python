def perfect_number(num):
    sum = 0
    s= ' '
    for i in range(1, num):
        if num % i == 0:
            yield(i)  # return one by one 
            sum += i  # sum each i 
            s += str(i)+'+'
    def check_result():
        if num == sum :
            print(f'Perfect: {num} is equal to sum of its proper divisors: {num} = ({s.rstrip(s[-1])} = {sum} )')
        elif num > sum :
            print(f'Lesser: prtfect < Number\n{num} > ({s.rstrip(s[-1])} = {sum} )')
        else :
            print(f'Greater: Perfect > Number\n{num} < ({s.rstrip(s[-1])} = {sum} )')

    check_result()


perfect_6 = perfect_number(6)
for j in perfect_6 :
    perfect_6

print('****'*5)

perfect_12= perfect_number(12)
for j in perfect_12 :
    perfect_12

print('****'*5)

perfect_8 = perfect_number(8)
for j in perfect_8:
    perfect_8


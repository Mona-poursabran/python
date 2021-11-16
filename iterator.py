# #Using Function : 
# def Primes(num):
#     for n in range(1, num):
#         if num > 1:
#             for i in range(2, n):
#                 if n % i == 0:
#                     break
#             else:
#                 print(n, end=' ') 
# Primes(13)
# print('\n')
#using __iter__ and __next__
class PrimeIter: 
    def __init__(self, num): 
        self.num = num - 1

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n < self.num:
            self.n += 1
            i = 2
            while i < (self.n // 2 + 1):
                if self.n % i == 0:
                    self.n = self.n + 1
                    if self.n > self.num:
                        raise StopIteration
                    i = 1
                i += 1
            else:
                return self.n
        else:
            raise StopIteration

p = PrimeIter(13)        
for i in p:
    print(i, end=' ')
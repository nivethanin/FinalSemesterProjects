<<<<<<< HEAD
print(0.108+0.016+0.064+0.012+0.072+0.144+0.008+0.576)
print(0.108+0.016+0.012+0.064)
print(0.108+0.012+0.072+0.008)
print(0.108+ 0.016+ 0.072+ 0.144)
print(0.2+0.2-0.108-0.012)

bbg = (3/5 * 1/4* 2/5 * 1/2)
bukake = 2/5* 3/4 * 3/5 * 1/2
print(f"yes mate: {bbg}")
print(f"no mate: {bukake}")
print()
=======
# print(0.108+0.016+0.064+0.012+0.072+0.144+0.008+0.576)
# print(0.108+0.016+0.012+0.064)
# print(0.108+0.012+0.072+0.008)
# print(0.108+ 0.016+ 0.072+ 0.144)
# print(0.2+0.2-0.108-0.012)

# bbg = (0.108+0.016)/(0.342)
# print(f"Bloody Test mate: {bbg}")

# psize = int(input("Insert a page size: "))
# offref = int(input("Insert your offset reference: "))

arr = [3085, 42095, 215201, 650000, 2000001]
lett = ['a', 'b', 'c', 'd', 'e']
psize = 1024
for x, ref in zip(lett, arr):
    pnum = int(ref/psize)
    offval = ref % psize
    
    print(f"{x}. Page number is {pnum} and offset value is {offval}")

>>>>>>> b7d89dc65bb25269d701a6185ebf4bb91a693f20

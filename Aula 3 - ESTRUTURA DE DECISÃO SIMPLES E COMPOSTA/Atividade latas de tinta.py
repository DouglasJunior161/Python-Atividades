import math
metrosquad = float (input())

tintalitro = 18
tinta = metrosquad / 3
latas = tinta / tintalitro
latasround = math.ceil(latas)
precotinta = latasround * 120

print(latasround)
print(f"{precotinta:.2f}")
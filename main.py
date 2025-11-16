from fractions import Fraction
from math import gcd
from itertools import islice

def rationals():
    """Генератор, перечисляющий все рациональные числа по одному разу.
    Представление: приводимая дробь p/q с q>0 и gcd(|p|,q)=1.
    Перебираем пары (p,q) в порядке возрастания |p|+q (диагоналями).
    """
    k = 0
    while True:
        for q in range(1, k + 2):
            p_abs = k - q
            if p_abs < 0:
                continue
            if p_abs == 0:
                p_vals = (0,)
            else:
                p_vals = (-p_abs, p_abs)
            for p in p_vals:
                if abs(p) == 0:
                    if q != 1:  # 0 допускаем только как 0/1
                        continue
                else:
                    if gcd(abs(p), q) != 1: # наибольший общий делитель чисел p и q ->  Если дробь p/q сократимая, то пропускаем её
                        continue
                yield Fraction(p, q)
        k += 1

# Пример: вывести первые 80 рациональных
gen = rationals()

print("80 рациональных чисел:")
for i, r in enumerate(islice(gen, 80), 1):
    print(f"{i}: {r}")

print("Для получения следующего рационального числа нажмите Enter.\nДля выхода введите exit")
i = 81
while True:
    user_input = input()
    if user_input == "exit":
        break
    print(f"{i}: {next(gen)}", end="")
    i += 1

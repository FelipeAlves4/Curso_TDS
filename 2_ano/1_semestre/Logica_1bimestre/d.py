n = 1500
en = False
while n <= 2700 and not en: 
    if n % 5 == 0 and n % 7 == 0:
        print(f"{n}")
        en = True
    n += 1 

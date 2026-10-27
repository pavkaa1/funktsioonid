def liida(a, b):
    return a + b

def lahuta(a, b):
    return a - b

def korruta(a, b):
    return a * b

def jaga(a, b):
    if b == 0:
        return "Nulliga jagada ei saa!"
    return a / b


while True:
    print("\n--- TASKUKALKULAATOR ---")
    print("1. Liitmine")
    print("2. Lahutamine")
    print("3. Korrutamine")
    print("4. Jagamine")
    print("5. Lõpeta")

    valik = input("Vali tehe (1-5): ")

    if valik == "5":
        print("Kalkulaator lõpetab töö.")
        break

    if valik in ["1", "2", "3", "4"]:
        try:
            a = float(input("Sisesta esimene arv: "))
            b = float(input("Sisesta teine arv: "))

            if valik == "1":
                tulemus = liida(a, b)
            elif valik == "2":
                tulemus = lahuta(a, b)
            elif valik == "3":
                tulemus = korruta(a, b)
            elif valik == "4":
                tulemus = jaga(a, b)

            print("Tulemus:", tulemus)

        except ValueError:
            print("Viga! Palun sisesta kehtivad arvud.")
    else:
        print("Vale valik! Vali number 1-5.")
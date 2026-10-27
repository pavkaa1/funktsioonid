def taishaalikuid(tekst):
    taishaalikud = "aeiouõäöü"
    arv = 0

    for taht in tekst.lower():
        if taht in taishaalikud:
            arv += 1

    return arv


# Test
print(taishaalikuid("Tere"))       # 2
print(taishaalikuid("Õunapuu"))    # 5
print(taishaalikuid("ABC"))        # 1
print(taishaalikuid(""))           # 0
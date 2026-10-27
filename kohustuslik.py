
def lisa_opilane(nimed, punktid, nimi, tulemus):
    nimi = nimi.strip()

    if nimi == "":
        print("Viga! Nimi ei tohi olla tühi.")
        return

    if nimi.casefold() in [n.casefold() for n in nimed]:
        print("Sellise nimega õpilane on juba olemas!")
        return

    if tulemus < 0 or tulemus > 100:
        print("Viga! Punktid peavad olema vahemikus 0–100.")
        return

    nimed.append(nimi)
    punktid.append(tulemus)
    print("Õpilane lisatud!")


def arvuta_hinne(punktid):
    hinded = []

    for p in punktid:
        if p >= 90:
            hinne = 5
        elif p >= 75:
            hinne = 4
        elif p >= 50:
            hinne = 3
        elif p >= 20:
            hinne = 2
        else:
            hinne = 1

        hinded.append(hinne)

    return hinded


def leia_keskmine(punktid):
    if len(punktid) == 0:
        return 0

    return sum(punktid) / len(punktid)


def leia_parim(nimed, punktid):
    if len(punktid) == 0:
        return None

    parim_indeks = 0

    for i in range(1, len(punktid)):
        if punktid[i] > punktid[parim_indeks]:
            parim_indeks = i

    return nimed[parim_indeks], punktid[parim_indeks]


def leia_norgim(nimed, punktid):
    if len(punktid) == 0:
        return None

    norgim_indeks = 0

    for i in range(1, len(punktid)):
        if punktid[i] < punktid[norgim_indeks]:
            norgim_indeks = i

    return nimed[norgim_indeks], punktid[norgim_indeks]


def kuva_opilased(nimed, punktid):
    if len(nimed) == 0:
        print("Õpilasi pole veel lisatud.")
        return

    hinded = arvuta_hinne(punktid)

    print("\n--- ÕPILASTE TULEMUSED ---")

    for i in range(len(nimed)):
        print(
            f"{i + 1}. {nimed[i]}: "
            f"{punktid[i]} punkti, hinne {hinded[i]}"
        )


def kuva_statistika(nimed, punktid):
    if len(nimed) == 0:
        print("Statistikat ei saa kuvada, sest õpilasi pole.")
        return

    parim = leia_parim(nimed, punktid)
    norgim = leia_norgim(nimed, punktid)
    hinded = arvuta_hinne(punktid)

    print("\n=================================")
    print("       KLASSI STATISTIKA")
    print("=================================")

    print("Õpilasi kokku:", len(nimed))
    print(f"Keskmine punktisumma: {leia_keskmine(punktid):.2f}")
    print(f"Parim tulemus: {parim[0]} ({parim[1]} p)")
    print(f"Nõrgim tulemus: {norgim[0]} ({norgim[1]} p)")

    print("\nHinnete jaotus:")

    for hinne in range(5, 0, -1):
        arv = hinded.count(hinne)

        if arv == 1:
            sona = "õpilane"
        else:
            sona = "õpilast"

        print(f"Hinne {hinne}: {arv} {sona}")


def otsi_opilane(nimed, punktid, nimi):
    for i in range(len(nimed)):
        if nimed[i].casefold() == nimi.strip().casefold():
            hinne = arvuta_hinne([punktid[i]])[0]

            print(f"Leitud õpilane: {nimed[i]}")
            print(f"Punktisumma: {punktid[i]}")
            print(f"Hinne: {hinne}")
            return nimed[i], punktid[i]

    print("Sellist õpilast ei leitud.")
    return None


def kuva_menuu():
    print("\n=================================")
    print("     ÕPILASTE HINNETE SÜSTEEM")
    print("=================================")
    print("1. Lisa õpilane")
    print("2. Kuva kõik õpilased")
    print("3. Kuva klassi statistika")
    print("4. Otsi õpilast nime järgi")
    print("0. Välju")


def loe_punktid():
    while True:
        try:
            tulemus = int(input("Sisesta punktisumma (0–100): "))

            if 0 <= tulemus <= 100:
                return tulemus

            print("Viga! Sisesta punktid vahemikus 0–100.")

        except ValueError:
            print("Viga! Sisesta punktisumma täisarvuna.")


def pohiprogramm():
    nimed = []
    punktid = []

    while True:
        kuva_menuu()
        valik = input("Vali tegevus: ").strip()

        if valik == "1":
            nimi = input("Sisesta õpilase nimi: ")
            tulemus = loe_punktid()
            lisa_opilane(nimed, punktid, nimi, tulemus)

        elif valik == "2":
            kuva_opilased(nimed, punktid)

        elif valik == "3":
            kuva_statistika(nimed, punktid)

        elif valik == "4":
            nimi = input("Sisesta otsitava õpilase nimi: ")
            otsi_opilane(nimed, punktid, nimi)

        elif valik == "0":
            print("Programm lõpetatud.")
            break

        else:
            print("Vigane valik! Proovi uuesti.")


pohiprogramm()

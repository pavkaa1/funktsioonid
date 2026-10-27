punktid = [78, 45, 92, 67, 34, 100, 56, 81]

def keskmine(punktid):
    return sum(punktid) / len(punktid)

def parim_tulemus(punktid):
    parim = punktid[0]
    for punkt in punktid:
        if punkt > parim:
            parim = punkt
    return parim

def norgim_tulemus(punktid):
    norgim = punktid[0]
    for punkt in punktid:
        if punkt < norgim:
            norgim = punkt
    return norgim

def edukate_arv(punktid, piir=50):
    arv = 0
    for punkt in punktid:
        if punkt >= piir:
            arv += 1
    return arv

print("Keskmine tulemus:", keskmine(punktid))
print("Parim tulemus:", parim_tulemus(punktid))
print("Nõrgim tulemus:", norgim_tulemus(punktid))
print("Edukate arv:", edukate_arv(punktid))
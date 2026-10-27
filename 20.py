def arvu_tyyp(arv):
    if arv > 0:
        return "Positiivne"
    elif arv < 0:
        return "Negatiivne"
    else:
        return "Null"


# Test
print(arvu_tyyp(5))   
print(arvu_tyyp(-3)) 
print(arvu_tyyp(0))  
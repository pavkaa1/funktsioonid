def teisenda_sekundid(sekundid):
    tunnid = sekundid // 3600
    minutid = (sekundid % 3600) // 60
    sekundid_ule = sekundid % 60

    return tunnid, minutid, sekundid_ule

print(teisenda_sekundid(3675))
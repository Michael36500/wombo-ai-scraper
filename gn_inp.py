import random as rn
import hastags

def gn_inp():
    Tpods = open("gn_inp_podstat.txt", "r")
    Tprid = open("gn_inp_pridav.txt", "r")

    Xpods = []
    Xprid = []
    for a in Tpods:
        Xpods.append(a)
    for a in Tprid:
        Xprid.append(a)

    pods = []
    prid = []
    for a in Xpods:
        l = len(a)
        short = a[:l - 1]
        pods.append(short)
    for a in Xprid:
        l = len(a)
        short = a[:l - 1]
        prid.append(short)

    Tphras = open("gn_inp_phrase.txt", "r")
    # print(Tphras)
    Xphras = []
    for a in Tphras:
        Xphras.append(a)
    phras = []
    for a in Xphras:
        l = len(a)
        short = a[:l - 1]
        phras.append(short)


    # print(pods)
    # print(prid)
    # print(phras)

    pods = str(pods[rn.randint(0, len(pods)-1)])
    prid = str(prid[rn.randint(0, len(prid)-1)])
    phras = str(phras[rn.randint(0, len(phras)-1)])

    out = "What a " + phras + " artwork of " + prid + " " + pods + " from steampunk world!!" +  "\n\n\n{}".format(hastags.chs_hst())

    return out

def gn_inp_short():
    Tpods = open("gn_inp_podstat.txt", "r")
    Tprid = open("gn_inp_pridav.txt", "r")

    Xpods = []
    Xprid = []
    for a in Tpods:
        Xpods.append(a)
    for a in Tprid:
        Xprid.append(a)

    pods = []
    prid = []
    for a in Xpods:
        l = len(a)
        short = a[:l - 1]
        pods.append(short)
    for a in Xprid:
        l = len(a)
        short = a[:l - 1]
        prid.append(short)

    # Tphras = open("gn_inp_phrase.txt", "r")
    # # print(Tphras)
    # Xphras = []
    # for a in Tphras:
    #     Xphras.append(a)
    # phras = []
    # for a in Xphras:
    #     l = len(a)
    #     short = a[:l - 1]
    #     phras.append(short)


    # print(pods)
    # print(prid)
    # print(phras)

    pods = str(pods[rn.randint(0, len(pods)-1)])
    prid = str(prid[rn.randint(0, len(prid)-1)])
    # phras = str(phras[rn.randint(0, len(phras)-1)])

    # out = "What a " + phras + " artwork of " + prid + pods + " from steampunk world!!" +  "\n\n\n{}".format(hastags.chs_hst())
    out = prid + " " + pods

    return out





print(gn_inp())
print(gn_inp_short())
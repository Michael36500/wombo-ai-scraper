import random as rn

def chs_hst():
        
    freq = open("hst_freq.txt", "r")
    mine = open("hst_mine.txt", "r")
    rare = open("hst_rare.txt", "r")
    avg = open("hst_avg.txt", "r")

    freq = freq.readlines()
    mine = mine.readlines()
    rare = rare.readlines()
    avg = avg.readlines()

    def listing (inp):

        temp = []
        for a in inp:
            l = len(a)
            short = a[:l - 2]
            temp.append(short)
        return temp

    freq = listing(freq)
    mine = listing(mine)
    rare = listing(rare)
    avg = listing(avg)
    # txt.close()


    def ap_hst(inp, kolik):
        hst = []
        for b in range (kolik):
            hst.append(inp[rn.randint(0,len(inp) - 1)])
        return hst
    
    freq = ap_hst(freq, 2)
    mine = ap_hst(mine, 10)
    rare = ap_hst(rare, 15)
    avg = ap_hst(avg, 3)

    hst = str(freq) + str(mine) + str(rare) + str(avg)
    # print(hst)

    hst = str(hst)
    hst = hst.replace("[", "")
    hst = hst.replace("]", "")
    hst = hst.replace("'", "")
    hst = hst.replace(",", "")

    return hst
    # return "workds"

# for a in range(100000):
print(chs_hst())
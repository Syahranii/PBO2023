import math

def lbalok(p,l,t):    
    luas_balok = (2*p*l) + (2*p*t) + (2*l*t)
    return luas_balok
def vbalok(p,l,t):
    volume_balok = p*l*t 
    return volume_balok

def lbola(r):
    Luas_bola = 4*math.pi*r*r
    return Luas_bola
def vbola(r):
    Volume_bola = 4/3*math.pi*r *r *r
    return Volume_bola

def lskerucut(r,s):
    luas_selimut = math.pi*r*s
    return luas_selimut
def lpkerucut(s,r):
    luas_permukaan = (math.pi*r*s) + (math.pi*r*r*r)
    return luas_permukaan
def vkerucut(r,t):
    volume_kerucut = 1/3*math.pi*r*r*t
    return volume_kerucut

def lkubus(r):
    Luas_kubus = 6*r*r
    return Luas_kubus
def vkubus(r):
    Volume_kubus = r*r*r
    return Volume_kubus

def lalas(ps):
    luas_alas = ps * ps
    return luas_alas
def lsisi_tegak(ps,tl):
    luas_sisi_tegak = 4 * (1/2 * ps * tl)
    return luas_sisi_tegak
def lplimas_segiempat(la,st):
    luas_permukaan_limas_segiempat = la + st
    return luas_permukaan_limas_segiempat
def vlimas_segiempat(la,tl):
    volume_limas_segiempat = 1/3 * la * tl
    return volume_limas_segiempat

def lsegitiga_alas(ps,ts):
    luas_segitiga_alas = 0.5 * ps * ts
    return luas_segitiga_alas
def lplimas_segitiga(sa,ps,tl):
    luas_permukaan_limas_segitiga = sa + 3 * (0.5 * ps * tl)
    return luas_permukaan_limas_segitiga
def vlimas_segitiga(sa,tl):
    volume_limas_segitiga = (1/3) * sa * tl
    return volume_limas_segitiga

def lsegitiga(at,ts):
    luas_segitiga = 1/2 * at * ts
    return luas_segitiga
def lsprisma(tp,ts):
    luas_selimut_prisma = 3 * tp* ts
    return luas_selimut_prisma
def lpprisma(ts,at,tp):
    luas_permukaan_prisma = ts* at + (3 * tp)
    return luas_permukaan_prisma
def vprisma(at,ts,tp):
    volume_prisma = 1/2 * at * ts * tp
    return volume_prisma

def lstabung(r,t):
    selimut_tabung = 2 * math.pi * r * t
    return selimut_tabung
def lptabung(r,t):
    luas_permukaan_tabung = (2 * math.pi * r * t) + 2 * math.pi * r * r
    return luas_permukaan_tabung
def vtabung(r,t):
    volume_tabung = math.pi * r * r * t
    return volume_tabung

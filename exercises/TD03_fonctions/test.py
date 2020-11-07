# temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    seconde = temps[0]*24*3600 + temps[1]*3600 + temps[2]*60 + temps[3]
    return seconde


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    j = seconde // (24*3600)
    h = (seconde % (3600*24)) // 3600
    m = (seconde % (3600*24)) % 3600 // 60
    s = ((seconde % (3600*24)) % 3600) % 60
    return (j, h, m, s)


# fonction auxiliaire ici
def pluriel(mot):
    """Renvoie la forme plurielle d'un mot càd rajoute un s"""
    return (mot+"s")


def afficheTemps(temps):
    mot = ["jour", "heure", "minute", "seconde"]
    for i in range(4):
        if temps[i] > 1:
            return (temps[i], pluriel(mot[i]))
        elif temps[i] == 1:
            return (temps[i], mot[i])


def demandeTemps():
    """demande de rentrer un nb de j, h ,min, sec"""
    j = int(input("how many days?"))
    h = int(input("how many hours?"))
    while h > 23:
        print("wrong. do it again")
        h = int(input())
    m = int(input("how many minutes?"))
    while m > 59:
        print("wrong. do it again")
        m = int(input())
    s = int(input("and how many seconds?"))
    while s > 59:
        print("wrong. do it again")    
        s = int(input())    
    return (j, h, m, s)


def sommeTemps(temps1, temps2):
    s = tempsEnSeconde(temps1)+tempsEnSeconde(temps2)
    t = secondeEnTemps(s)
    return t


sommeTemps((2, 3, 4, 25), (5, 22, 57, 1)) 
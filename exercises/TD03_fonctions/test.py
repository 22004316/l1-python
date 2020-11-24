def tempsEnDate(temps):
    année = 1970+temps[0]//365
    jour = temps[0] % 365
    heure = temps[1]
    minute = temps[2]
    seconde = temps[3]
    return (année, jour, heure, minute, seconde)


def pluriel(mot):
    """Renvoie la forme plurielle d'un mot càd rajoute un s"""
    return (mot+"s")
    
def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    j = seconde//(24*3600)
    h = (seconde %(3600*24))//3600
    m = (seconde%(3600*24)) % 3600//60
    s = ((seconde%(3600*24)) % 3600) % 60
    return (j,h,m,s)

def afficheTemps(temps):
    """fonction d'affichage du temps en j, h, min, sec"""
    mot=["jour","heure","minute","seconde"]
    for i in range(4):
        if temps[i] >1 :
            print (temps[i], pluriel(mot[i])," ", end = '')
        elif temps[i] ==1 :
            print  (temps[i], mot[i]," ", end = '')   

def afficheDate(date = -1):
    mot=["année","jour","heure","minute","seconde"]
    for i in range(5):
        if tempsEnDate[i] >1 :
            print (tempsEnDate[i], pluriel(mot[i])," ", end = '')
        elif tempsEnDate[i] ==1 :
            print  (temps[i], mot[i]," ", end = '')

temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))
afficheDate()            
            
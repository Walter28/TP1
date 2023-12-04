liste_employer = []

def saisir_infos_employer(nom_entreprise, nb_employer):

    liste_nom = []
    liste_salaire = []

    for i in range(nb_employer):

        nom = input("Entrer le nom : ")
        salaire = input("Entrer le salaire : ")

        liste_nom.append(nom)
        liste_salaire.append(int(salaire))

    liste_employer = [liste_nom, liste_salaire]

    return liste_employer

def filter_salaire(liste):

    salaire_min = min(liste[1])
    index_min = liste[1].index(salaire_min)
    salaire_max = max(liste[1])
    index_max = liste[1].index(salaire_max)

    employer_moin_payer = liste[0][index_min]
    employer_plus_payer = liste[0][index_max]

    return [employer_moin_payer, employer_plus_payer]
    

if __name__ == '__main__':

    nom_e = input("Entrer le nom de l'Ese : ")
    nb_e = int(input("Entrer le nombre des employer : "))

    print("")
    print(" +++++++++++ Enregistrement des employer pour {} +++++++++".format(nom_e))
    print("")
    info = saisir_infos_employer(nom_e, nb_e)

    # print(info)
    # time.sleep(10)

    
    moin_plus = filter_salaire(info)

    print("")
    demande_user = int(input("Voudriez vous afficher l'employer le moin et le plus payer ? (1 ou 0) : "))

    if demande_user == 1:

        print("Le moin payer est ", moin_plus[0])
        print("Le plus payer est ", moin_plus[1])

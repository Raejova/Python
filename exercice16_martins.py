def distance_hamming(mot1, mot2):
    cnt = 0
    if (len(mot1) == len(mot2)):
        for x in range(len(mot1)):
            if (mot1[x] != mot2[x]):
                cnt = cnt + 1

        return print(cnt)
    else:
        print("Les deux mots ne font pas la même longueur")


distance_hamming(mot1="JAPON", mot2="SAVON")
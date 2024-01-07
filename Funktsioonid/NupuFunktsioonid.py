def LisaSündmusNupuF(olek):
    miksEiTöötaPõhjused = []
    if olek.TäpsemaVaatePäev != None:
        miksEiTöötaPõhjused.append("Detailsma vaate aken on prg lahti.")
    if olek.SündmuseLisamine == True:
        miksEiTöötaPõhjused.append("Sündmuse lisamine juba käib.")
    if len(miksEiTöötaPõhjused) == 0:
        if olek.tegevuseNäitamine == True: print("Sündmuse lisamine: False -> True.")
        olek.SündmuseLisamine = True
    else:
        if len(miksEiTöötaPõhjused) == 1 and olek.tegevuseNäitamine == True:
            print("Aken ei avane, sest " + miksEiTöötaPõhjused[0].lower())
        else:
            print("Sündmute lisamine ei alga järgmistel põhjustel: ")
            for i in range(len(miksEiTöötaPõhjused)):
                print("   " + str(i+1) + ". " + miksEiTöötaPõhjused[i])
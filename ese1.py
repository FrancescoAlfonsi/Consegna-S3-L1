
print("Questo programma ti aiuterà a calcolare il perimetro di alcune figure geometriche.")

while(1):
    data_validation=False
    while data_validation==False:
        scelta=input("Scegliere: \na) per il quadrato;\nb) per il cerchio;\nc) per il rettangolo; \nd) per uscire\n").lower()
        if scelta!='a' and scelta!='b' and scelta!='c' and scelta!='d':
            print("Input non valido.")
            print("Inserisci soltanto una lettera tra a, b, c e d")
            continue
        else:
            data_validation=True
            
    data_validation=False
    if scelta=='a':
        while data_validation==False:
            lato=input("Inserisci il lato del quadrato (sono accettati soltanto numeri): ")
            try:
                lato=float(lato)
                print("Il perimetro del quadrato è: ",lato*4)
                data_validation=True
            except:
                continue
            
    data_validation=False
    if scelta=='b':
        while data_validation==False:
            raggio=input("Inserisci il raggio del cerchio (sono accettati soltanto numeri): ")
            try:
                raggio=float(raggio)
                print("Il perimetro del cerchio è: ",2*raggio*3.14)
                data_validation=True
            except:
                continue
            
    data_validation=False
    if scelta=='c':
        while data_validation==False:
            lato1=input("Inserisci la base del rettangolo (sono accettati soltanto numeri): ")
            lato2=input("Inserisci l'altezza del rettangolo (sono accettati soltanto numeri): ")
            try:
                lato1=float(lato1)
                lato2=float(lato2)
                data_validation=True
                print("Il perimetro del rettangolo è: ",2*(lato1+lato2))
            except:
                continue
            
    if scelta=='d':
        break

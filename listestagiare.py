import pickle
from stagiare import stagiare
class ListeStagiare:
    ListeS=list()
    
    
    @staticmethod
    def AjoutStagiare():
        N= int(input("Saisir le Nombre de stagiare a saisir :"))
        
        for i in range(N):
            
            Mat = int(input("Saisir le Nombre du Matricule"))
            S=stagiare(Mat)#constructeur de recherche
            if S in Listetagiare.ListeS:
                print("Stagiare deja existant")
            else:
                Nom=input("Saisir le Nom:   ")
                Prenom=input(" Saisir Prenom: ")
                Age=int(input("Saisir l'age: "))
                Fil=input("Saisir la filiere")
                S= stagiare(Mat,Nom,Prenom,Age,Fil)
                ListeSatagiare.ListeS.append(S) 
    @staticmethod
    def AffichageStagiare():
        for OS in ListeStagiare.ListeS:
            print (OS)
    @staticmethod
    def TrieAge():
        ListeStagiare.ListeS.sort(key=lambda x: x.Age, reverse=True)
        print('Fichier Trie par age ave succees') 
    @staticmethod
    def TrieNom():
         ListeStagiare.ListeS.sort(key=lambda x: x.nom,reverse=False)
         print('Fichier Trie par age ave succees')
    @staticmethod
    def supprimerStagiare():
        Mat=int(input('Saisir la Matricule a supprimer: '))
        S=stagiare(Mat)#construceur de recherche
        if S in ListeStagiare.ListeS:
            Rep=input("Voulez vous vraiment supprimez(O/N): ")
            print(S)
            if(Rep.upper()=='O'):
                ListeStagiare.ListeS.remove(S)
                print('Stagiare supprimer avec succes')
            else:
                print("Ce stagiare nexiste pas dans la liste")
    @staticmethod
    def RechercherStagiare():
        
        Mat=int(input(' sasir le matricule de stagiare a rechercher: '))
        S= stagiare(Mat)
        if S in ListeStagiare.ListeS:
            i=ListeStagiare.ListeS.index(S)
            print(ListeStagiare.ListeS[i])
        else:
            print("ce stagiare nexiste pas dans la liste!!!")
#================================================================

    @staticmethod
    def SauvgarderStagiare():
        f=open('LesStagiare.b','wb')
        serial==pickle.dumps(ListeStagiare.ListeS)
        f.write(serial)
        f.close()
        print("\tDonnees sauvgardes avec succes.....")
#===============================================================
#================================================================


    @staticmethod
    def RestaurerStagiare():
        f=open('lesSatagiare.b','rb')
        Donneee=f.read()
        ListeStagiare.ListeS=pickle.loads(Donneee)
        print("\tDonnees Restaurer par succees")
        
               
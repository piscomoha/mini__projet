class stagiare:
    nbstagiare=0
    def __init__(self,num,nom,prenom,age,filiere):
        self.__num = num
        self.__nom = nom
        self.__prenom=prenom
        self.__age = age
        self.__filiere = filiere
        mbsstagiare+=1
    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self,n):
        self.__num = n
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,name:str):
        self.__nom = name
    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self,pre:str):
        self.__prenom = pre
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,a:int):
        self.__age = a
    @property
    def filiere(self):
        return self.__filiere
    @filiere.setter
    def filiere(self,f):
        self.__filiere = f
    def __str__(self):
        return f'num de stagiare est:{self.__num},   , Nom de stagiare est:{self.__nom},  , Prenom de stagiare est:{self.__prenom},  ,Age du Stagiare est:{self.__age},   ,filiere du stagiare est:{self.__filiere}'
    def Affiche_detaille(self):
        print('================================================================')
        print(' numero est: {self.__num}')
        print(' Nom est: {self.__nom}')
        print(' Prenom est: {self.__prenom}')
        print(' age est: {self.__age}')
        print(' filiere est: {self.__filiere}')
    def __eq__(self,n:"stagiare")->bool:
        return  n.__num==self.__num 
    
   
    
    
        
        
        
        
        
        
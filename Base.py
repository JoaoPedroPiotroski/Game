import random
print("---- Você começa sua aventura ----")
print("      Escolha seu personagem       ")
print("Você pode escolher entre :  ")
print("1 - O GUERREIRO que empunha espada e escudo, um personagem bastante equilibrado")
print("2 - O MAGO que empunha seu cajado, dando grande quantidade de dano")
print("3 - O TANQUE que empunha um grande escudo, dando grande capacidade de defesa")
charclass=input("> ")
if charclass == "1":
    print("Ótimo! Você escolheu o guerreiro!")
    print("Você começa com uma quantidade igual de defesa e ataque")
    ataque=10
    defesa=10
elif charclass == "2":
    print("Ótimo! Você escolheu o mago!")
    print("Você começa com uma grande quantidade de ataque, mas pouca defesa")
    ataque=15
    defesa=5
elif charclass == "3":
    print("Ótimo! Você escolheu o tanque!")
    print("Você começa com uma maior quantidade de defesa, mas menor ataque")
    ataque=8
    defesa=12
firsttime=1
monsterhp=1
playermaxhp=25
playerhp=25
playerlevel=1
playerwantstocontinue=""
if firsttime==1:
        xp=0
print("Agora é hora de começar sua aventura de verdade!")
while len(str(playerwantstocontinue))==0:
    if playerlevel == 1:
            if firsttime==1:
                monsterhp=(random.randint(10,20))
                monsterattack=(random.randint(5,10))
                monsterdefense=(random.randint(5,10))        
            elif firsttime!=0:
                monsterhp=(random.randint(10,30))
                monsterattack=(random.randint(5,15))
                monsterdefense=(random.randint(5,15))
    elif playerlevel == 2:
            monsterhp=(random.randint(20,40))
            monsterattack=(random.randint(15,25))
            monsterdefense=(random.randint(15,25))
    elif playerlevel == 3:
            monsterhp=(random.randint(30,50))
            monsterattack=(random.randint(25,35))
            monsterdefense=(random.randint(25,35))
    elif playerlevel == 4:
            monsterhp=(random.randint(40, 60))
            monsterattack=(random.randint(35, 45))
            monsterdefense=(random.randint(45, 55))
    elif playerlevel == 5:
            monsterhp=(random.randint(50,70))
            monsterattack=(random.randint(55,65))
            monsterdefense=(random.randint(55,65))
    elif playerlevel == 6:
            monsterhp=(random.randint(60,80))
            monsterattack=(random.randint(65,75))
            monsterdefense=(random.randint(65,75))
    elif playerlevel == 7:
            monsterhp=(random.randint(70,90))
            monsterattack=(random.randint(75,85))
            monsterdefense=(random.randint(75,85))
    elif playerlevel == 8:
            monsterhp=(random.randint(80,100))
            monsterattack=(random.randint(85,95))
            monsterdefense=(random.randint(85,95))
    elif playerlevel == 9:
            monsterhp=(random.randint(90,110))
            monsterattack=(random.randint(95,105))
            monsterdefense=(random.randint(95,105))
    elif playerlevel == 10:
            monsterhp=(random.randint(100,120))
            monsterattack=(random.randint(105,115))
            monsterdefense=(random.randint(105,115))
    maxmonsterhp=monsterhp                                                            
    if monsterhp <15:
        species1=["slime","rato"]
    elif 15 <= monsterhp <25:
        species1=["goblin","mão rastejante","morcego"]
    elif 25<= monsterhp <45:
        species1=["esqueleto","fantasma fracote","mago wannabe","morcego gigante","homem lama"]
    elif 45 <= monsterhp < 55:
        species1=["gato marinho","pato-coelho","beholder cego","lich apodrecido"]
    elif 55 <= monsterhp <65:
        species1=[]
    species=(random.choice(species1))
    print("Você encontra um %s!"%species)    
    while monsterhp > 0:    
                print("Hp do monstro: %d / %d   Seu hp: %d / %d  Seu nivel: %d   "%(monsterhp, maxmonsterhp, playerhp, playermaxhp, playerlevel))
                print("Seu ataque: %d   Sua defesa: %d Seu xp: %d"%(ataque, defesa, xp))
                if firsttime==1:
                        print("Você ataca ou defende?")
                firsttime=2
                print("1 - Atacar  2 - Defender")
                decisao=int(input("> "))
                if decisao==1:
                                        mdecision=random.randint(1,100)
                                        if mdecision > 70 and monsterhp > 0:
                                                                        print("O %s defende!"%species)
                                                                        damagetoplayer=(monsterattack)/((random.randint(1,2)))
                                                                        damagetomonster=(ataque*(random.randint(1,2)))-(monsterdefense*(random.randint(1,2)))
                                                                        if damagetomonster > 0 :
                                                                                                                monsterhp-=damagetomonster
                                                                        if damagetoplayer > 0:
                                                                                                                playerhp-=damagetoplayer
                                        elif mdecision <=70 and monsterhp > 0:
                                                                        print("O %s ataca!"%species)
                                                                        damagetoplayer=monsterattack-defesa/(random.randint(1,2))
                                                                        damagetomonster=ataque-monsterdefense/(random.randint(1,2))
                                                                        if damagetomonster > 0 :
                                                                                                                monsterhp-=damagetomonster
                                                                        if damagetoplayer > 0:
                                                                                                                playerhp-=damagetoplayer
                                                                        
                elif decisao==2:
                                        mdecision=random.randint(1,100)
                                        if mdecision > 70 and monsterhp > 0:
                                                                        print("O %s ataca!"%species)
                                                                        damagetoplayer=monsterattack-defesa*(random.randint(1,2))
                                                                        damagetomonster=ataque-monsterdefense/(random.randint(1,2))
                                                                        if damagetomonster > 0 :
                                                                                                                monsterhp-=damagetomonster
                                                                        if damagetoplayer > 0:
                                                                                                                playerhp-=damagetoplayer
                                        elif mdecision <=70 and monsterhp > 0:
                                                                        print("O %s defende!"%species)
                                                                        damagetoplayer=monsterattack/(random.randint(1,2))-defesa*(random.randint(1,2))
                                                                        damagetomonster=ataque/(random.randint(1,2))-(monsterdefense)*(random.randint(1,2))
                                                                        if damagetomonster > 0 :
                                                                                                                monsterhp-=damagetomonster
                                                                        if damagetoplayer > 0:
                                                                                                                playerhp-=damagetoplayer
                print("Você deu %d de dano no %s e você tomou %d de dano"%(damagetomonster, species, damagetoplayer))
                if playerhp < 0:
                        break
                if monsterhp <= 0:
                        print("O %s morreu!"%species)
                        break
    if  monsterhp < 0:
                        xp = xp+((monsterattack+monsterdefense)/2)
                        print("Você ganhou %dXp"%xp)
                        if xp >= 10*playerlevel:
                                        print("Você aumentou 1 nivel!")
                                        playerlevel += 1
                                        playermaxhp += 10
                                        ataque += 10
                                        defesa += 10
                                        playerhp=playermaxhp
                                        xp=0        
    print("Continuar - Nada    Parar - Digite qualquer coisa")
    playerwantstocontinue=input("> ")
    if playerhp <= 0:
                print("You died")
                playerwantstocontinue=14414
    playerhp+=playermaxhp/2
    if playerhp > playermaxhp:
            playerhp=playermaxhp

Exit=input("-Pressione qualquer tecla para sair-")

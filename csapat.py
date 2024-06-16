class csapat:
    def __init__(self, sor:str) -> None:
        sor=sor.strip().split(";")
        self.orszag=sor[0]
        self.reszvetelek_szama=int(sor[1])
        self.elso_reszvetel=int(sor[2])
        self.utolso_reszvetel=int(sor[3])
        self.legjobb_eredmeny=sor[4]
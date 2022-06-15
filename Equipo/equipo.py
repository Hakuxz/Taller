class equipo:
    def __init__(self,nombre,tipo,dano,tipoDano):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__dano = dano
        self.__tipoDano = tipoDano

    @property # ------------------------------------->>
    def nombre(self) -> str:
        return self.__nombre

    @property # ------------------------------------->>
    def tipo(self) -> str:
        return self.__tipo

    @property # ------------------------------------->>
    def raza(self) -> str:
        return self.__dano

    @property # ------------------------------------->>
    def genero(self) -> str:
        return self.__tipoDano
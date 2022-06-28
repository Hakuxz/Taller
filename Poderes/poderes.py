class poderes:
    def __init__(self,id_poder,nombre,detalle,id_raza):
        self.__id_poder = id_poder
        self.__nombre = nombre
        self.__detalle = detalle
        self.__id_raza = id_raza

    @property # ------------------------------------->>
    def id(self) -> int:
        return self.__id_poder

    @property # ------------------------------------->>
    def nombre(self) -> str:
        return self.__nombre

    @property # ------------------------------------->>
    def detalle(self) -> str:
        return self.__detalle

    @property # ------------------------------------->>
    def raza(self) -> int:
        return self.__id_raza
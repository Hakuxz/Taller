class habilidades:
    def __init__(self,id_poder,nombre,detalle):
        self.__id_poder = id_poder
        self.__nombre = nombre
        self.__detalle = detalle

    @property # ------------------------------------->>
    def id(self) -> str:
        return self.__id_poder

    @property # ------------------------------------->>
    def nombre(self) -> str:
        return self.__nombre

    @property # ------------------------------------->>
    def detalle(self) -> str:
        return self.__detalle
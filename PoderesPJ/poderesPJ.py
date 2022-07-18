class poderesPJ:
    def __init__(self,id_personaje,id_poder):
        self.__id_personaje = id_personaje
        self.__id_poder = id_poder

    @property # ------------------------------------->>
    def personaje(self) -> int:
        return self.__id_personaje

    @property # ------------------------------------->>
    def poder(self) -> int:
        return self.__id_poder


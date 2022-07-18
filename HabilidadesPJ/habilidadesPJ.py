class habilidadesPJ:
    def __init__(self,id_personaje,id_habilidad):
        self.__id_personaje = id_personaje
        self.__id_habilidad = id_habilidad

    @property # ------------------------------------->>
    def personaje(self) -> int:
        return self.__id_personaje

    @property # ------------------------------------->>
    def habilidad(self) -> int:
        return self.__id_habilidad


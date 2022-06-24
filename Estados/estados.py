class estados:
    def __init__(self,id_estado,nombre,descripcion):
        self.__id_estado = id_estado
        self.__nombre = nombre
        self.__descripcion = descripcion

    @property # ------------------------------------->>
    def id(self) -> int:
        return self.__id_estado

    @property # ------------------------------------->>
    def nombre(self) -> str:
        return self.__nombre

    @property # ------------------------------------->>
    def descripcion(self) -> str:
        return self.__descripcion
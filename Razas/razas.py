class razas:
    def __init__(self,id_raza,nombre,fuerza,destreza,resistencia,detalle,habilidad,poder):
        self.__id_raza = id_raza
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__destreza = destreza
        self.__resistencia = resistencia
        self.__detalle = detalle
        self.__habilidad = habilidad
        self.__poder = poder

    @property # ------------------------------------->>
    def id(self) -> str:
        return self.__id_raza

    @property # ------------------------------------->>
    def nombre(self) -> str:
        return self.__nombre

    @property # ------------------------------------->>
    def fuerza(self) -> str:
        return self.__fuerza

    @property # ------------------------------------->>
    def destreza(self) -> str:
        return self.__destreza

    @property # ------------------------------------->>
    def resistencia(self) -> str:
        return self.__resistencia

    @property # ------------------------------------->>
    def detalle(self) -> str:
        return self.__detalle

    @property # ------------------------------------->>
    def habilidad(self) -> str:
        return self.__habilidad

    @property # ------------------------------------->>
    def poder(self) -> str:
        return self.__poder
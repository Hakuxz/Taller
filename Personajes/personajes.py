class razas:
    def __init__(self,id_pj,nombre,estado,nivel,inteligencia,sabiduria,carisma,experiencia,fuerza,destreza,resistencia):
        self.__id_pj = id_pj
        self.__nombre = nombre
        self.__estado = estado
        self.__nivel = nivel
        self.__inteligencia = inteligencia
        self.__sabiduria = sabiduria
        self.__carisma = carisma
        self.__experiencia = experiencia
        self.__fuerza = fuerza
        self.__destreza = destreza
        self.__resistencia = resistencia

    @property # ------------------------------------->>
    def id(self) -> str:
        return self.__id_pj

    @property # ------------------------------------->>
    def nombre(self) -> str:
        return self.__nombre

    @property # ------------------------------------->>
    def estado(self) -> str:
        return self.__estado

    @property # ------------------------------------->>
    def nivel(self) -> str:
        return self.__nivel

    @property # ------------------------------------->>
    def inteligencia(self) -> str:
        return self.__inteligencia

    @property # ------------------------------------->>
    def sabiduria(self) -> str:
        return self.__sabiduria

    @property # ------------------------------------->>
    def carisma(self) -> str:
        return self.__carisma

    @property # ------------------------------------->>
    def experiencia(self) -> str:
        return self.__experiencia

    @property # ------------------------------------->>
    def fuerza(self) -> str:
        return self.__fuerza

    @property # ------------------------------------->>
    def destreza(self) -> str:
        return self.__destreza

    @property # ------------------------------------->>
    def resistencia(self) -> str:
        return self.__resistencia
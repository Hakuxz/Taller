class personajes:
    def __init__(self,id_pj,nombre,estado,nivel,inteligencia,sabiduria,carisma,experiencia,fuerza,destreza,resistencia,id_jugador,equipo,raza):
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
        self.__id_jugador = id_jugador
        self.__equipo = equipo
        self.__raza = raza

    @property # ------------------------------------->>
    def id(self) -> int:
        return self.__id_pj

    @property # ------------------------------------->>
    def nombre(self) -> str:
        return self.__nombre

    @property # ------------------------------------->>
    def estado(self) -> int:
        return self.__estado

    @property # ------------------------------------->>
    def nivel(self) -> int:
        return self.__nivel

    @property # ------------------------------------->>
    def inteligencia(self) -> int:
        return self.__inteligencia

    @property # ------------------------------------->>
    def sabiduria(self) -> int:
        return self.__sabiduria

    @property # ------------------------------------->>
    def carisma(self) -> int:
        return self.__carisma

    @property # ------------------------------------->>
    def experiencia(self) -> int:
        return self.__experiencia

    @property # ------------------------------------->>
    def fuerza(self) -> int:
        return self.__fuerza

    @property # ------------------------------------->>
    def destreza(self) -> int:
        return self.__destreza

    @property # ------------------------------------->>
    def resistencia(self) -> int:
        return self.__resistencia

    @property # ------------------------------------->>
    def id_jugador(self) -> int:
        return self.__id_jugador

    @property # ------------------------------------->>
    def equipo(self) -> int:
        return self.__equipo

    @property # ------------------------------------->>
    def raza(self) -> int:
        return self.__raza

import cx_Oracle

class coneccion:
    connection = None
    cursor = None

    @classmethod
    def getStartConnection(cls):
        cx_Oracle.init_oracle_client(lib_dir=r"C:/lib_client")
        connect = cx_Oracle.connect(user="felipe", password="TallerSistemas2022", dsn="tallerdesarrollovespertino_high")
        cls.cursor = connect.cursor()
        cls.connection = connect

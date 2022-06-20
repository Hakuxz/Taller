<<<<<<< HEAD
import cx_Oracle

class coneccion:
    connection = None
    cursor = None

    @classmethod
    def getStartConnection(cls):
        cx_Oracle.init_oracle_client(lib_dir=r"C:/lib_client")
        #connect = cx_Oracle.connect(user="felipe", password="TallerSistemas2022", dsn="tallerdesarrollovespertino_high")
        connect = cx_Oracle.connect(user='admin',password='Pass Taller.2022',dsn='dbeva2tallerap_high')
        cls.cursor = connect.cursor()
        cls.connection = connect
=======
import cx_Oracle

class coneccion:
    connection = None
    cursor = None

    @classmethod
    def getStartConnection(cls):
        cx_Oracle.init_oracle_client(lib_dir=r"C:/lib_client")
        #connect = cx_Oracle.connect(user="felipe", password="TallerSistemas2022", dsn="tallerdesarrollovespertino_high")
        connect = cx_Oracle.connect(user='admin',password='Pass Taller.2022',dsn='dbeva2tallerap_high')
        cls.cursor = connect.cursor()
        cls.connection = connect
>>>>>>> 6a1aa426e26295b2e64db0e0d0ccef8adcf8fef4

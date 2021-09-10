import dataexpansion.sql_class

class MySQL_Ex(dataexpansion.sql_class.SQL_ABC) :
    DataBaseHost = str()
    DataBaseUser = str()
    DataBasePass = str()
    def __init__(self) -> None:
        super().__init__()
    pass
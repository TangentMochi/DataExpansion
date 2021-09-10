
class SQL_ABC :
    DataField = dict()
    DataBasePass = str()
    DataBaseEncr = bool

    def __init__(self, option : dict) -> None:
        if option in 'encr':
            self.DataBaseEncr = True
        elif option in 'encryption':
            self.DataBaseEncr = True
        else :
            self.DataBaseEncr = False
        

    #overwrite
    def sql_create_table(self, name : str, option : dict) -> int:
        return -1

    #overwrite
    def sql_create_data(self) -> int:
        return -1

    
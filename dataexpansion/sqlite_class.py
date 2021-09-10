import dataexpansion.sql_class

class SQLite_Ex(dataexpansion.sql_class.SQL_ABC) :
    def __init__(self, **option) -> None:
        super().__init__(option)
        
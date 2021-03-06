class TablaSimbolos:
    'Clase abstracta'

class TableData(TablaSimbolos):
    def __init__(self, database, table, name, type, size, pk, fk, default, null, unique, check):
        self.database = database
        self.table = table
        self.name = name
        self.type = type
        self.size = size
        self.pk = pk
        self.fk = fk
        self.default = default
        self.null = null
        self.check = check
        self.unique = unique

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)

class DatabaseData(TablaSimbolos):
        def __init__(self, name, owner, mode, use):
            self.name = name
            self.owner = owner
            self.use = use

        def execute(self):
            return self

        def __repr__(self):
            return str(self.__dict__)

class EnumData(TablaSimbolos):
        def __init__(self, name, val, database):
            self.name = name
            self.owner = owner
            self.use = use

        def execute(self):
            return self

        def __repr__(self):
            return str(self.__dict__)

class ConstraintData(TablaSimbolos):
        def __init__(self, name, val):
            self.name = name
            self.val = val

        def execute(self):
            return self

        def __repr__(self):
            return str(self.__dict__)

#
from mathtrig import *
#


class query():
    ' Clase abstracta query'


class select(query):

    def __init__(self, distinct=False, select_list=[], table_expression=[], condition=[], group=False, having=[], orderby=[], orderAscDesc='F', limit=0, offset=0):
        self.distinct = distinct
        self.select_list = select_list
        self.table_expression = table_expression
        self.condition = condition
        self.group = group
        self.having = having
        self.orderby = orderby
        self.orderascdesc = orderAscDesc
        self.limit = limit
        self.offset = offset


class exp_query():
    'Abstract Class'


class exp_id(exp_query):
    'Esta expresion devuelve'
    'el arreglo de la base de datos'

    def __init__(self, val, table):
        self.val = val
        self.table = table


class exp_bool(exp_query):
    'Esta expresion devuelve un'
    'boolean'

    def __init__(self, val):
        self.val = val


class exp_text(exp_query):
    'Devuelve el texto'

    def __init__(self, val):
        self.val = val


class exp_int(exp_query):
    'Devuelve un entero'

    def __init__(self, val):
        self.val = val


class exp_dec(exp_query):
    'Devuelve un flotante'

    def __init__(self, val):
        self.val = val


class exp_suma(exp_query):
    'Suma las dos expresiones'

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2


class exp_resta(exp_query):
    'Suma las dos expresiones'

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2


class exp_multiplicacion(exp_query):
    'Suma las dos expresiones'

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2


class exp_division(exp_query):
    'Suma las dos expresiones'

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2


class select_column():
    'Abstract Class'


class column_id(select_column):
    def __init__(self, id, table, alias):
        self.id = id
        self. table = table
        self.alias = alias


class column_mathtrig(select_column):
    'Abstract Class'


class math_abs(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class math_cbrt(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class math_ceil(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class math_degrees(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class math_div(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias


class math_factorial(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class math_floor(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class math_gcd(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias


class math_ln(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class math_log(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias


class math_log10(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class math_mod(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class math_pi(column_mathtrig):
    def __init__(self, alias):
        self.val = pi()
        self.alias = alias


class math_power(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias


class math_radians(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class math_round(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class math_sign(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class math_sqrt(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class math_widthBucket(column_mathtrig):
    def __init__(self, exp1, exp2, exp3, exp4, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.exp4 = exp4
        self.alias = alias


class math_trunc(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class math_random(column_mathtrig):
    def __init__(self, alias):
        self.alias = alias


class trig_acos(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class trig_acosd(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class trig_asin(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class trig_asind(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class trig_atan(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class trig_atand(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class trig_atan2(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias


class trig_atan2d(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp = exp1
        self.exp2 = exp2
        self.alias = alias


class trig_cos(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class trig_cosd(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class trig_cot(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class trig_cotd(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class trig_sin(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class trig_sind(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


class trig_tan(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

class trig_tand(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

class trig_sinh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

class trig_cosh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

class trig_tanh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

class trig_asinh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

class trig_acosh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

class trig_atanh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

class column_function(select_column):
    'clase Abstracta'

class fun_length(column_function):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

class fun_substring(column_function):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

class fun_trim(column_function):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

class fun_md5(column_function):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

class fun_sha256(column_function):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

class fun_substr(column_function):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

class fun_convert(column_function):
    def __init__ (self,exp,type,alias):
        self.exp = exp
        self.type = type
        self.alias = alias

class fun_greatest(column_function):
    def __init__ (self,lexps,alias):
        self.lexps = lexps
        self.alias = alias

class fun_least(column_function):
    def __init__ (self,lexps,alias):
        self.lexps = lexps
        self.alias = alias
        
from .validate_func import *
from .from_to import *
from .treat_database import *

def log(name, type, value): #log
    print('name: %s, type: %s, value: %s' % (name, type, value))

#validade e formatação ---------------------------------------------
def apply_validade(df_temp,column) : 
    for c in column:
        name = c.name
        if name not in df_temp.columns:
            raise HTTPException(406,detail=f"Coluna '{name}' não encontrada.")
        type = c.type
        scale = c.scale
        zfill = c.zfill
        regex = c.regex
        cut = c.cut
        case_txt = c.case_txt
        valcut = c.valcut
        regex_index = c.regex_index
        
        df_temp = format_check(df_temp,name,zfill,regex,regex_index,cut,case_txt,valcut)
        df_temp = type_check(df_temp,name,type,scale)

    return df_temp
    
#---------------------------------------------------------------------
from .validate_format import *
import pandas as pd

def type_check(df_temp,name,type,scale):

    
    if type in ["str","string","texto","Texto"]:
        df_temp[name] = df_temp[name].astype(str)
        
    elif type in ["int","inteiro","integer","Inteiro"]:
        df_temp[name] = pd.to_numeric(df_temp[name]) 

    elif type in ["date","data","datetime.date","Data"]:
        df_temp[name] = pd.to_datetime(df_temp[name], errors='ignore')

    elif type in ["bool","boolean", "booleano","Booleano"]: 
        df_temp[name] = df_temp[name].convert_dtypes(convert_boolean = True)

    elif type in ["float","decimal.Decimal","real","Real"]:
        df_temp[name] = df_temp[name].convert_dtypes(convert_floating = True)
        df_temp[name] = format_num(scale,name,df_temp)

    else:
        raise HTTPException(406, detail=f"O tipo '{type}' da coluna '{name}' é inválido")
    
    return df_temp



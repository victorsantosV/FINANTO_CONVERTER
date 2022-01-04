import re
import pandas as pd
from imports.imports import invalid_list,split_from_list
from fastapi import HTTPException

def bd_treat(arquivo,unnamed,deleta_coluna):
    bd = arquivo[arquivo.columns.drop(arquivo.filter(regex=unnamed))]
    bd = delete_col(deleta_coluna,bd) 
    bd = date_format(bd)
    return bd

def date_format(bd):
    for name in bd.columns:
        if bd[name].dtype == '<M8[ns]' or bd[name].dtype == 'datetime64[ns]':
            bd[name] = pd.to_datetime(bd[name]).dt.date
    return bd

def delete_col(delete_c,df_temp):
    if delete_c not in invalid_list:
        try:    
            for dc in delete_c:
                dc = re.split(split_from_list,dc)
            for i in dc:
                df_temp = df_temp.drop(columns=[i])
        except BaseException as e:
            print(e)
            raise HTTPException(406,detail=f"Não encontrado valor: '{i}'")
    return df_temp

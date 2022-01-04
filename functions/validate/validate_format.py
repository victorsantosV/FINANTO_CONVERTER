import pandas as pd
from fastapi import HTTPException
from .regex import *
from definitions.in_definitions import invalid_list

def format_num(scale,name,df_temp):   
    if scale not in invalid_list:
        df_temp[name] = df_temp[name].round(scale).astype(float)
    else:
        df_temp[name] = pd.to_numeric(df_temp[name], downcast= "float")
    return df_temp

def format_check(df_temp,name,zfill,regex,regex_index,cut,case_txt,valuecut):
    
    if regex not in invalid_list and regex_index not in invalid_list: 
        try:
            regex_index = int(regex_index)
            regex = regex_func(regex)
            df_temp[name] = df_temp[name].astype(str)
            df_temp[name] = df_temp[name].str.extract(regex)[regex_index]
        except BaseException as e:
            print(e)
            raise HTTPException(406, detail=f"Erro ao aplicar regex '{regex}' em '{name}', capturando indice '{regex_index}'.")

    if zfill not in invalid_list:   
        try:
            zfill = int(zfill)
            df_temp[name] = df_temp[name].astype(str)
            df_temp[name] = df_temp[name].str.zfill(zfill)
        except BaseException as e:
            print(e)
            raise HTTPException(406, detail=f"Erro ao preencher '{name}' com zeros utilizando o valor: '{zfill}'.")
    
    if cut not in invalid_list:
        try:

            df_temp[name] = df_temp[name].astype(str)

            if cut in ["strip","Cortar caractere geral"]:
                df_temp[name] = df_temp[name].str.strip(valuecut)   

            elif cut in ["lstrip","Cortar caractere a esquerda"]:
                df_temp[name] = df_temp[name].str.lstrip(valuecut) 
                
            elif cut in ["rstrip","Cortar caractere a direita"]:
                df_temp[name] = df_temp[name].str.rstrip(valuecut) 

        except BaseException as e:
            print(e)
            raise HTTPException(406, detail=f"Erro ao cortar '{valuecut}' de forma '{cut}'.")
    
    if case_txt not in invalid_list:
        try:
            if case_txt in ["upper","Caixa Alta"]:
                if name not in invalid_list:
                    df_temp[name] = df_temp[name].astype(str)
                    df_temp[name] = df_temp[name].str.upper()
                else:
                    for i in df_temp.columns:
                        df_temp[i] = df_temp[i].astype(str)
                        df_temp[i] = df_temp[i].str.upper()

            if case_txt in ["lower","Caixa Baixa"]:
                if name not in invalid_list:
                    df_temp[name] = df_temp[name].astype(str)
                    df_temp[name] = df_temp[name].str.lower()
                else:
                    for i in df_temp.columns:
                        df_temp[i] = df_temp[i].astype(str)
                        df_temp[i] = df_temp[i].str.lower()

            elif case_txt in ["capitalize","Caixa alta pra primeira letra da primeira palavra"]:
                if name not in invalid_list:
                    df_temp[name] = df_temp[name].astype(str)
                    df_temp[name] = df_temp[name].str.capitalize()
                else:
                    for i in df_temp.columns:
                        df_temp[i] = df_temp[i].astype(str)
                        df_temp[i] = df_temp[i].str.capitalize() 

            elif case_txt in ["swapcase","Inverte a caixa"]:
                if name not in invalid_list:
                    df_temp[name] = df_temp[name].astype(str)
                    df_temp[name] = df_temp[name].str.swapcase()   
                else:
                    for i in df_temp.columns:
                        df_temp[i] = df_temp[i].astype(str)
                        df_temp[i] = df_temp[i].str.swapcase()  

            elif case_txt in ["title","Caixa alta pra primeira letra de todas as palavras"]:
                if name not in invalid_list:
                    df_temp[name] = df_temp[name].astype(str)
                    df_temp[name] = df_temp[name].str.title()    
                else:
                    for i in df_temp.columns:
                        df_temp[i] = df_temp[i].astype(str)
                        df_temp[i] = df_temp[i].str.title()  
        except BaseException as e:
            print(e)
            raise HTTPException(406, detail=f"Erro ao aplicar formatação '{case_txt}' ao valor '{name}'.")                    
            

    return df_temp

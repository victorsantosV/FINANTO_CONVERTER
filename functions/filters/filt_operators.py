from fastapi.exceptions import HTTPException
from pandas import merge
from definitions.in_definitions import invalid_list

def op_check(i,op_or,op_and,df_t,op,df_temp,name,val):  
    try:
        if op in ['gt','>','maior']:

            if op_or not in invalid_list: 
                if i == 0: 
                    df_temp = df_temp[df_temp[name] > val]  
                else:
                    df_y = df_temp
                    df_temp = df_temp.merge(df_t,how="outer")
                    df_temp = df_temp[df_temp[name] > val]
                    df = merge(df_temp,df_y,how="outer")
                    df_temp = df

            elif op_and not in invalid_list:
                df_temp = df_temp[df_temp[name] > val]
            return df_temp

        elif op in ['lt','<','menor']:
            if op_or not in invalid_list:
                if i == 0:
                    df_temp = df_temp[df_temp[name] < val]
                else:
                    df_y = df_temp
                    df_temp = df_temp.merge(df_t,how="outer")
                    df_temp = df_temp[df_temp[name] < val]
                    df = merge(df_temp,df_y,how="outer")
                    df_temp = df

            elif op_and not in invalid_list:
                df_temp = df_temp[df_temp[name] < val]
                
            return df_temp

        elif op in ['==','eq','=','igual']:
            if op_or not in invalid_list:
                if i == 0:
                    df_temp = df_temp[df_temp[name] == val]
                else:
                    df_y = df_temp
                    df_temp = df_temp.merge(df_t,how="outer")
                    df_temp = df_temp[df_temp[name] == val]
                    df = merge(df_temp,df_y,how="outer")
                    df_temp = df
            elif op_and not in invalid_list:
                df_temp = df_temp[df_temp[name] == val]
            return df_temp
            
        elif op in ['neq','!=','diferente','não equivalente']:
            if op_or not in invalid_list:
                if i == 0:
                    df_temp = df_temp[df_temp[name] != val]
                else:
                    df_y = df_temp
                    df_temp = df_temp.merge(df_t,how="outer")
                    df_temp = df_temp[df_temp[name] != val]
                    df = merge(df_temp,df_y,how="outer")
                    df_temp = df

            elif op_and not in invalid_list:
                df_temp = df_temp[df_temp[name] != val]
                
            return df_temp

        elif op in ['gte','>=','maior ou igual']:
            if op_or not in invalid_list:
                if i == 0:
                    df_temp = df_temp[df_temp[name] >= val]
                else:
                    df_y = df_temp
                    df_temp = df_temp.merge(df_t,how="outer")
                    df_temp = df_temp[df_temp[name] >= val]
                    df = merge(df_temp,df_y,how="outer")
                    df_temp = df
            elif op_and not in invalid_list:
                df_temp = df_temp[df_temp[name] >= val]
            return df_temp

        elif op in ['lte','<=','menor ou igual']:
            if op_or not in invalid_list:
                if i == 0:
                    df_temp = df_temp[df_temp[name] <= val]
                else:
                    df_y = df_temp
                    df_temp = df_temp.merge(df_t,how="outer")
                    df_temp = df_temp[df_temp[name] <= val]
                    df = merge(df_temp,df_y,how="outer")
                    df_temp = df        
            elif op_and not in invalid_list:
                df_temp = df_temp[df_temp[name] <= val]
            return df_temp

        elif op in ['lk','like','contains','possui', 'contêm']:
            if op_or not in invalid_list:
                if i == 0:
                    df_temp = df_temp[df_temp[name].str.contains(val)]
                else:
                    df_y = df_temp
                    df_temp = df_temp.merge(df_t,how="outer")
                    df_temp = df_temp[df_temp[name].str.contains(val)]
                    df = merge(df_temp,df_y,how="outer")
                    df_temp = df  
            elif op_and not in invalid_list:
                df_temp = df_temp[df_temp[name].str.contains(val)] 
            return df_temp

        elif op in ['nlk','nlike','not like','not contains','não possui', 'não contêm']:
            if op_or not in invalid_list:
                if i == 0:
                    df_temp = df_temp[~df_temp[name].str.contains(val)]
                else:
                    df_y = df_temp
                    df_temp = df_temp.merge(df_t,how="outer")
                    df_temp = df_temp[~df_temp[name].str.contains(val)]
                    df = merge(df_temp,df_y,how="outer")
                    df_temp = df          
            elif op_and not in invalid_list:
                df_temp = df_temp[~df_temp[name].str.contains(val)]
            return df_temp

        elif op in ['ls','like start','sw','startswith','possui no começo', 'começa com']:
            if op_or not in invalid_list:
                if i == 0:
                    df_temp = df_temp[df_temp[name].str.startswith(val)]
                else:
                    df_y = df_temp
                    df_temp = df_temp.merge(df_t,how="outer")
                    df_temp = df_temp[df_temp[name].str.startswith(val)]
                    df = merge(df_temp,df_y,how="outer")
                    df_temp = df           
            elif op_and not in invalid_list:
                df_temp = df_temp[df_temp[name].str.startswith(val)]    
            return df_temp

        elif op in ['nls','not like start','nsw','not startswith','não possui no começo', 'não começa com']:
            if op_or not in invalid_list:
                if i == 0:
                    df_temp = df_temp[~df_temp[name].str.startswith(val)]
                else:
                    df_y = df_temp
                    df_temp = df_temp.merge(df_t,how="outer")
                    df_temp = df_temp[~df_temp[name].str.startswith(val)]
                    df = merge(df_temp,df_y,how="outer")
                    df_temp = df     
            elif op_and not in invalid_list:
                df_temp = df_temp[~df_temp[name].str.startswith(val)]    
            return df_temp

        elif op in ['le','like end','ew','endswith','possui no final', 'termina com']:
            if op_or not in invalid_list:
                if i == 0:
                    df_temp = df_temp[df_temp[name].str.endswith(val)]
                else:
                    df_y = df_temp
                    df_temp = df_temp.merge(df_t,how="outer")
                    df_temp = df_temp[df_temp[name].str.endswith(val)]
                    df = merge(df_temp,df_y,how="outer")
                    df_temp = df  
            elif op_and not in invalid_list:
                df_temp = df_temp[df_temp[name].str.endswith(val)]    
            return df_temp

        elif op in ['nle','not like end','new','not endswith','não possui no final', 'não termina com']:
            if op_or not in invalid_list:
                if i == 0:
                    df_temp = df_temp[~df_temp[name].str.endswith(val)]
                else:
                    df_y = df_temp
                    df_temp = df_temp.merge(df_t,how="outer")
                    df_temp = df_temp[~df_temp[name].str.endswith(val)]
                    df = merge(df_temp,df_y,how="outer")
                    df_temp = df  
            elif op_and not in invalid_list:  
                df_temp = df_temp[~df_temp[name].str.endswith(val)]    
            return df_temp
    except BaseException as e:
        print(e)
        raise HTTPException(406,f"Erro ao filtrar: '{name} {op} {val}'")
    return df_temp

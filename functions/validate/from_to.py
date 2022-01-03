import pandas as pd
from fastapi import HTTPException
from definitions.in_definitions import invalid_list

def rename_df(extract,df_temp):
    df = pd.DataFrame()
    dlt = []
    for e in extract:
        try:
            from_to = e.from_to 
            if from_to not in invalid_list: 
                for fto in from_to:
                    for f,t in fto.items():
                        df = pd.concat([df,df_temp[f]],axis=1)
                        dlt.append(f)
                        try:
                            df.rename({f:t}, axis = 1, inplace = True)
                        except BaseException as e:
                            print(e)
                            raise HTTPException(406,detail=f"Erro ao renomear: '{f}' -> '{t}'")
        except BaseException as e:
            print(e)
            raise HTTPException(406,detail=f"Erro ao renomear: '{f}' -> '{t}'")
            
    for i in dlt:
        df_temp = df_temp.drop(columns=[i],errors = "ignore")
    df_temp = pd.concat([df_temp,df],axis=1)
    return df_temp

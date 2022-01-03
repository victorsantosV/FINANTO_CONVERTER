from fastapi import HTTPException

def sl_row(df_temp,return_options):
    for ro in return_options:
        how = ro.how
        rows = ro.rows
        rowmax = ro.rowmax
        
        if how == "head" and rows not in [0,None]:
            df_temp = df_temp.head(rows)
        elif how == "head" and rows in [0,None]:
            df_temp = df_temp.head()
        
        elif how == "tail" and rows not in [0,None]:
            df_temp = df_temp.tail(rows)
        elif how == "tail" and rows in [0,None]:
            df_temp = df_temp.tail()

        elif how == "loc" and rowmax not in [0,None]:
            if rowmax>=rows:
                df_temp = df_temp.loc[rows:rowmax,:]
            else:
                raise HTTPException(406,detail=f'{rowmax} menor que {rows}, o retorno será vazio.')
    return df_temp
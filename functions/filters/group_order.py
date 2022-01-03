import pandas as pd
from fastapi import HTTPException

def od_by(df_temp,name,srt): 
    if srt in ['asc','ASC','crescente','Crescente','CRESCENTE']:
        df_temp = df_temp.sort_values(by = name,ascending = True)
    elif srt in ['desc','DESC','decrescente','Decrescente','DECRESCENTE']:
        df_temp = df_temp.sort_values(by = name,ascending = False)
    else:
        raise HTTPException(406,detail=f"Erro ao ordenar '{name}' de maneira {srt}")

    return df_temp

def gby(gcolumns,gb,df_temp):   
    gr_oup = pd.DataFrame()
    col_list = []
    
    for b in gb:
        nameb = b.name
        if nameb not in df_temp.columns:
            raise HTTPException(406,detail=f"'{nameb}' não encontrado nas colunas.")
        grouper = df_temp.groupby(nameb)

        for g in gcolumns:
            namec = g.name
            col_list.append(namec)
            if namec not in df_temp.columns:
                raise HTTPException(406,detail=f"'{namec}' não encontrado nas colunas.")    
            how_gb = g.how_gp
            
            if how_gb in ["sum","SUM","Sum","SOMA","soma","Soma"]:
                gr_oup[namec] = grouper[namec].sum()
                
            elif how_gb in ["mean","MEAN","Mean","média","media","MEDIA","MÉDIA","Média","Media"]:
                gr_oup[namec] = grouper[namec].mean()

            elif how_gb in ["count","COUNT","Count","Contar","Contagem","CONTAR","CONTAGEM","contar","contagem"]:
                gr_oup[namec] = grouper[namec].count()

            elif how_gb in ["max","MAX","Max","Máximo","MÁXIMO","máximo","Maximo","MAXIMO","maximo"]:
                gr_oup[namec] = grouper[namec].max()
                
            elif how_gb in ["min","MIN","Min","Mínimo","MÍNIMO","mínimo","Minimo","Minimo","MINIMO"]:
                gr_oup[namec] = grouper[namec].min()
        
            else:
                raise HTTPException(406,detail='Agrupamento inválido')

        for i in gr_oup.columns:
            if i not in col_list:
                gr_oup = gr_oup.drop([i],axis = 1)

        df_temp = gr_oup


    if len(df_temp) == 0:
        raise HTTPException(406,detail='Agrupamento inválido.')

    return df_temp

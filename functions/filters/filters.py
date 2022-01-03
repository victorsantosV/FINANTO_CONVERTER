from pandas import merge
from fastapi import HTTPException
from .group_order import *
from .filt_operators import *
from definitions.in_definitions import invalid_list,split_from_list


def apply_filter(df_temp,filters):
    for f in filters:
        group = f.group
        order_by = f.order_by
        exp = f.expressions
        a = 0
        
        df_temp = filt_options(exp,df_temp)
        
        if group not in invalid_list:
            for g in group:
                gcolumns = g.group_columns
                gb = g.group_by
                df_temp = gby(gcolumns,gb,df_temp)

        if order_by not in invalid_list:
            for o in order_by: 
                name = o.name
                srt = o.sort
                df_temp = od_by(df_temp,name,srt)

        df_temp = df_temp.reset_index()
        df_temp = df_temp.drop('index', axis=1, errors='ignore')
        return df_temp

def filt_options(exp,df_temp):  
    for e in exp:
        df_t = df_temp
        i = 0  
        op_and = e.op_and 
        op_or = e.op_or
        slct = e.select

        if op_and not in invalid_list: 
            i = 0
            df_temp = df_t
            for op_a in op_and:
                op_ou = None
                name = op_a.name[0]
                op = op_a.op[0]     
                val = op_a.val[0]   
                df_temp = op_check(i,op_ou,op_a,df_t,op,df_temp,name,val)    
                
                if len(df_temp) == 0:
                    raise HTTPException(406,f"O filtro '{name} {op} {val}' retornou um resultado vazio.")
                
                for cl in df_temp[name]:
                    if val not in ['']:
                        df_temp = df_temp[df_temp[name] != '']                    

                df_and = df_temp 
                i = i + 1
            
        if op_or not in invalid_list: 
            i = 0
            df_temp = df_t
            for op_o in op_or:       
                op_e = None
                name = op_o.name[0]  
                op = op_o.op[0]      
                val = op_o.val[0]    
                df_temp = op_check(i,op_o,op_e,df_t,op,df_temp,name,val)
                
                if len(df_temp) == 0:
                    raise HTTPException(406,f"O filtro '{name} {op} {val}' retornou um resultado vazio.")

                for rw in df_temp[name]:
                    if val not in ['']:
                        df_temp = df_temp[df_temp[name] != '']   
                        
                df_or = df_temp
                i = i + 1
        
        if op_and not in invalid_list and op_or not in invalid_list:
            hw = e.how
            if hw in ["ou","or"]:
                df_temp = merge(df_and,df_or,how = "outer") 
            elif hw in ["e","and"]:
                df_temp = merge(df_and,df_or,how = "inner") 
            else:
                raise HTTPException(406,detail='Não encontrado valor or/and para agrupamento dos filtros.')
        
        try:
            if slct not in invalid_list:
                for sl in slct:
                    sl = sl.split(split_from_list)
                    df_temp = df_temp.loc[:,sl]
        except BaseException as e:
            print(e)
            raise HTTPException(406,detail=f"Erro ao selecionar as colunas {slct}. Certifique-se da existência de todas na tabela.")

        if len(df_temp) == 0:
            raise HTTPException(406,detail='Os filtros fizeram a tabela voltar vazia.')
    return df_temp


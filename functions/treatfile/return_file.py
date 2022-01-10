from functions.treatfile.create import cria_pasta, zip_and_remove
from definitions.in_definitions import Post_fs,Salvamento
from .div_rows import *
from fastapi import HTTPException
import pandas as pd  

def return_file(nome_do_arquivo,zip_format,formato_do_arquivo,bd,numero_de_linhas_do_arquivo,modo_salvamento,pasta_arquivos,sheet_nme):
    namedir = f'{nome_do_arquivo}.{zip_format}'
    nome_arquivo = f'{nome_do_arquivo}.{formato_do_arquivo}'
    arq = []
    if formato_do_arquivo == Post_fs.xlsx:
        idx = 0
        arq = div_col(bd,arq,numero_de_linhas_do_arquivo)

        if modo_salvamento == Salvamento.varios_arquivos:
            if arq in [None,'',[]]:
                raise HTTPException(406, detail='Não encontrado número de linhas por arquivo.')            
            cria_pasta(namedir)            
            for i in arq:
                arq[idx].to_excel(f'{namedir}/{nome_do_arquivo}_{idx+1}.{formato_do_arquivo}')
                idx = idx + 1 
            zip_and_remove(pasta_arquivos,nome_do_arquivo,zip_format,formato_do_arquivo,namedir)
            file = f'{pasta_arquivos}/{nome_arquivo}.{zip_format}'
            return file
            
        elif modo_salvamento == Salvamento.uma_pagina:
            cria_pasta(namedir)
            bd.to_excel(f'{namedir}/{nome_do_arquivo}.{formato_do_arquivo}')
            zip_and_remove(pasta_arquivos,nome_do_arquivo,zip_format,formato_do_arquivo,namedir)
            file = f'{pasta_arquivos}/{nome_arquivo}.{zip_format}'
            return file
        
        elif modo_salvamento == Salvamento.varias_paginas:
            if arq in [None,'',[]]:
                raise HTTPException(406, detail='Não encontrado número de linhas por arquivo.')
            cria_pasta(namedir)
            with pd.ExcelWriter(f'{namedir}/{nome_do_arquivo}.{formato_do_arquivo}') as writer:  
                for i in arq:
                    arq[idx].to_excel(writer, sheet_name=f'{sheet_nme}{idx+1}')
                    idx = idx + 1 
            zip_and_remove(pasta_arquivos,nome_do_arquivo,zip_format,formato_do_arquivo,namedir)
            file = f'{pasta_arquivos}/{nome_arquivo}.{zip_format}'
            return file

    if formato_do_arquivo == Post_fs.csv:
        cria_pasta(namedir)       
        bd.to_csv(f'{namedir}/{nome_do_arquivo}.{formato_do_arquivo}')
        zip_and_remove(pasta_arquivos,nome_do_arquivo,zip_format,formato_do_arquivo,namedir)
        file = f'{pasta_arquivos}/{nome_arquivo}.{zip_format}'
        return file

    if formato_do_arquivo == Post_fs.json:
        cria_pasta(namedir)       
        bd.to_json(f'{namedir}/{nome_do_arquivo}.{formato_do_arquivo}')
        zip_and_remove(pasta_arquivos,nome_do_arquivo,zip_format,formato_do_arquivo,namedir)
        file = f'{pasta_arquivos}/{nome_arquivo}.{zip_format}'
        return file
    else:
        raise HTTPException(406,detail='Não encontrado o formato de saída.')


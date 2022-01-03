from definitions.in_definitions import invalid_list,invalid_list_int,ctype_csv,ctype_json,ctype_xlsx,ctype_html,utf,default_value
from io import StringIO
import pandas as pd
from fastapi import HTTPException

def read_arq(df,file_binary,link,type_content,indice_html):
    if type_content not in invalid_list:
        if type_content in ctype_xlsx:            
            try:
                df = pd.concat(pd.read_excel(file_binary, sheet_name=default_value), ignore_index=True)
            except BaseException as e:
                print(e)
                raise HTTPException(406, detail='Dados de arquivo inválidos')

        elif type_content in ctype_csv:
            try:
                df = pd.read_csv(StringIO(str(file_binary, utf)), encoding=utf)
            except BaseException as e:
                print(e)
                raise HTTPException(406, detail='Dados de arquivo inválidos')
        
        elif type_content in ctype_json:
            try:
                df = pd.read_json(file_binary)
            except BaseException as e:
                print(e)
                raise HTTPException(406, detail='Dados de arquivo inválidos')

        elif type_content in ctype_html:
            try:
                df = pd.read_html(file_binary)
                if indice_html != None:
                    df = df[indice_html]
                elif indice_html in invalid_list_int:
                    raise HTTPException(406, detail='Insira o indice da tabela do site.')
            except BaseException as e:
                print(e)
                raise HTTPException(406, detail='Dados de arquivo inválidos.')

    elif link not in invalid_list:
        try:
            df = pd.read_html(link)
        except BaseException as e:
            print(e)
            raise HTTPException(406, detail='Nenhuma tabela foi encontrada no link.')
        try:
            if indice_html != None:
                df = df[indice_html]
        except BaseException as e:
            print(e)
            raise HTTPException(406, detail='Índice fora do alcance da lista.')
    else:
        raise HTTPException(415,detail='Arquivo inválido ou não encontrado.')
    
    return df



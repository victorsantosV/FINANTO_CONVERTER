import shutil 
import os
from fastapi import HTTPException

def clear_all(base_dados,guarda_arquivo,slct,filter_and,filter_or,gcol,gb,grp,order,exp,modelo):
    base_dados.clear()
    guarda_arquivo.clear()
    slct.clear()
    filter_and.clear()
    filter_or.clear()
    gcol.clear()
    gb.clear()
    grp.clear()
    order.clear()
    exp.clear()
    modelo.clear()

def create_dict(arquivo):
    return arquivo.to_dict(orient="records")

def cria_pasta(namedir):
    if os.path.isdir(namedir):
        try:
            os.rmdir(namedir)
            os.mkdir(namedir)
        except:
            for f in os.listdir(namedir):
                os.remove(os.path.join(namedir, f))
            os.rmdir(namedir)
            os.mkdir(namedir)
    else:
        os.mkdir(namedir)

def zip_and_remove(pasta_arquivos,nome_saida,zip_format,formato_saida,namedir): 
    try:
        shutil.make_archive(f'{pasta_arquivos}/{nome_saida}.{formato_saida}', zip_format, namedir)
    
    except BaseException as e:
        print(e)
        raise HTTPException(500, detail=f"Erro ao compactar '{nome_saida}.{formato_saida}' no formato {zip_format}.")

    for f in os.listdir(namedir):
        os.remove(os.path.join(namedir, f))
    os.rmdir(namedir)
    
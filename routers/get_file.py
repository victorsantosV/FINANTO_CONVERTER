from imports.imports import *

@router.get(get_all)
def get_file(current_user: User = Depends(get_current_active_user)):
    try:
        if guarda_arquivo not in invalid_list:
            for file in guarda_arquivo:
                return FileResponse(path=file,filename=file,media_type=zip_format)
    except BaseException as e:
        print(e)
        raise HTTPException(307,detail='Erro ao fazer download do arquivo.')
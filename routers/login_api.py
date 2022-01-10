from .imports import *

login_token = []

@router.post(post_lg)
async def login_api(username: str = Header(...),password: str = Header(...)):
    login_token.clear()
    token = get_tok(username,password)
    login_token.append(token)
    return login_token
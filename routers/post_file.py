from imports.imports import *
from .login_api import login_token

@router.post(post_md)
async def post_file(
    file: UploadFile = File(default_value),
    token: str = Header(...),
    link: str = Body(default_value),
    nome_do_arquivo: str = Body(default_name_file),
    modo_salvamento: Salvamento = Body(Salvamento.varios_arquivos),
    numero_de_linhas_do_arquivo: int = Body(default_value),
    formato_do_arquivo: Post_fs = Body(Post_fs.xlsx),
    nome_a_renomear: List[str] = Body(default_value),
    novo_nome: List[str] = Body(default_value),
    deleta_coluna: List[str] = Body(default_value),
    colunas_selecionadas: List[str] = Body(default_value),
    junta_colunas_filtradas: How_join = Body(default_value),
    nome_operador_and: List[str] = Body(default_value),
    operador_and: List[str] = Body(default_value),
    valor_a_ser_filtrado_and: List[str] = Body(default_value),
    nome_operador_or: List[str] = Body(default_value),
    operador_or: List[str] = Body(default_value),
    valor_a_ser_filtrado_or: List[str] = Body(default_value),
    nome_da_coluna_indice_para_ordenar: List[str] = Body(default_value),
    forma_de_ordenacao: Ob = Body(default_value),
    coluna_indice_de_agrupamento: str = Body(default_value),
    colunas_a_serem_agrupadas: List[str] = Body(default_value),
    forma_de_agrupamento: List[str] = Body(default_value),
    linhas_a_retornar: Hw = Body(default_value),
    qtde_linhas_ou_numero_da_pmeira_coluna_caso_loc: Optional[int] = Body(default_value_int),
    maximo_de_linhas_a_retornar_caso_loc: Optional[int] = Body(default_value),
    indice_tabela_caso_html: Optional[int] = Body(default_value),
    nome_coluna: List[str] = Body(default_value),
    tipo_coluna: List[str] = Body(default_value),
    preencher_com_zeros: List[str] = Body(default_value),
    numeros_apos_a_virgula: List[str] = Body(default_value),
    formatacao_da_coluna: List[str] = Body(default_value),
    cortar: List[str] = Body(default_value),
    valor_a_cortar: List[str] = Body(default_value),
    regex: List[str] = Body(default_value),
    regex_index: List[str] = Body(default_value)):

    for tk in login_token:
        if token == tk:
            token = token
        else:
            raise HTTPException(401,detail="Inautorizado.")

    clear_all(base_dados,guarda_arquivo,slct,filter_and,filter_or,gcol,gb,grp,order,exp,modelo)
    cria_pasta(pasta_arquivos)
    type_content = default_value
    file_binary = default_value

    if file not in invalid_list:
        type_content = file.content_type
        file_binary = await file.read()

    extct = post_exct(nome_a_renomear,novo_nome)
    colmns = post_clmns(nome_coluna,tipo_coluna,preencher_com_zeros,numeros_apos_a_virgula,formatacao_da_coluna,cortar,valor_a_cortar,regex,regex_index)
    filtrs = post_filter(colunas_selecionadas,junta_colunas_filtradas,nome_operador_and,operador_and,valor_a_ser_filtrado_and,nome_operador_or,operador_or,valor_a_ser_filtrado_or,nome_da_coluna_indice_para_ordenar,forma_de_ordenacao,colunas_a_serem_agrupadas,forma_de_agrupamento,coluna_indice_de_agrupamento)
    return_ot = slct_(linhas_a_retornar,qtde_linhas_ou_numero_da_pmeira_coluna_caso_loc,maximo_de_linhas_a_retornar_caso_loc)
    modelo.append(Model(type_content = type_content, extract = extct, return_options = return_ot,filters = filtrs, columns = colmns))     
    arquivo = use_model(file_binary,link, modelo,indice_tabela_caso_html)
    bd = bd_treat(arquivo,unnamed,deleta_coluna)
    bup = create_dict(bd)
    base_dados.append(bup)
            
    file = return_file(nome_do_arquivo,zip_format,formato_do_arquivo,bd,numero_de_linhas_do_arquivo,modo_salvamento,pasta_arquivos,sheet_nme)
    guarda_arquivo.append(file)
    return file
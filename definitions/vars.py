from fastapi import APIRouter

default_name_file = 'tabela'
pasta_arquivos = "arquivos"
post_lg = "/token"
post_md = '/'
get_all = '/'
zip_format = 'zip'
sheet_nme = 'pagina_'
unnamed = 'Unnamed'
ctype_json = ['application/json']
ctype_csv = ['text/csv','application/vnd.ms-excel']
ctype_xlsx = ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]
ctype_html = ['text/html']
utf = 'utf-8'
split_from_list = r"[\b]*,[\b]*(?!\s)"
base_dados = []
guarda_arquivo = []
default_value = None
default_value_int = 0
invalid_list = [None,'',[],False,[''],0,[{'':''}],'Nada','nada','NADA']
invalid_list_int = [None,'',[],False,[''],[{'':''}],'Nada','nada','NADA']
router = APIRouter()


colmns = []
extct = []
slct = []
return_ot = []
filter_and = []
filter_or = []
gcol = []
gb = []
grp = []
order = []
exp = []
filtrs = []
modelo = []

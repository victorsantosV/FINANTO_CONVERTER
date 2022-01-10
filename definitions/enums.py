from enum import Enum
  
class Salvamento(str,Enum):
    varios_arquivos = "Em vários arquivos."
    uma_pagina = "Em uma página em um só arquivo."
    varias_paginas = "Em várias páginas em um só arquivo."

class FmtText(str,Enum):
    upper = "Caixa Alta"
    lower = "Caixa Baixa"
    capitalize = "Caixa alta pra primeira letra da primeira palavra"
    swapcase = "Inverte a caixa" 
    title_txt = "Caixa alta pra primeira letra de todas as palavras"

class Post_fs(str,Enum):
    xlsx = "xlsx"
    json = "json"
    csv = "csv"

class Join_exp(str, Enum):
    inner = "inner"
    outer = "outer"
    left = "left"
    right = "right"

class How_join(str, Enum):
    e = "and"
    ou = "or"

class Op(str, Enum):
    gt = ">"
    lt = "<"
    eq = "="
    neq = "!=" 
    lk = "like"
    nlk = "not like"
    sw = "startswith"
    nsw = "not startswith"
    ew = "endswith"
    new = "not endswith"

class Hw(str, Enum):
    head = "head"
    tail = "tail"
    loc = "loc"

class TypesCol(str, Enum):
    string = "Texto"
    int = "Inteiro"
    float = "Real"
    date = "Data"
    bool = "Booleano" 

class Cut(str, Enum):
    strip = "Cortar caractere geral"
    lstrip = "Cortar caractere a esquerda"
    rstrip = "Cortar caractere a direita"

class Gb(str, Enum):
    sum = "sum"
    mean = "mean"      
    count = "count"

class Ob(str, Enum):
    desc = "DECRESCENTE"
    asc = "CRESCENTE"  

class Regex(str, Enum):
    reg1 = ""
    reg2 = "CPF"
    reg3 = "CNPJ"
    reg4 = "Data: 00/00/0000"
    reg5 = "Data: 0000/00/00"
    reg6 = "Modelo: 'Número - Texto'"
    reg7 = "Modelo: 'Texto - Texto'"
    reg8 = "Modelo: 'Texto, Texto'"
    reg9 = "Modelo: 'Texto: Texto'"
    reg10 = "Modelo: 'Número: Texto'"
    reg11 = "Modelo: 'Texto_Texto'"
    reg12 = "Modelo: 00.000000000-00"

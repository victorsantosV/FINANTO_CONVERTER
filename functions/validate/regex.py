from fastapi import HTTPException

def regex_func(regex):
    try:
        if regex == "CPF":
            rex = "(\d{3}\.\d{3}\.\d{3}\-\d{2})"

        elif regex == "CNPJ":
            rex = "(\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2})"

        elif regex == "Data: 00/00/0000":
            rex = "(\d{2}\/\d{2}\/\d{4})"

        elif regex == "Data: 0000/00/00":
            rex = "(\d{4}\/\d{2}\/\d{2})"

        elif regex == "Data: 00-00-0000":
            rex = "(\d{2}\-\d{2}\-\d{4})"

        elif regex == "Data: 0000-00-00":
            rex = "(\d{4}\-\d{2}\-\d{2})"

        elif regex == "Modelo: 'Número - Texto'":
            rex = "([0-9]*)\s-\s([A-z\s]*)"

        elif regex == "Modelo: 'Texto - Texto'":
            rex = "([A-z\s]*)\s-\s([A-z\s]*)"

        elif regex == "Modelo: 'Texto, Texto'":
            rex = "([0-9]*),\s([A-z\s]*)"

        elif regex == "Modelo: 'Texto: Texto'":
            rex = "([A-z\s]*):\s([A-z\s]*)"

        elif regex == "Modelo: 'Número: Texto'":
            rex = "([0-9]*):\s([A-z\s]*)"

        elif regex == "Modelo: 'Texto_Texto'":
            rex = "([0-9]*)_([A-z\s]*)"

        elif regex == "Modelo: 00.000000000-00":
            rex = "(\d{2}\.\d{9}\-\d{2})"

        else:
            rex = regex
            
        return rex
    except BaseException as e:
        print(e)
        raise HTTPException(406, detail='Regex inválido') 
    
    
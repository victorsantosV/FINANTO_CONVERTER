from definitions.in_definitions import invalid_list

def div_col(arquivo,arq,row_num):
    if row_num not in invalid_list:
        i = 0
        a = len(arquivo)
        b = 0
        while b < a:
            if i == 0 and b == 0:
                i = b
                b = b + row_num
                arq.append(arquivo[i:b])
            else:
                i = b
                b = b + row_num
                arq.append(arquivo[i:b]) 
        return arq
    else:
        return arq

from fastapi import HTTPException
from definitions.in_definitions import *

def post_clmns(name,type,preencher_com_zeros,numeros_apos_a_virgula,formatacao_da_coluna,cortar,valor_a_cortar,regex,regex_index):
    colmns = []
    lta = 0
    if name not in invalid_list:
        for n in name:
            n = n.split(split_from_list)
        for t in type:
            t = t.split(split_from_list)
        for pcz in preencher_com_zeros:
            pcz = pcz.split(split_from_list)
        for nav in numeros_apos_a_virgula:
            nav = nav.split(split_from_list)
        for fdc in formatacao_da_coluna:
            fdc = fdc.split(split_from_list)
        for c in cortar:
            c = c.split(split_from_list)
        for vac in valor_a_cortar:
            vac = vac.split(split_from_list)
        for r in regex:
            r = r.split(split_from_list)
        for ri in regex_index:
            ri = ri.split(split_from_list)

        for nm in n:
            colmns.append(Columns(name = n[lta],type = t[lta],zfill = pcz[lta],scale = nav[lta],case_txt = fdc[lta],cut = c[lta],valcut = vac[lta],regex = r[lta],regex_index = ri[lta]))
            lta = lta + 1
    return colmns

def post_filter(select,how_join,name_op_and,op_and,val_op_and,name_op_or,op_or,val_op_or,name_ob,sort_ob,name_gp,how_gp,name_gby):
    
    filter_and = []
    filter_or = []
    gcol = []
    gb = []
    grp = []
    order = []
    exp = []
    filtrs = []

    i = 0
    
    if name_op_and not in invalid_list:
        try:

            for nopand in name_op_and:
                nopand = nopand.split(split_from_list) 

            if op_and not in invalid_list:      
                for opand in op_and:
                    opand = opand.split(split_from_list)        
            else:
                raise HTTPException(406)

            if val_op_and not in invalid_list:
                for vopand in val_op_and:
                    vopand = vopand.split(split_from_list)
            else:
                raise HTTPException(406)

            for noa in nopand:
                filter_and.append(Filter_and(name = [nopand[i]],op = [opand[i]],val = [vopand[i]]))
                i = i + 1
        except BaseException as e:
            print(e)
            raise HTTPException(406,detail=f"Preencha todos os dados da coluna '{nopand[i]}', do filtro 'e' corretamente.")
    i = 0

    if name_op_or not in invalid_list:
        try:
            for nopor in name_op_or:
                nopor = nopor.split(split_from_list)

            if op_or not in invalid_list:      
                for opor in op_or:
                    opor = opor.split(split_from_list)        
            else:
                raise HTTPException(406)

            if val_op_or not in invalid_list:
                for vopor in val_op_or:
                    vopor = vopor.split(split_from_list)
            else:
                raise HTTPException(406)
            for nor in nopor:
                filter_or.append(Filter_or(name = [nopor[i]],op = [opor[i]],val = [vopor[i]]))
                i = i + 1
        except BaseException as e:
            print(e)
            raise HTTPException(406,detail=f"Preencha todos os dados da coluna '{nopor[i]}', do filtro 'ou' corretamente.")

    exp.append(Expressions(select = select, op_or = filter_or,how = how_join, op_and = filter_and))
    

    if name_gby not in invalid_list:
        gb.append(Group_by(name = name_gby))
    i = 0

    if name_gp not in invalid_list:
        try:
            for ngp in name_gp:
                ngp = ngp.split(split_from_list)
            for hgp in how_gp:
                hgp = hgp.split(split_from_list)
            for x in ngp:
                gcol.append(Group_col(name = ngp[i],how_gp = hgp[i]))
                i = i + 1
        except BaseException as e:
            print(e)
            raise HTTPException(406,detail='Preencha todos os dados do agrupamento corretamente.')

    grp.append(Group(group_by = gb,group_columns = gcol))
    
    if name_ob not in invalid_list: 
        try:
            for nob in name_ob:
                nob = nob.split(split_from_list)
            order.append(Order_by(name = nob,sort = sort_ob))   
        except BaseException as e:
            print(e)
            raise HTTPException(406,detail='Preencha todos os dados da ordenação corretamente.')

    filtrs.append(Filter(group = grp,order_by = order,expressions = exp))
    return filtrs

def slct_(how,rows,rowmax):
    slct = []
    if how != None:
        slct.append(Return_options(how = how, rows = rows, rowmax = rowmax))
    return slct

def post_exct(frm,to):
    extct = []
    lta = 0
    if frm != None:
        for f in frm:
            f = f.split(split_from_list)
        for t in to:
            t = t.split(split_from_list)
        for i in f:
            extct.append(ModelExtract(from_to = [{f"{f[lta]}":f"{t[lta]}"}]))
            lta = lta + 1
    return extct




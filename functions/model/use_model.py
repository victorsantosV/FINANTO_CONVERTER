from functions.filters.in_filters import sl_row,apply_filter
from functions.validate.validate import apply_validade,rename_df
from functions.treatfile.read_file import read_arq
from definitions.in_definitions import Model,invalid_list
import pandas as pd

def use_model(file_binary,link, modelo,indice_html):
    for b in modelo:
        mod = Model(type_content = b.type_content, extract = b.extract, return_options = b.return_options, filters = b.filters, columns = b.columns)
        extract = mod.extract
        return_options = mod.return_options
        filters = mod.filters
        columns = mod.columns
        type_content = mod.type_content
        df = pd.DataFrame()
        df = read_arq(df,file_binary,link,type_content,indice_html)
        df_temp = pd.DataFrame()
        df_temp = df.copy()

        if extract not in invalid_list:
            df_temp = rename_df(extract,df_temp)
        if columns not in invalid_list:
            df_temp = apply_validade(df_temp,columns)
        if filters not in invalid_list:
            df_temp = apply_filter(df_temp,filters)
        if return_options not in invalid_list:
            df_temp = sl_row(df_temp,return_options)

        
        r = df_temp
        return r
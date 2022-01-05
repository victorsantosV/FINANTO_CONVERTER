from pydantic import BaseModel
from typing import List, Optional, Union

class Login(str):
    username: str
    password: str

class Group_col(BaseModel):
    name: str
    how_gp: str

class Group_by(BaseModel):
    name: str

class Group(BaseModel):
    group_by: List[Group_by]
    group_columns: List[Group_col]

class Order_by(BaseModel):
    name: Optional[List[str]]
    sort: Optional[str]

class Filter_and(BaseModel):
    name: Optional[List[str]]
    op: Optional[List[str]]
    val: Optional[List[Union[int, float, str, bool]]]

class Filter_or(BaseModel):
    name: Optional[List[str]]
    op: Optional[List[str]]
    val: Optional[List[Union[int, float, str, bool]]]

class Expressions(BaseModel):
    select:  Optional[List[str]]
    op_or:  Optional[List[Filter_or]]
    how: Optional[str] 
    op_and:  Optional[List[Filter_and]]

class Filter(BaseModel):
    group: Optional[List[Group]]
    order_by: Optional[List[Order_by]]
    expressions: Optional[List[Expressions]]

class Return_options(BaseModel):
    how: Optional[str]
    rows: Optional[int]
    rowmax: Optional[int]

class ModelExtract(BaseModel):
    from_to: Optional[List[dict]]

class Columns(BaseModel):
    name: Optional[str]
    type: Optional[str]
    zfill: Optional[str]
    scale: Optional[str]
    case_txt: Optional[str] 
    cut: Optional[str]  
    valcut: Optional[str]
    regex: Optional[str]
    regex_index: Optional[str] 

class Model(BaseModel):
    type_content: Optional[str]
    extract: Optional[List[ModelExtract]]
    return_options: Optional[List[Return_options]] 
    filters: Optional[List[Filter]]
    columns: Optional[List[Columns]]



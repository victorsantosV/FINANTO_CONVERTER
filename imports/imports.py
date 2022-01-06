from fastapi import FastAPI, File,UploadFile,Body,HTTPException,APIRouter, Depends,status,Header
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from typing import List, Union
from definitions.in_definitions import *
from functions.in_functions import *
from security.auth import get_tok
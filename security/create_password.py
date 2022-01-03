def get_password_hash(pwd_context,password):
    return pwd_context.hash(password)
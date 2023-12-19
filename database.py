from sqlalchemy import create_engine, text

user = "root"
password = "root"
host = "localhost"
port = 3306
database = "base_datos_spotifinder"

def get_connection():
    connection = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    return create_engine(connection)


engine = get_connection()

def execute_query(string: str) -> list:
    with engine.connect() as connection:
        result = connection.execute(text(string))
        return result
            



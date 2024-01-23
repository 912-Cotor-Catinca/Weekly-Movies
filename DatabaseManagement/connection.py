from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# # Database connection parameters
# db_params = {
#     'host': 'localhost',
#     'port': '5432',
#     'database': 'cinema',
#     'user': 'postgres',
#     'password': 'parola'
# }
# # for creating connection string
# # Create a SQLAlchemy engine to connect to the database
# engine = create_engine(f'postgresql+psycopg2://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}')
#
# # you can test if the connection is made or not
# try:
#     with engine.connect() as connection_str:
#         print('Successfully connected to the PostgreSQL database')
# except Exception as ex:
#     print(f'Sorry failed to connect: {ex}')
#
#
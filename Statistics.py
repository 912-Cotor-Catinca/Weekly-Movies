import pandas as pd

class DatabaseStatistics:
    def __init__(self, db_params, engine):
        self.db_params = db_params
        self.engine = engine

    def execute_query(self, query):
        result = pd.read_sql_query(query, self.engine)
        return result

    def get_table_statistics(self, table_name):
        query = f"SELECT * FROM {table_name};"
        table_df = self.execute_query(query)

        if not table_df.empty:
            print(f"\n{table_name} Table Statistics:")
            print(table_df.describe(include='all'))
        else:
            print(f"\n{table_name} Table is empty.")

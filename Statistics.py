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
            describe_stats = table_df.describe(include='all')
            statistics_dict = {
                'count': describe_stats.loc['count'].to_dict(),
                'mean': describe_stats.loc['mean'].to_dict(),
                'std': describe_stats.loc['std'].to_dict(),
                'min': describe_stats.loc['min'].to_dict(),
                '25%': describe_stats.loc['25%'].to_dict(),
                '50%': describe_stats.loc['50%'].to_dict(),
                '75%': describe_stats.loc['75%'].to_dict(),
                'max': describe_stats.loc['max'].to_dict()
            }
            return statistics_dict
        else:
            print(f"\n{table_name} Table is empty.")

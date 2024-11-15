
import dlt
import humanize
from dlt.common import pendulum
from dlt.sources.credentials import ConnectionStringCredentials
from dlt.sources.sql_database import sql_database, sql_table

def load_entire_database():
    """
    Load the entire database into a Postgres Sql.

    This function assumes that the database connection string is stored in a
    'connection_string' environment variable."""

    pipeline = dlt.pipeline(
        pipeline_name='northwind',
        destination='postgres',
        dataset_name='public'

    )


    source = sql_database()
    info = pipeline.run(source, write_disposition='replace')

    print(info)


if __name__ == '__main__':
    load_entire_database()
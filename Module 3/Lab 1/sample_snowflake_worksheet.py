import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col

def main(session: snowpark.Session): 
    # Your code goes here, inside the "main" handler.
    output = session.sql("create or replace temp stage my_stage").collect()

    # Return value will appear in the Results tab.
    return output
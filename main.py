import psycopg2
import json

conn = psycopg2.connect( host="", database="", user="" , password=""  )

print( conn.status )

print( conn.info )

with conn.cursor() as cur:
    cur.execute( 'select to_json( x.* )  from ( select * from cnae limit 10 ) x ' )
    for record in cur:
       print( json.loads( json.dumps( record )) )


conn.close()

print("fim")
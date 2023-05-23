import psycopg2
import json

conn = psycopg2.connect( host="", database="", user="" , password=""  )

print( conn.status )

print( conn.info )

with conn.cursor() as cur:
    cur.execute( 'select * from cnae limit 10' )
    for record in cur:
       print(record)
       print( json.dumps( record ))
       print( record[0])
       cnae = { "codigo": record[0], "nome" : record[1] }
       print( cnae )


conn.close()

print("fim")
import psycopg2

conn = psycopg2.connect( host="191.252.0.35", database="bigdata", user="delta" , password="Delta202301"  )

print( conn.status )

print( conn.info )

with conn.cursor() as cur:
    cur.execute( 'select * from cnae limit 10')
    for record in cur:
       print(record)
       print( record[0])

conn.close()

print("fim")
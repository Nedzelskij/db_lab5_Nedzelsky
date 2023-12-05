import json
import psycopg2

username = 'nedzelsky'
password = '3030'
database = 'db_lab5_nedzelsky'

conn = psycopg2.connect(user=username, password=password, dbname=database)

data = {}
with conn:

    cur = conn.cursor()
    
    for table in ('storages', 'supermarkets', 'vegetables', 'storage_vegetables', 'deliveries'):
        cur.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cur.description]

        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table] = rows

with open('Nedzelsky_DB.json', 'w') as outf:
    json.dump(data, outf, default = str)
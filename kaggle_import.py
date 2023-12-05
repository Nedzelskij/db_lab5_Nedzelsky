import csv
import psycopg2

username = 'nedzelsky'
password = '3030'
database = 'db_lab5_nedzelsky'

INPUT_CSV_FILE = 'Vegetable_market.csv'

query_01 = '''
DELETE FROM vegetables
'''

query_02 = '''
DELETE FROM storage_vegetables
'''

query_03 = '''
DELETE FROM deliveries
'''

query_1 = '''
INSERT INTO vegetables (prod_id, prod_name, season, month, prod_price_kg) VALUES (%s, %s, %s, %s, %s)
'''

query_2 = '''
INSERT INTO
    storage_vegetables (stor_id, prod_id, stor_prod_quantity_kg)
VALUES
    (1, 10001, 140),
    (1, 10004, 34.5),
	(1, 10005, 12.2),
    (2, 10003, 72.2),
	(2, 10007, 212.2),
	(2, 10006, 122.2),
	(2, 10010, 102),
	(4, 10009, 34),
    (4, 10001, 355),
	(5, 10010, 40),
    (5, 10006, 230),
	(6, 10001, 77),
	(6, 10002, 77),
	(7, 10009, 70),
	(7, 10010, 92),
	(7, 10007, 20),
	(8, 10001, 277),
	(8, 10005, 45),
	(9, 10004, 54),
	(9, 10008, 27),
	(9, 10001, 4),
	(10, 10008, 190),
    (10, 10001, 181)
'''

query_3 = '''
INSERT INTO
    deliveries (del_date, stor_id, prod_id, sup_id, del_quantity_kg)
VALUES
    ('2023-05-01', 1, 10001, 'sup_11', 20),
    ('2023-07-02', 1, 10005, 'sup_13', 10),
    ('2023-01-07', 2, 10007, 'sup_15', 27),
    ('2023-10-10', 2, 10006, 'sup_11', 15),
    ('2023-06-26', 2, 10003, 'sup_11', 34),
	('2023-07-03', 4, 10001, 'sup_12', 111),
	('2023-11-01', 4, 10009, 'sup_13', 19),
	('2023-03-17', 5, 10010, 'sup_18', 20),
	('2023-01-14', 6, 10002, 'sup_15', 5),
	('2023-03-20', 6, 10001, 'sup_17', 30),
	('2023-08-14', 7, 10007, 'sup_16', 25),
	('2023-07-30', 9, 10004, 'sup_17', 41),
	('2023-03-14', 9, 10008, 'sup_18', 55),
	('2023-09-14', 9, 10001, 'sup_19', 5),
	('2023-05-22', 10, 10008, 'sup_18', 18)
	
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()
    cur.execute(query_03)
    cur.execute(query_02)
    cur.execute(query_01)

    seen = []
    my_idx = 0
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
            price = float(row['Price per kg'])
            values = (idx + 10001 - my_idx, row['Vegetable'], row['Season'], row['Month'], price)
            # cur.execute(query_1, values)
            if values[1] not in seen: 
                cur.execute(query_1, values)
                seen.append(values[1])
            else:
                my_idx += 1

    cur.execute(query_2)
    cur.execute(query_3)
    conn.commit()

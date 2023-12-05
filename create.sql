CREATE TABLE storages
(
  stor_id INT NOT NULL,
  stor_address VARCHAR(25) NOT NULL,
  PRIMARY KEY (stor_id)
);

CREATE TABLE supermarkets
(
  sup_id CHAR(15) NOT NULL,
  sup_address VARCHAR(25) NOT NULL,
  sup_name VARCHAR(20) NOT NULL,
  PRIMARY KEY (sup_id)
);

CREATE TABLE vegetables
(
  prod_id INT NOT NULL,
  prod_name VARCHAR(15) NOT NULL,
  prod_price_kg FLOAT NOT NULL,
  season CHAR(10),
  month CHAR(15),
  PRIMARY KEY (prod_id)
);

CREATE TABLE storage_vegetables
(
  stor_prod_quantity_kg FLOAT NOT NULL,
  stor_id INT NOT NULL,
  prod_id INT NOT NULL,
  PRIMARY KEY (stor_id, prod_id),
  FOREIGN KEY (stor_id) REFERENCES storages(stor_id),
  FOREIGN KEY (prod_id) REFERENCES vegetables(prod_id)
);

CREATE TABLE deliveries
(
  del_date DATE NOT NULL,
  del_quantity_kg FLOAT NOT NULL,
  sup_id CHAR(15) NOT NULL,
  stor_id INT NOT NULL,
  prod_id INT NOT NULL,
  PRIMARY KEY (del_date, sup_id, stor_id, prod_id),
  FOREIGN KEY (sup_id) REFERENCES supermarkets(sup_id),
  FOREIGN KEY (stor_id, prod_id) REFERENCES storage_vegetables(stor_id, prod_id)
);
create table StorageCopy as select * from storages; 
delete from StorageCopy;
-- select * from StorageCopy;
-- drop table StorageCopy;

DO $$
 DECLARE
     store_id   storagecopy.stor_id%TYPE;
     store_address storagecopy.stor_address%TYPE;

 BEGIN
     store_id := 0;
     store_address := ' Main Street';
     FOR counter IN 1..20
         LOOP
            INSERT INTO storagecopy (stor_id, stor_address)
             VALUES (counter + store_id, 2*counter || store_address);
         END LOOP;
 END;
 $$
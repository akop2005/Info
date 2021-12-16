
UPDATE clients
 SET registration = SUBSTR(registration,7,4) || '-' || SUBSTR(registration,4,2) || '-' || SUBSTR(registration,1,2);
SELECT * from clients;
 
 
SELECT * FROM clients ORDER BY registration DESC limit 1;
SELECT DISTINCT birth from clients;
SELECT SUM(number) as 'total_items' from goods;
select
      AVG(
         (DATE('now')-birth) 
          )
FROM clients where (DATE('now')-registration)<=2;
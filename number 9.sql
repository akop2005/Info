SELECT * FROM clients, orders where clients.id=client_id;

select surname,name,order_price from clients, orders where clients.id=client_id;

select client_id,good_name from clients,orders,goods where clients.id=client_id and goods.id=good_id;

select surname,name,good_id from clients,orders where clients.id = client_id and clients.id=2;

select orders.id,phone_number from clients, orders where clients.id = client_id;
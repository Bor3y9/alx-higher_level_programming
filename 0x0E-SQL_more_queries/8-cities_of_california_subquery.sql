-- list cities of california
SELECT id,name FROM cities WHERE state_id =
(SELECT id FROM states WHERE name = 'California') ORDERD BY cities.id ASC;

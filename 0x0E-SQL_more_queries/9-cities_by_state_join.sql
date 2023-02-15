-- lists all cities contained in a database
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state.id ORDER BY cities.id;

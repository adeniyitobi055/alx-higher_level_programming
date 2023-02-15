-- lists all cities contained in a database
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON state.id = cities.states.id ORDER BY cities.id;

from movies.db import driver


with driver.session() as session:

    result = session.run(
        """
        MATCH (u:User)-[:WATCHED]->(m:Movie)-[:HAS_GENRE]->(g:Genre)

        RETURN u, m, g
        """
    )

    found = False

    for record in result:
        found = True

        user = dict(record["u"])
        movie = dict(record["m"])
        genre = dict(record["g"])

        print(
            user,
            "-> WATCHED ->",
            movie,
            "-> HAS_GENRE ->",
            genre
        )

    if not found:
        print("No User -> Movie -> Genre path found.")


driver.close()

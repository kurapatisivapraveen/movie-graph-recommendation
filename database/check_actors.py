from movies.db import driver


with driver.session() as session:

    result = session.run(
        """
        MATCH (m:Movie)-[:HAS_ACTOR]->(a:Actor)
        RETURN m.title AS movie,
               a.name AS actor
        ORDER BY movie, actor
        """
    )

    for record in result:
        print(
            record["movie"],
            "->",
            record["actor"]
        )


driver.close()
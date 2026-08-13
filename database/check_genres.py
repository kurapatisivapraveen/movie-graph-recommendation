from movies.db import driver

with driver.session() as session:
    result = session.run(
        """
        MATCH (m:Movie)-[:HAS_GENRE]->(g:Genre)
        RETURN m.title AS movie,
               g.name AS genre
        ORDER BY movie, genre
        """

    )

    for record in result:
        print(
            record["movie"],
            "->",
            record["genre"]
        )
driver.close()

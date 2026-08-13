from movies.db import driver 

with driver.session() as session:

    result = session.run(
        """
        MATCH (m:Movie)-[:DIRECTED_BY]->(d:Director)
        RETURN m.title AS movie,
               d.name AS director
        ORDER BY movie
        """
    )

    for record in result:
        print(
            record["movie"],
            "->",
            record["director"]
        )


driver.close()
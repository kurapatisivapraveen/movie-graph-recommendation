from movies.db import driver


with driver.session() as session:

    result = session.run(
        """
        MATCH (u:User)-[w:WATCHED]->(m:Movie)
        RETURN u.name AS user,
               m.title AS movie,
               w.rating AS rating
        ORDER BY user, movie
        """
    )

    for record in result:
        print(
            record["user"],
            "->",
            record["movie"],
            "| Rating:",
            record["rating"]
        )


driver.close()
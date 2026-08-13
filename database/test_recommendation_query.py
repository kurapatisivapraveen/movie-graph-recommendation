from movies.db import driver


with driver.session() as session:

    result = session.run(
        """
        MATCH (u:User {name: "Praveen"})
              -[:WATCHED]->
              (watched:Movie)
              -[:HAS_GENRE]->
              (genre:Genre)
              <-[:HAS_GENRE]-
              (recommended:Movie)

        WHERE NOT (u)-[:WATCHED]->(recommended)

        RETURN DISTINCT
               u.name AS user,
               watched.title AS watched_movie,
               genre.name AS genre,
               recommended.title AS recommendation
        """
    )

    records = result.data()

    print("Number of results:", len(records))

    for record in records:
        print(
            record["user"],
            "| watched:", record["watched_movie"],
            "| genre:", record["genre"],
            "| recommendation:", record["recommendation"]
        )


driver.close()
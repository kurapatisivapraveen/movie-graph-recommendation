from movies.db import driver


with driver.session() as session:

    result = session.run(
        """
        MATCH (m:Movie)
        RETURN m.title AS title, m.year AS year
        ORDER BY m.year
        """
    )

    for record in result:
        print(
            "Movie:",
            record["title"],
            "| Year:",
            record["year"]
        )

driver.close()
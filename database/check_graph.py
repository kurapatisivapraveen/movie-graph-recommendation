from movies.db import driver


with driver.session() as session:

    result = session.run(
        """
        MATCH (n)
        RETURN labels(n) AS labels,
               n
        LIMIT 50
        """
    )

    for record in result:
        print(
            "Labels:",
            record["labels"],
            "| Data:",
            dict(record["n"])
        )


driver.close()
from movies.db import driver


with driver.session() as session:

    result = session.run(
        """
        MATCH (a)-[r]->(b)
        RETURN labels(a) AS from_labels,
               a,
               type(r) AS relationship,
               labels(b) AS to_labels,
               b
        LIMIT 50
        """
    )

    for record in result:
        print(
            dict(record["a"]),
            "--",
            record["relationship"],
            "-->",
            dict(record["b"])
        )


driver.close()
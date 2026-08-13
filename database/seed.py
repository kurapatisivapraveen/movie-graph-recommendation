from movies.db import driver



movies = [
    {
        "title": "RRR test",
        "year": 2022
    },
    {
        "title": "Baahubali: The Beginning",
        "year": 2015
    },
    {
        "title": "Pushpa: The Rise",
        "year": 2021
    },
    {
        "title": "Jersey",
        "year": 2019
    },
    {
        "title": "Eega",
        "year": 2012
    }
]


with driver.session() as session:

    for movie in movies:

        result = session.run(
            """
            MERGE (m:Movie {title: $title})
            SET m.year = $year
            RETURN m.title AS title, m.year AS year
            """,
            title=movie["title"],
            year=movie["year"]
        )

        record = result.single()

        print(
            "Movie:",
            record["title"],
            "| Year:",
            record["year"]
        )


driver.close()
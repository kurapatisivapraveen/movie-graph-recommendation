from movies.db import driver


movie_genres = [
    {
        "movie": "RRR",
        "genres": ["Action", "Drama"]
    },
    {
        "movie": "Eega",
        "genres": ["Fantasy", "Action"]
    },
    {
        "movie": "Baahubali: The Beginning",
        "genres": ["Action", "Fantasy"]
    },
    {
        "movie": "Jersey",
        "genres": ["Drama", "Sports"]
    },
    {
        "movie": "Pushpa: The Rise",
        "genres": ["Action", "Drama"]
    },
    {
        "movie": "Inception",
        "genres": ["Action", "Sci-Fi", "Thriller"]
    }
]


with driver.session() as session:

    for item in movie_genres:

        for genre in item["genres"]:

            result = session.run(
                """
                MATCH (m:Movie {title: $movie})

                MERGE (g:Genre {name: $genre})

                MERGE (m)-[:HAS_GENRE]->(g)

                RETURN m.title AS movie,
                       g.name AS genre
                """,
                movie=item["movie"],
                genre=genre
            )

            record = result.single()

            print(
                record["movie"],
                "->",
                record["genre"]
            )


driver.close()
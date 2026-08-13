from movies.db import driver


def recommend_movies(username):

    with driver.session() as session:

        result = session.run(
            """
            MATCH (u:User {name: $username})-[:WATCHED]->(watched:Movie)

            WITH u, collect(watched.title) AS watchedMovies

            MATCH (u)-[:WATCHED]->(watchedMovie:Movie)-[:HAS_GENRE]->(g:Genre)

            MATCH (recommended:Movie)-[:HAS_GENRE]->(g)

            WHERE NOT recommended.title IN watchedMovies

            RETURN DISTINCT
                recommended.title AS movie,
                recommended.year AS year
            """,
            username=username
        )

        return result.data()
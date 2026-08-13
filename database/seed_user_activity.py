from movies.db import driver


activities = [
    {
        "user": "Praveen",
        "movie": "RRR",
        "rating": 5
    },
    {
        "user": "Praveen",
        "movie": "Eega",
        "rating": 4
    },
    {
        "user": "Praveen",
        "movie": "Jersey",
        "rating": 5
    },
    {
        "user": "Rahul",
        "movie": "RRR",
        "rating": 4
    },
    {
        "user": "Rahul",
        "movie": "Pushpa: The Rise",
        "rating": 5
    },
    {
        "user": "Sandeep",
        "movie": "Baahubali: The Beginning",
        "rating": 5
    },
    {
        "user": "Sandeep",
        "movie": "Pushpa: The Rise",
        "rating": 4
    },
    {
        "user": "Anjali",
        "movie": "Eega",
        "rating": 5
    },
    {
        "user": "Anjali",
        "movie": "Inception",
        "rating": 5
    }
]


with driver.session() as session:

    for item in activities:

        result = session.run(
            """
            MATCH (u:User {name: $user})
            MATCH (m:Movie {title: $movie})

            MERGE (u)-[w:WATCHED]->(m)

            SET w.rating = $rating

            RETURN u.name AS user,
                   m.title AS movie,
                   w.rating AS rating
            """,
            user=item["user"],
            movie=item["movie"],
            rating=item["rating"]
        )

        record = result.single()

        print(
            record["user"],
            "-> WATCHED ->",
            record["movie"],
            "| Rating:",
            record["rating"]
        )


driver.close()
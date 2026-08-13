from movies.db import driver 
relationships =[
    {
        "movie":"RRR",
        "director":"S.S. Rajamouli"
    },
    {
        "movie": "Eega",
        "director": "S.S. Rajamouli"
    },
    {
        "movie": "Baahubali: The Beginning",
        "director": "S.S. Rajamouli"
    },
    {
        "movie": "Jersey",
        "director": "Gowtam Tinnanuri"
    },
    {
        "movie": "Pushpa: The Rise",
        "director": "Sukumar"
    },
    {
        "movie": "Inception",
        "director": "Christopher Nolan"
    }
    
]

with driver.session() as session:
    
    for item in relationships:

        result = session.run(
            """
            MATCH (m:Movie {title:$movie})

            MERGE (d:Director {name: $director})

            MERGE (m)-[:DIRECTED_BY]->(d)

            RETURN m.title AS movie,
                   d.name AS director
            """,
            movie=item["movie"],
            director=item["director"]
        )

        record = result.single()

        print(
            "Movie:",
            record["movie"],
            "-> Director:",
            record["director"]
        )
driver.close()


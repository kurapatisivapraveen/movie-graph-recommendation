from movies.db import driver 

movie_actors =[
    {
        'movie':"RRR",
        'actors':[
            "N.T. Rama Rao Jr."
            'Ram Charan'
            "Alia Bhatt"
        ]
    },
    {
        "movie":"Eega",
        "actors":[
            "Nani",
            "Samantha Ruth Prabhu",
            "Sudeep"
        ]  
    },
    {
        "movie": "Baahubali: The Beginning",
        "actors": [
            "Prabhas",
            "Rana Daggubati",
            "Anushka Shetty",
            "Tamannaah Bhatia"
        ]
    },
    {
        "movie":"Jersey",
        "actors":[
            "Nani",
             "Shraddha Srinath"
        ]
    },
    {
        "movie": "Pushpa: The Rise",
        "actors": [
            "Allu Arjun",
            "Rashmika Mandanna",
            "Fahadh Faasil"
        ]
    },
    {
        "movie": "Inception",
        "actors": [
            "Leonardo DiCaprio",
            "Joseph Gordon-Levitt",
            "Elliot Page"
        ]
    }
]


with driver.session() as session:

    for item in movie_actors:

        for actor in item["actors"]:

            result = session.run(
                """
                MATCH (m:Movie {title: $movie})

                MERGE (a:Actor {name: $actor})

                MERGE (m)-[:HAS_ACTOR]->(a)

                RETURN m.title AS movie,
                       a.name AS actor
                """,
                movie=item["movie"],
                actor=actor
            )

            record = result.single()

            print(
                record["movie"],
                "->",
                record["actor"]
            )


driver.close()

        
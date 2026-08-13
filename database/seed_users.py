from movies.db import driver


users = [
    {
        "name": "Praveen"
    },
    {
        "name": "Rahul"
    },
    {
        "name": "Sandeep"
    },
    {
        "name": "Anjali"
    }
]


with driver.session() as session:

    for user in users:

        result = session.run(
            """
            MERGE (u:User {name: $name})

            RETURN u.name AS name
            """,
            name=user["name"]
        )

        record = result.single()

        print(
            "User created:",
            record["name"]
        )


driver.close()
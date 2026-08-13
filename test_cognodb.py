import os

from dotenv import load_dotenv
from neo4j import GraphDatabase


load_dotenv()


uri = os.getenv("COGNODB_URI")
username = os.getenv("COGNODB_USERNAME")
password = os.getenv("COGNODB_PASSWORD")


driver = GraphDatabase.driver(
    uri,
    auth=(username, password)
)


try:
    driver.verify_connectivity()
    print("Connected to CognoDB successfully!")

    with driver.session() as session:

        result = session.run(
            """
            CREATE (m:Movie {
                title: "Inception",
                year: 2010
            })
            RETURN m.title AS title, m.year AS year
            """
        )

        record = result.single()

        print("Movie created:")
        print("Title:", record["title"])
        print("Year:", record["year"])

finally:
    driver.close()
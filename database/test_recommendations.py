from database.recommendations import recommend_movies


results = recommend_movies("Praveen")


for record in results:

    print(
        "Movie:",
        record["movie"],
        "| Year:",
        record["year"],
        "| Matching Genres:",
        record["matching_genres"]
    )
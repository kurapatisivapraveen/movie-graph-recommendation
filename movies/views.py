from django.shortcuts import render
from django.http import JsonResponse

from database.recommendations import recommend_movies


def home(request):
    return render(request, "index.html")


def recommendations(request, username):

    results = recommend_movies(username)

    return JsonResponse({
        "user": username,
        "recommendations": results
    })





from django.shortcuts import render
from django.http import JsonResponse

from movies.db import driver
from database.recommendations import recommend_movies


def home(request):
    return render(request, "index.html")


def users(request):

    with driver.session() as session:

        result = session.run(
            """
            MATCH (u:User)
            RETURN u.name AS name
            ORDER BY u.name
            """
        )

        user_list = [
            record["name"]
            for record in result
        ]

    return JsonResponse({
        "users": user_list
    })


def recommendations(request, username):

    results = recommend_movies(username)

    return JsonResponse({
        "user": username,
        "recommendations": results
    })
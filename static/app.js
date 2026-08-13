const usernameSelect =
    document.getElementById("username");

const recommendations =
    document.getElementById("recommendations");

const message =
    document.getElementById("message");

const stats =
    document.getElementById("stats");

const movieCount =
    document.getElementById("movieCount");


/* LOAD USERS */

async function loadUsers() {

    try {

        const response =
            await fetch("/api/users/");

        if (!response.ok) {
            throw new Error("Could not load users");
        }

        const data =
            await response.json();


        usernameSelect.innerHTML =
            '<option value="">Select a user</option>';


        data.users.forEach(user => {

            const option =
                document.createElement("option");

            option.value = user;

            option.textContent = user;

            usernameSelect.appendChild(option);

        });


    } catch (error) {

        console.error(error);

        usernameSelect.innerHTML =
            '<option value="">Unable to load users</option>';

    }

}


/* GET RECOMMENDATIONS */

async function getRecommendations() {

    const username =
        usernameSelect.value;


    if (!username) {

        message.innerHTML =
            "Please select a user first.";

        return;
    }


    message.innerHTML =
        "🔄 Finding recommendations...";


    recommendations.innerHTML = "";

    stats.classList.add("hidden");


    try {

        const response =
            await fetch(
                `/api/recommendations/${encodeURIComponent(username)}/`
            );


        if (!response.ok) {

            throw new Error(
                "Failed to fetch recommendations"
            );

        }


        const data =
            await response.json();


        message.innerHTML =
            `Recommendations for <strong>${data.user}</strong>`;


        movieCount.textContent =
            data.recommendations.length;


        stats.classList.remove("hidden");


        if (data.recommendations.length === 0) {

            recommendations.innerHTML = `
                <div class="welcome-card">

                    <div class="welcome-icon">
                        😔
                    </div>

                    <h3>
                        No recommendations found
                    </h3>

                    <p>
                        We couldn't find movies for this user yet.
                    </p>

                </div>
            `;

            return;
        }


        data.recommendations.forEach(movie => {

            const card =
                document.createElement("div");


            card.className =
                "movie-card";


            card.innerHTML = `

                <div class="movie-icon">
                    🎬
                </div>

                <h3>
                    ${movie.movie}
                </h3>

                <p class="movie-year">
                    📅 ${movie.year}
                </p>

            `;


            recommendations.appendChild(card);

        });


    } catch (error) {

        console.error(error);


        message.innerHTML =
            "❌ Could not load recommendations.";


        recommendations.innerHTML = `

            <div class="welcome-card">

                <div class="welcome-icon">
                    ⚠️
                </div>

                <h3>
                    Something went wrong
                </h3>

                <p>
                    Please check that the Django server
                    is running.
                </p>

            </div>

        `;

    }

}


/* LOAD USERS WHEN PAGE OPENS */

loadUsers();
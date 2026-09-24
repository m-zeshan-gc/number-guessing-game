// Start the game
async function startGame() {

    let name = document.getElementById("nameInput").value;

    let favoriteGame =
        document.getElementById("favoriteGameInput").value;


    // Check if name is empty
    if (name == "") {

        alert("Please enter your name.");

        return;
    }


    // Send player information to Python
    let response = await fetch("/start", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            name: name,

            favorite_game: favoriteGame

        })
    });


    // Get Python's response
    let data = await response.json();


    // Hide start section
    document.getElementById("start-section").style.display = "none";


    // Show game section
    document.getElementById("game-section").style.display = "block";


    // Show welcome message
    document.getElementById("welcomeMessage").innerText =
        data.message;
}


// Check user's guess
async function checkGuess() {

    let guess =
        document.getElementById("guessInput").value;


    // Check if input is empty
    if (guess == "") {

        alert("Please enter a number.");

        return;
    }


    // Send guess to Python
    let response = await fetch("/guess", {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify({

            guess: Number(guess)

        })
    });


    // Get Python response
    let data = await response.json();


    // Show result
    document.getElementById("result").innerText =
        data.message;


    // If game is over
    if (data.game_over == true) {

        document.getElementById("newGameButton").style.display =
            "inline-block";
    }
}


// Start new game
async function newGame() {

    let response = await fetch("/new-game", {

        method: "POST"

    });


    // Get Python response
    let data = await response.json();


    // Show message
    document.getElementById("result").innerText =
        data.message;


    // Clear old guess
    document.getElementById("guessInput").value = "";


    // Hide New Game button
    document.getElementById("newGameButton").style.display =
        "none";
}
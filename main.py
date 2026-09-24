from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import random


# Create FastAPI application
app = FastAPI()


# Tell FastAPI where HTML files are
templates = Jinja2Templates(directory="templates")


# Tell FastAPI where CSS and JavaScript files are
app.mount("/static", StaticFiles(directory="static"), name="static")


# Game variables
secret_number = 0
attempts = 0
max_attempts = 7
player_name = ""
favorite_game = ""
game_started = False


# Home page
@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# Start the game
@app.post("/start")
def start_game(data: dict):

    global secret_number
    global attempts
    global player_name
    global favorite_game
    global game_started

    player_name = data["name"]
    favorite_game = data["favorite_game"]

    secret_number = random.randint(1, 100)

    attempts = 0

    game_started = True

    return {
        "message": f"Welcome {player_name}! Guess a number between 1 and 100."
    }


# Check the user's guess
@app.post("/guess")
def check_guess(data: dict):

    global attempts
    global game_started

    if not game_started:
        return {
            "message": "Please start the game first.",
            "game_over": True
        }

    guess = data["guess"]

    attempts += 1

    # Correct guess
    if guess == secret_number:

        game_started = False

        return {
            "message": f"Correct! 🎉 You guessed the number in {attempts} attempts.",
            "correct": True,
            "game_over": True
        }

    # Maximum attempts reached
    if attempts >= max_attempts:

        game_started = False

        return {
            "message": f"Game Over! 😢 The secret number was {secret_number}.",
            "correct": False,
            "game_over": True
        }

    # Guess is too low
    if guess < secret_number:

        return {
            "message": f"Too low! ⬆️ Try a higher number. Attempts left: {max_attempts - attempts}",
            "correct": False,
            "game_over": False
        }

    # Guess is too high
    else:

        return {
            "message": f"Too high! ⬇️ Try a lower number. Attempts left: {max_attempts - attempts}",
            "correct": False,
            "game_over": False
        }


# Start a new game
@app.post("/new-game")
def new_game():

    global secret_number
    global attempts
    global game_started

    secret_number = random.randint(1, 100)

    attempts = 0

    game_started = True

    return {
        "message": f"New game started! {player_name}, guess a number between 1 and 100."
    }
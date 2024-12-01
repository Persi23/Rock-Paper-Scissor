from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]

html_temp = '''
<!DOCTYPE html>
<html>
    <head>
        <title> Rock Paper Scissor Game</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                background-color: #F0F0F0;
                padding: 20px;
            }
            h1 {
                color: black;
                font-size: 45px;
            }
            pre {
                font-size: 18px;
                font-family: monospace;
                color: black;
            }
            label {
                font-size: 18px;
            }
            select, button {
                padding: 20px;
                font-weight: bold;
                margin: 30px;
            }
            .result {
                color: blue;
                font-size: 40px;
                font-weight: bolder;
            }
            button{
                background-color:blue;
                color:white;
                font-size:20px;
                border-radius:50%;
            }
        </style>
    </head>
    <body>
        <h1>Rock Paper Scissor Game</h1>
        <form method="POST" action="/">
            <label for="choice">Choose:</label>
            <select name="choice">
                <option value="0">Rock</option>
                <option value="1">Paper</option>
                <option value="2">Scissors</option>
            </select>
            <button type="submit">Play</button>
        </form>

        {% if user_ascii %}
            <h2>Your choice:</h2>
            <pre>{{ user_ascii }}</pre>
            <h2>Computer's choice:</h2>
            <pre>{{ comp_ascii }}</pre>
            <div class="result">{{ result }}</div>
        {% endif %}
    </body>
</html>
'''


@app.route("/", methods=["POST", "GET"])
def play():
    user_ascii = None
    comp_ascii = None
    result = None

    if request.method == "POST":
        try:
            user_choice = int(request.form["choice"])
            comp_choice = random.randint(0, 2)

            user_ascii = game[user_choice]
            comp_ascii = game[comp_choice]

            if (user_choice == 0 and comp_choice == 2) or \
                    (user_choice == 1 and comp_choice == 0) or \
                    (user_choice == 2 and comp_choice == 1):
                result = "You Win!!!"
            elif user_choice == comp_choice:
                result = "It's a Draw"
            else:
                result = "You Lose!!!"
        except (ValueError, IndexError):
            result = "Invalid Choice. Try again!!"

    return render_template_string(
        html_temp,
        user_ascii=user_ascii,
        comp_ascii=comp_ascii,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=False, host='127.0.0.1')

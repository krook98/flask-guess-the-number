from flask import Flask
import random

app = Flask(__name__)
number = random.randint(0, 9)


@app.route('/')
def home():
    return '<h1>Guess the number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="Animated image"/>'

@app.route('/<int:guess>')
def guess_number(guess):
    if guess + 6 < number:
        return '<h1>Waaaaaay too low</h1>' \
               '<img src="https://media0.giphy.com/media/Gsy6Jk7f3axNVT3uRn/giphy.gif?cid=790b7611cef799ec9a9d6c595cd76dcc1be642d821a04f17&rid=giphy.gif&ct=g" alt="too-low"/>'
    if guess > number:
        return '<h1>Too high</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="too-high"/>'
    elif guess < number:
        return '<h1>Too low</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="too-low"/>'
    else:
        return '<h1>That is correct!</h1>' \
               '<img src="https://media1.giphy.com/media/MNmyTin5qt5LSXirxd/giphy.gif?cid=790b7611810e9bd826e65b99abfb955172ed1da11f03f8c0&rid=giphy.gif&ct=g" alt="correct"/>'


if __name__ == 'name':
    app.run(debug=True)
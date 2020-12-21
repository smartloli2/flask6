import nltk
from flask import Flask, redirect, url_for, request
from flask import render_template
from flask import Response
from api import find_words_by_request
import os


app = Flask("My app", template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), "layout"))


@app.route('/')
def index():
    words = "Dragon"
    examples = 5
    if request.cookies.get("words"):
        words = request.cookies.get("words")
    if request.cookies.get("examples"):
        examples = request.cookies.get("examples")
    return render_template('home.html', words=words, examples=examples)


@app.route('/test#home')
def test():
    return 'Sweet home alabama'


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/result')
def result():
    words = request.args.get('words', type=str, default="").replace(' ', '').split(';')
    examples = request.args.get('examples', type=int, default=5)
    sentences = find_words_by_request({"words": words, "examples": examples})
    resp = Response(render_template('result.html', sentences=sentences['words'], words=words), status=200)
    resp.set_cookie("words", ';'.join(words))
    resp.set_cookie("examples", str(examples))
    return resp


@app.route('/request', methods=['POST'])
def req():
    obj = request.get_json(force=True)
    sentences = find_words_by_request(obj)
    return sentences, 200




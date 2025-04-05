from fastapi import FastAPI
import random

app = FastAPI()

posts = [
    {"id": 1, "title": "Getting Started with FastAPI", "author": "Salman", "content": "FastAPI is awesome!"},
    {"id": 2, "title": "Learn Python", "author": "Ayesha", "content": "Python is beginner-friendly."},
    {"id": 3, "title": "REST API Tips", "author": "Ali", "content": "Use proper status codes."},
]

success_quotes = [
    "Success is not final, failure is not fatal: It is the courage to continue that counts. — Winston Churchill",
    "Don't watch the clock; do what it does. Keep going. — Sam Levenson",
    "The only place where success comes before work is in the dictionary. — Vidal Sassoon",
    "Success usually comes to those who are too busy to be looking for it. — Henry David Thoreau",
    "Opportunities don't happen. You create them. — Chris Grosser",
    "I never dreamed about success. I worked for it. — Estée Lauder",
    "Success is walking from failure to failure with no loss of enthusiasm. — Winston Churchill",
    "There are no secrets to success. It is the result of preparation, hard work, and learning from failure. — Colin Powell",
    "Success doesn’t come from what you do occasionally, it comes from what you do consistently. — Marie Forleo",
    "The road to success and the road to failure are almost exactly the same. — Colin R. Davis"
]


@app.get('/post')

def get_posts():
    """ Return a random list of posts"""
    return {"post":random.choice(posts)}


@app.get('/success_quote')

def get_success_quote(apikey):
    """ Return a random success quote"""
    if apikey != "12345":
        return {"error": "Invalid"}
    return {"success_quote": random.choice(success_quotes)}


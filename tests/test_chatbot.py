# tests/test_chatbot.py

import pytest
from src.chatbot import Chatbot

def test_positive_sentiment():
    bot = Chatbot()
    _, sentiment = bot.reply("I am so happy today!")
    assert sentiment["label"] == "positive"

def test_negative_sentiment():
    bot = Chatbot()
    _, sentiment = bot.reply("I am really sad and upset.")
    assert sentiment["label"] == "negative"

def test_neutral_sentiment():
    bot = Chatbot()
    _, sentiment = bot.reply("I went to the store.")
    assert sentiment["label"] == "neutral"

def test_mood_trend_improved():
    bot = Chatbot()
    bot.reply("I am sad")
    bot.reply("Now I feel better")
    summary = bot.finalize_conversation_report()
    assert "improved" in summary["mood_trend"]

def test_mood_trend_stable():
    bot = Chatbot()
    bot.reply("I am okay")
    bot.reply("Still okay")
    summary = bot.finalize_conversation_report()
    assert "stable" in summary["mood_trend"]

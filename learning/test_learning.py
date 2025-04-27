import pytest
from learning import learning

def test_next_word_prediction_basic():
    # Reset knowledge
    learning.knowledge.clear()
    learning.learn_from_input("hello world")
    learning.learn_from_input("hello there")
    # Predict next word after 'hello'
    predicted = learning.predict_next_word('hello')
    assert predicted in ['world', 'there']

def test_next_word_prediction_unknown_word():
    learning.knowledge.clear()
    learning.learn_from_input("foo bar")
    predicted = learning.predict_next_word('baz')
    assert predicted is None 
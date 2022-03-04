from main import pydb

scores = pydb("scores")

scores.add_column()
scores.add_column()

scores.exportdb("guesserscores")
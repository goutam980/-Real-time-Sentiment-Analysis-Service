from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.form['text']

    blob = TextBlob(data)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        sentiment_label = 'Positive'
    elif sentiment < 0:
        sentiment_label = 'Negative'
    else:
        sentiment_label = 'Neutral'

    response = {
        'sentiment': sentiment_label,
        'polarity': sentiment
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

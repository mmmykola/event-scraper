
from flask import Flask, jsonify
from scraper import scrape_eventbrite_edmonton

app = Flask(__name__)

@app.route('/events', methods=['GET'])
def get_events():
    events = scrape_eventbrite_edmonton()
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)

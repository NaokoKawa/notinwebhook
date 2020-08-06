from flask import abort, Flask, jsonify, request
from slackeventsapi import SlackEventAdapter

app = Flask(__name__)

slack_events_adapter = SlackEventAdapter("SIGINING_SECRET", "7653aef4d589b149c94a47cb8b848dd8", app)
@slack_events_adapter.on("message")
def hookSlackEvents(event_data):
    app.logger.debug(event_data)
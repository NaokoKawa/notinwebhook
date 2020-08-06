import json
import webapp2

class EchoHandler(webapp2.RequestHandler):
    VERIFICATION_TOKEN = 'YOUR_VERIFICATION_TOKEN'

    def post(self):
        body = json.loads(self.request.body)
        if body['token'] != self.VERIFICATION_TOKEN:
            self.response.headers['Content-Type'] = 'text/plain'
            self.status = 403
            self.response.write('403 Forbidden')
            return
        if body['type'] == 'url_verification':
            self.verify_url(body)

    def verify_url(self, params):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(params['challenge'])

app = webapp2.WSGIApplication([
    ('/echo-bot-hook', EchoHandler)
], debug=True)
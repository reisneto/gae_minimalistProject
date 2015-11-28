import os

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Main(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())

class Page2(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('page2.html')
        self.response.write(template.render())


application = webapp2.WSGIApplication([
    ('/', Main),
    ('/page2', Page2)
], debug=True)
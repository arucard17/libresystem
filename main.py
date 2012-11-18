#!/usr/bin/env python

import cgi
import os
import webapp2

from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

class ServiciosPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}

        path = os.path.join(os.path.dirname(__file__), 'servicios.html')
        self.response.out.write(template.render(path, template_values))

class ContactoPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}

        path = os.path.join(os.path.dirname(__file__), 'contacto.html')
        self.response.out.write(template.render(path, template_values))

class SobremiPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}

        path = os.path.join(os.path.dirname(__file__), 'sobremi.html')
        self.response.out.write(template.render(path, template_values))

class PostPage(webapp2.RequestHandler):
    def get(self,post):
        template_values = {}
        posts = {
	        'richard_stallman':'rt.html',
	        'pyme': 'slpyme.html',
	        'software_libre': 'sleducacion.html'
	    }

        if post in posts:
	        path = os.path.join(os.path.dirname(__file__), posts[post])
	        self.response.out.write(template.render(path, template_values))
        else:
			self.response.headers['Content-Type'] = 'text/plain'
			self.response.write('Error al encontrar el post')

class NotFoundPageHandler(webapp2.RequestHandler):
	"""docstring for Error"""
	def get(self):
		template_values = {}

		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write('Error al encontrar la pagina.')


app = webapp2.WSGIApplication([('/', MainPage),
								('/contacto', ContactoPage),
								('/servicios', ServiciosPage),
								('/quienessomos', SobremiPage),
								('/post\/?([a-z_]*)', PostPage),
							    ('/.*', NotFoundPageHandler)],
                                  debug=True)

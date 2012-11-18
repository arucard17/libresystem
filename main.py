#!/usr/bin/env python

import cgi
import os
import webapp2
import json

from google.appengine.ext.webapp import template
from google.appengine.api import mail

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

class SendMail(webapp2.RequestHandler):
	def post(self):
		data = json.loads(self.request.body)

		if not mail.is_email_valid(data['sender']):
			self.response.out.write(json.dumps('{sucess:false,error:"El correo es incorrecto"}'))       	
		else:
			sender_address = data['sender']
			subject = 'contacto'
			body = data['body_mail'] + data['name']
			user_address = 'libresystem@gmail.com'

			mail.send_mail(sender_address, user_address, subject, body)	

			self.response.out.write(json.dumps('{"success":true, "msg":"El correo se ha enviado"}'))   
    	    	


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
								('/sendmail', SendMail),
							    ('/.*', NotFoundPageHandler)],
                                  debug=True)

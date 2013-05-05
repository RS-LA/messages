from google.appengine.ext import db
import json
import webapp2

class Message(db.Model):
    
    body = db.StringProperty()
    
    
    
class MessageRequestHandler(webapp2.RequestHandler):
    
    def get(self, message_id):
        
        # Set this method to return JSON instead of normal text
        self.response.headers['Content-Type'] = 'application/json'

        # Create the Key for the Entity we want using the JID that was passed in.               
        key_user = db.Key.from_path('Message', message_id)
        
        # Perform the query for the Entity using that Key.
        message = db.get(key_user)
        
        message_json = {
            'body': message.body 
        }
        
        self.response.write(json.dumps(message_json))
        
        
    def post(self, message_id):
        
        # Set this method to return JSON instead of normal text
        self.response.headers['Content-Type'] = 'application/json'
        
        
        try:
            # Grab the POST request parameters and put them into variables.
            param_body = self.request.get('body')

            # Make a User object. His Key should be his JID.
            message = Message(key_name=message_id,
                         body=param_body)
            
            # Save the new User into the datastore.
            message.put()
            
            # Tell the user.
            self.response.write('Created new message: %s.\n' % message.body)
            
        except (TypeError, ValueError):
            # If we couldn't grab the PUT request parameters, then show an error.
            self.response.write('Invalid inputs')
            return

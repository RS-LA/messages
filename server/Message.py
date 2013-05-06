from google.appengine.ext import db
import json
import webapp2

class Message(db.Model):
    
    body = db.StringProperty()
    responses = db.ListProperty(db.Key)
    
    def to_json(self):
        return {
            'message_id': self.key().id(),
            'body': self.body
        }
    
    
class MessageRequestHandler(webapp2.RequestHandler):
#     
#     def get(self, user_id):
#         
#         # Set this method to return JSON instead of normal text
#         self.response.headers['Content-Type'] = 'application/json'
# 
#         # Create the Key for the Entity we want using the JID that was passed in.               
#         key_user = db.Key.from_path('User', user_id)
#         
#         # Perform the query for the Entity using that Key.
#         user = db.get(key_user)
#         
#         messages = db.get(user.outbox)
#         
#         
#         
#         self.response.write(json.dumps(message_json))
        
        
    def post(self, user_id):
        
        # Set this method to return JSON instead of normal text
        self.response.headers['Content-Type'] = 'application/json'
        
        try:
            # Get the User object that this Message belongs to.
            key_user = db.Key.from_path('User', user_id)
            user = db.get(key_user)
            
            param_body = self.request.get('body')

            message = Message(body=param_body)
            
            message.put()
            
            user.outbox.append(message.key())
            
            # Tell the user.
            self.response.write(json.dumps(message.to_json()))
            
        except (TypeError, ValueError):
            # If we couldn't grab the PUT request parameters, then show an error.
            self.response.write('Invalid inputs')
            return
        
        

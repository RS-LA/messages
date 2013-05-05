from google.appengine.ext import db
import json
import webapp2
from Message import Message

class Response(db.Model):
    
    body = db.StringProperty()
    author = db.StringProperty()
    
    def to_json(self):
        return {
            'message_id': self.key().id(),
            'author': self.author,
            'body': self.body
        }
    
    
class ResponseRequestHandler(webapp2.RequestHandler):
    
#     def get(self, message_id):
#         
#         # Set this method to return JSON instead of normal text
#         self.response.headers['Content-Type'] = 'application/json'
# 
#         # Create the Key for the Entity we want using the JID that was passed in.               
#         key_message = db.Key.from_path('Message', message_id)
#         
#         # Perform the query for the Entity using that Key.
#         message = db.get(key_message)
#         
#         message_json = {
#             'body': message.body 
#         }
#         
#         self.response.write(json.dumps(message_json))
        
        
    def post(self, user_id, message_id):
        
        # Set this method to return JSON instead of normal text
        self.response.headers['Content-Type'] = 'application/json'
        
        try:
#             self.response.write("User id: %s, Message id: %s" % (user_id, message_id))
            
            message = Message.get_by_id(int(message_id))
            
            
#             self.response.write("Message %s" % message.body)
             
            # Grab the POST request parameters and put them into variables.
            param_author = self.request.get('author')
            param_body = self.request.get('body')
  
            # Make a User object. His Key should be his JID.
            response = Response(author=param_author, body=param_body)
            response.put()
              
            # Save the new User into the datastore.
            message.responses.append(response.key())
             
            # Tell the user.
            self.response.write(json.dumps(response.to_json()))

            
            
            
            
        except (TypeError, ValueError):
            # If we couldn't grab the PUT request parameters, then show an error.
            self.response.write('Invalid inputs')
            return
        
        

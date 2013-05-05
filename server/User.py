from google.appengine.ext import db
import json
import webapp2

class User(db.Model):
    
    first_name = db.StringProperty()
    last_name = db.StringProperty()
    
    inbox = db.ListProperty(db.Key)
    outbox = db.ListProperty(db.Key)
    
    
    
    
class UserRequestHandler(webapp2.RequestHandler):
    
    def get(self, user_id):
        
        user = User();
        
        user.first_name = "Girum"
        user.last_name = "Ibssa"
        
        self.response.write("User %s: %s %s" % (user_id, user.first_name, user.last_name))
        
    def put(self, user_id):
        try:
            # Grab the PUT request parameters and put them into variables.
            param_first_name = self.request.get('fn')
            param_last_name = self.request.get('ln')
            
            # Make a User object. His Key should be his JID.
            user = User(key_name=user_id,
                         first_name=param_first_name,
                         last_name=param_last_name)
            
            # Save the new User into the datastore.
            user.put()
            
            # Tell the user.
            self.response.write('Created new user %s.\n' % user.first_name)
            
        except (TypeError, ValueError):
            # If we couldn't grab the PUT request parameters, then show an error.
            self.response.write('Invalid inputs')
            return
        

        
        
from google.appengine.ext import db
import json
import webapp2

class User(db.Model):
    
    first_name = db.StringProperty()
    last_name = db.StringProperty()
    
    facebook_friends = db.ListProperty(db.Key)
    
    inbox = db.ListProperty(db.Key)
    outbox = db.ListProperty(db.Key)
    
    def to_json(self):
        return {
            'user_id': self.key().name(),
            'fn': self.first_name,
            'ln': self.last_name,
            'friends': self.facebook_friends
        }
    

class UserRequestHandler(webapp2.RequestHandler):
    
    def get(self, user_id):
        
        # Set this method to return JSON instead of normal text
        self.response.headers['Content-Type'] = 'application/json'

        # Create the Key for the Entity we want using the JID that was passed in.               
        key_user = db.Key.from_path('User', user_id)
        
        # Perform the query for the Entity using that Key.
        user = db.get(key_user)
        
        self.response.write(json.dumps(user.to_json()))
        
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
        

        
        
''' NDB storage entities, aka tables '''
from google.cloud import ndb

class Activity(ndb.Model):
    url = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)


class Visit(ndb.Model):
    ip = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

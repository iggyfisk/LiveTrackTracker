''' Livetrack redirect '''
# [START gae_python38_app]
# [START gae_python3_app]

from flask import Flask, request, redirect
from werkzeug.middleware.proxy_fix import ProxyFix
from google.cloud import ndb
from parse import get_livetrack_urls
from entities import Visit, Activity

client = ndb.Client()

def ndb_wsgi_middleware(wsgi_app):
    ''' Wrap request in ndb context '''
    def middleware(environ, start_response):
        with client.context():
            return wsgi_app(environ, start_response)

    return middleware

app = Flask(__name__)
# Wrap the app in middleware.
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=2)
app.wsgi_app = ndb_wsgi_middleware(app.wsgi_app)

@app.route('/')
def redirect_to_activity():
    """On default navigation, redirect to the latest activity"""
    visit = Visit(ip=request.remote_addr)
    visit.put_async()
    lastact = Activity.query().order(-Activity.date).fetch(1)
    return redirect(lastact[0].url)

@app.route('/_ah/mail/<string:to_address>', methods=['POST'])
def mail(to_address: str):
    """On received email, parse an activity URL and store it"""
    urls = get_livetrack_urls(request.data)

    for url in urls:
        act = Activity(url=url)
        act.put()

    return '', 204

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

# [END gae_python3_app]
# [END gae_python38_app]

# Garmin LiveTrack tracker
Every time you start a LiveTrack session with a Garmin device, it creates a unique URL for that session. This mini App Engine project lets you give people a single URL they can visit whenever instead.

* Create a Google cloud project with Firestore in Datastore mode
* Deploy this repo to App Engine for that project: `gcloud app deploy`
* Add an e-mail recipient for LiveTrack sessions in Garmin Connect: `whatever@[YOUR_GCLOUD_APP_ID].appspotmail.com`
* From now on, `https://[YOUR_GCLOUD_APP_ID].appspot.com` will always redirect to your latest LiveTrack session (give or take a few moments for Garmin to send the e-mail and Google to receive it)
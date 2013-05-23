### AppEngine Google+ Sign In with Cloud Endpoints Authenticated calls.

### Run The App Locally
  * Open app.yaml and change YOUR_GOOGLE_API_CLIENT_ID to your Google [API Console Client ID](https://code.google.com/apis/console). You also need to change this in frontend/templates/index.html
    * This project should have access to Google+ API under Services.

You can set Javascript origins when you create the OAuth2 Client in the API Console to:

    http://localhost:7777
    http://your-app-id.appspot.com
    https://your-app-id.appspot.com

### Deploying to AppEngine
  * Make sure to change your-app-id to your own (in app.yaml and 

#### Tools and Technologies
  * AppEngine Python
  * AppEngine Cloud Endpoints
  * HTML/CSS/JS/JQuery
  * Google+ Sign In JS Client
  * OAuth2

#### What's in There?
  * All Google+ Sign In is on client-side.
  * Get user's email and profile.
  * Make OAuth2 Authenticated calls to a cloud endpoints API backend.


### References
  * [AppEngine Cloud Endpoints](https://developers.google.com/appengine/docs/python/endpoints/create_api)
  * [Google+ People and Profiles](https://developers.google.com/+/web/people/#retrieve_an_authenticated_users_email_address)
  * [Google+ Sign in](https://developers.google.com/+/web/signin/)

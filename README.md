# endpoints_auth
A basic way to provide authentication/authorization for Google Cloud Endpoints apps using webapp2

## Prerequisites
endpoints_auth was intended for [Google Cloud Endpoints](https://cloud.google.com/appengine/docs/java/endpoints/)apps built using [webapp2](https://webapp-improved.appspot.com/) as the authentication framework. This project lets your app authenticate Endpoints requests and reject requests not made by your application's users.

## Usage
Use the ```auth_required``` function as a decorator for any of your Endpoints method like so:

````
import endpoints_auth

...

  @endpoints.method(RequestMessage, ResponseMessage, path='path/to/endpoint', http_method='POST', name='my_method_name')
  @endpoints_auth.auth_required()
  def foo(self, request):
      # Define function here

````

The client will need to make a request to your Endpoints API with the webapp2 user ID and token in the ```User-Id``` and ```Token``` headers, respectively.


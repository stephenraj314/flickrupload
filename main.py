import flickr_api as flickr
import os.path as path


def get_keys():
    key = input("Copy API key: ")
    secret = input("Copy API Secret: ")
    return key, secret


def authflickr():
    a = flickr.auth.AuthHandler()
    perms = "delete"
    url = a.get_authorization_url(perms)
    print("Open this Link in a web browser -->", url)
    oauth_verifier = input("Copy & Past tag &oauth_verifier : ")
    a.set_verifier(oauth_verifier)
    flickr.set_auth_handler(a)
    a.save('.auth')

def upload():
    file = input("Enter Image Path : ")
    title = input("Enter Image Title : ")
    return flickr.upload(photo_file=file, title=title)


keys = get_keys()

flickr.set_keys(api_key = keys[0], api_secret = keys[1])

if path.exists(".auth") :
    flickr.set_auth_handler(".auth")
else:
    authflickr()


up = upload()

print("Photo Successfully Uploaded photo with id : {}  ".format(up.id))


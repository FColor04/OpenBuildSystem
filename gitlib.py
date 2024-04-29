from github import Auth
from github import Github
from github import GithubIntegration
import os
from os.path import exists
import dotenv
dot = None

def load_dotenv():
    if exists(".env"):
        dotenv_file = dotenv.find_dotenv()
    else:
        with open(".env", "w+"): pass
        dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)
    return dotenv_file

def set_key(key="", dotenv_file=""):
    os.environ["key"] = key
    #print(os.environ['key'])
    dotenv.set_key(dotenv_file, "key", os.environ["key"])

dot = load_dotenv()
def login_github():
    try:
        os.environ["key"]
    except:
        print("no key")
        return -1
    auth = Auth.Token(os.environ["key"])
    g = Github(auth=auth)
    print(g.get_user().login)
    return g

if __name__ == "__main__":
    load_github()
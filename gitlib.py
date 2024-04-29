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
    repos = []
    with open("git.repos", 'w+') as f:
        for repo in g.get_user().get_repos():
            print(repo.name)
            try: top = repo.get_topics()
            except: top = []
            if "openbs" in top:
                repos.append(repo)
        for i in repos:
            f.write(i.full_name+"\n")
    return g, repos

if __name__ == "__main__":
    _, r = login_github()
    print(r)
    print(r[0].get_contents('test1').decoded_content)
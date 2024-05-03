from github import Auth
from github import Github
from github import GithubIntegration
import os
from os.path import exists
import dotenv
from json import loads
from git import Repo
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
def login_github(keys=''):
    global dot
    try:
        k = os.environ["key"]
    except:
        k = keys
        set_key(k, dot)
        return -1
    auth = Auth.Token(k)
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

def get_repo_data(reps):
    print(reps)
    repo_data = []
    for i in reps:
        repo_data.append([loads(i.get_contents('makefile.obs').decoded_content.decode("ascii")), i])
    return repo_data

def clone_repo(repo, path):
    repo_path = "https://github.com/"+repo.full_name
    try: repo = Repo.clone_from(repo_path, path)
    except: repo = Repo.init(path)
    return repo


if __name__ == "__main__":
    _, reps = login_github()
    repo_data = get_repo_data(reps)
    rep = clone_repo(repo_data[0][1], "C:/Users/R9_Dev/TestRepo")
    print(rep)
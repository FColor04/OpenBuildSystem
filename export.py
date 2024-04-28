import json
from subprocess import run
from os import chdir

def export(path="TestProj/Test", platform='Windows'):
    chdir(path)
    with open("makefile.obs") as f:
        settings = json.loads(f.read())
    print(settings)
    run(['godot', '--export-'+settings["exp_type"], platform, settings["exp_path"]])

def write_settings(set_path="TestProj/Test/", export_type="release",
    export_path='absolute/path/to/project.exe'):
    settings = {}
    settings["exp_path"] = export_path
    settings["exp_type"] = export_type
    p = set_path
    if p.endswith("/"):
        p += "makefile.obs"
    else:
        p += "/makefile.obs"
    with open(p, "w+") as f:
        f.write(json.dumps(settings))

if __name__ == "__main__":
    write_settings()
    export()
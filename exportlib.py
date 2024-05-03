import json
from subprocess import run
from os import chdir

def read_settings(path="TestProj/Test"):
    p = path
    if p.endswith("/"):
        p += ""
    else:
        p += "/"
    with open(p+'makefile.obs') as f:
        settings = json.loads(f.read())
    return settings

def export(path="TestProj/Test", platform='Windows'):
    settings = read_settings(path)
    print(settings)
    chdir(settings['proj_path'])
    args = ['godot', '--export-'+settings["exp_type"], f'{platform}', settings["exp_path"]]
    if bool(settings['headless']):
        args.append("--headless")
    run(args)
    return settings['exp_path']

def write_settings(set_path="TestProj/Test/", export_type="release",
    export_path='absolute/path/to/project.exe', headless=True):
    settings = {}
    settings["exp_path"] = export_path
    settings["exp_type"] = export_type
    settings['headless'] = headless
    settings['proj_path'] = set_path
    p = set_path
    if p.endswith("makefile.obs"):
        pass
    elif p.endswith("/"):
        p += "makefile.obs"
    else:
        p += "/makefile.obs"
    with open(p, "w+") as f:
        f.write(json.dumps(settings))

if __name__ == "__main__":
    print(json.dumps(write_settings(export_path='TestProj/test.exe')))
    export()
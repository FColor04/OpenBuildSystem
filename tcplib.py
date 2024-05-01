import easySocket as es
import json
import exportlib as ex
from subprocess import run
from os import getcwd
host = "127.0.0.1"
port = 65432

def start_client(platform="Windows"):
    data = {"platform": platform}
    conn = es.connect_tcp(host, port)
    es.send_text(json.dumps(data), conn)
    run("send/sendserver.exe")

def start_server(path="TestProj/Test"):
    conn = es.host_tcp(host, port)
    data = json.loads(es.rcv_data(conn).decode())["platform"]
    print(data)
    p = ex.export(path, data)
    cwd = getcwd()
    print(cwd)
    run(["sendclient.exe", str(conn.getsockname()[0]), p])
    pass

start_client()
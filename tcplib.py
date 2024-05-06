import easySocket as es
import json
import exportlib as ex
import lzmalib as xz
from subprocess import run
from os import getcwd
import udplib as udp
host = "127.0.0.1"
port = 65432

def start_client(output="test.exe", platform="Windows"):
    data = {"platform": platform}
    conn = es.connect_tcp(host, port)
    es.send_text(json.dumps(data), conn)
    run("send/sendserver.exe")
    xz.decompress_file("output.xz", output)

def start_server(path="TestProj/Test"):
    udp.start_client("add")
    while True:
        conn = es.host_tcp(host, port)
        if es.rcv_data(conn) == b'':
            break
        data = json.loads(es.rcv_data(conn).decode())["platform"]
        print(data)
        p = ex.export(path, data)
        xz.compress_file(p, "output.xz")
        cwd = getcwd()
        print(cwd)
        run(["E:\Rares\GitHub\OpenBuildSystem\sendclient.exe", str(conn.getsockname()[0]), "output.xz"])
    udp.start_client("remove")

if __name__ == "__main__":
    start_client()
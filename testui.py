import PySimpleGUI as sg
import gitlib as g
import tcplib as tcp
import udplib as udp

window = None
def main_ui():
    global window
    sg.theme('DarkAmber')
    layout = [  [sg.Button('Login Github'), sg.InputText()],
                [sg.Button("Start Host"), sg.Button('Start Client')],
                [sg.Button("Start Server")],
                [sg.InputText("127.0.0.1", key="ip")], [sg.InputText("TestProj/Test", key="path")],
                [sg.Text("", key="text")] ]
    window = sg.Window('Main', layout, size=(300, 200))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            return 0
        if event == 'Login Github':
            user, reps = g.login_github(values[0])
            window['text'].update("Github logged in")
            window.close()
            github_ui(user, reps)
            return 0
        elif event == "Start Host":
            print(values["ip"], values["ip"])
            tcp.host = values["ip"]
            tcp.start_server(values["path"])
        elif event == 'Start Client':
            print(values["ip"], values["ip"])
            tcp.host = values["ip"]
            tcp.start_client(values["path"])
            window['text'].update("Got build successfully")
        elif event == "Start Server":
            udp.localIP = values["ip"]
            window.close()
            udp.start_server()

def github_ui(user, reps):
    global window
    sg.theme('DarkAmber')
    layout = [[]]
    for i in range(len(reps)):
        layout.append([sg.Button(reps[i].full_name, key=i)])
    window = sg.Window('Github', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event in range(len(reps)):
            print(reps[event])

if __name__ == "__main__":
    main_ui()
import threading
import watchfiles
import webview
import json
set_data: dict = {}

def watch_and_reload(window, event):
    #debug
    window.load_url("settings/index.html")
    for change in watchfiles.watch('gui', stop_event=event):
        # using this instead of window.load_url() because that didn't work for me
        window.evaluate_js('window.location.reload()')

class api:
    def gh_click(e):
        print("Github :)")
    def n_click(e):
        print("Node :)")
    def load_config(self):
        with open("settings.json", "r+") as f:
            data = json.loads(f.read())
        return data
    def save_config(self, config):
        global set_data
        print(config)
        for i in json.loads(config).keys():
            set_data[i] = json.loads(config)[i]
        with open("settings.json", "w+") as f:
            f.writelines(json.dumps(set_data))
        print("Store "+config)

if __name__ == '__main__':
    # Create a standard webview window
    window = webview.create_window(
        'Open Build System', 
        'gui/index.html',
        js_api=api()
    )
    # this handles stopping the watcher
    thread_running = threading.Event()

    # using a thread to watch
    reload_thread = threading.Thread(
        target=watch_and_reload,
        args=(window, thread_running)
    )
    reload_thread.start()

    # start the webview app
    webview.start(args=window, debug=True)

    # upon the webview app exitting, stop the watcher
    thread_running.set()
    reload_thread.join()

    print('exitted successfully!')

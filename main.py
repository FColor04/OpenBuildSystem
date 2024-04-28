import threading
import watchfiles
import webview


def watch_and_reload(window, event):
    for change in watchfiles.watch('gui', stop_event=event):
        # using this instead of window.load_url() because that didn't work for me
        window.evaluate_js('window.location.reload()')
        # window.load_url()


if __name__ == '__main__':
    # Create a standard webview window
    window = webview.create_window(
        'Open Build System', 'gui/index.html'
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
    webview.start(debug=True)

    # upon the webview app exitting, stop the watcher
    thread_running.set()
    reload_thread.join()

    print('exitted successfully!')

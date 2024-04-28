import webview
from exportlib import write_settings


def on_start():
    window.load_url("settings/index.html")


if __name__ == '__main__':
    # Create a standard webview window
    window = webview.create_window(
        'Test', 'gui/index.html'
    )
    webview.start(on_start, debug=True)

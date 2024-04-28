import webview
from exportlib import write_settings

if __name__ == '__main__':
    # Create a standard webview window
    webview.create_window(
        'Test', 'gui/settings/index.html', confirm_close=True
    )
    webview.start()
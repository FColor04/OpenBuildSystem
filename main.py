import webview

if __name__ == '__main__':
    # Create a standard webview window
    webview.create_window(
        'Test', 'gui/index.html', confirm_close=True
    )
    webview.start()
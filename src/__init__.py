from .uttils import screeRecording
import webview

html = open("src/window.html", "r").read()


def loadcss(window):
    with open("src/style.css") as f:
        window.load_css(f.read())


def mainWindow():
    Window = webview.create_window(
        "Free Screen Recording",
        html=html, confirm_close=True,
        js_api=screeRecording())
    webview.start(loadcss, Window)

import xbmc
import xbmcgui
import subprocess

def launch_moonlight():
    # Replace 'moonlight' with the full path to the Moonlight executable if needed.
    try:
        subprocess.Popen(['moonlight'])
    except Exception as e:
        xbmcgui.Dialog().ok("Error", str(e))

if __name__ == '__main__':
    dialog = xbmcgui.Dialog()
    if dialog.yesno("Launch Moonlight?", "Do you want to launch Moonlight?"):
        launch_moonlight()

import xbmc
import xbmcgui
import subprocess
import os

# Function to get moonlight path from environment variable
def get_moonlight_path():
    # Define the name of the environment variable
    env_var_name = "MOONLIGHT_PATH"

    # Get the value of the environment variable
    moonlight_path = os.getenv(env_var_name)

    if not moonlight_path:
        xbmcgui.Dialog().ok("Error", f"Environment variable {env_var_name} is not set.")
        return None

    # Ensure the path ends with the executable name (e.g., 'moonlight.exe' on Windows)
    if os.name == 'nt':
        moonlight_executable = "moonlight.exe"
    else:
        moonlight_executable = "moonlight"

    full_path = os.path.join(moonlight_path, moonlight_executable)

    # Check if the executable exists
    if not os.path.isfile(full_path):
        xbmcgui.Dialog().ok("Error", f"Moonlight executable not found at: {full_path}")
        return None

    return full_path


def launch_moonlight():
    # Replace 'moonlight' with the full path to the Moonlight executable if needed.
    try:
        moonlight_path = get_moonlight_path()
        if moonlight_path:
            subprocess.Popen([moonlight_path])
        else:
            xbmcgui.Dialog().ok("Error", "Failed to find Moonlight executable.")
    except Exception as e:
        xbmcgui.Dialog().ok("Error", str(e))


if __name__ == '__main__':
    dialog = xbmcgui.Dialog()
    if dialog.yesno("Launch Moonlight?", "Do you want to launch Moonlight?"):
        launch_moonlight()

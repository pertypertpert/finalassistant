import webbrowser
import datetime
def schedulezoom():
    with open('storage files\\minute.txt', 'r') as f:
        minute = f.read()
    with open('storage files\\hour.txt', 'r') as f:
        hour = f.read()
    with open('storage files\\link.txt', 'r') as f:
        link = f.read()
    timenow = datetime.datetime.now()
    currentmin = timenow.strftime('%M')
    currenthr=timenow.strftime('%H')
    if int(currenthr)== hour:
        if int(currentmin)==minute:
            webbrowser.open(link)

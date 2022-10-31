import webbrowser
import requests
try:
    requests.get('https://www.youtube.com').status_code
    print('Site acessível!')
except:
    print('Site não acessível!')

#webbrowser.open('bcfgbfd')

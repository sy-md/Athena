from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint
import json

"""
send a payload to a website to login as user
then prep the page content to be dislayed in the terminal for veiwing

"""

url = "https://accounts.pixiv.net/ajax/login?lang=en"
#url = "https://accounts.pixiv.net/login?return_to=https%3A%2F%2Fwww.pixiv.net%2Fen%2F&lang=en&source=pc&view_type=page"
payload = {
    'login_id': 'crazymartell@gmail.com',
    'password': '121200mdcDbbg',
    "source": "pc",
    "app_ios": "0",
    "ref": "",
    "return_to": "https://www.pixiv.net/en/",
    "lang": "en",
    "g_recaptcha_response": "",
    "recaptcha_enterprise_score_token": "03AFcWeA7oeQahWj6Wg6qH3tmuwxTmZxxfFMaFToNnxO6NtkjKXNre7o3m4u3fij7qnViuC3NAY42wrhdLL31TxIQ3JC3i93MqaH_hPLq9RoUzrhNYn9ZRlnvQsF4BhSWcNkOs4a5PMKBCtyCXGvpbAp9pVoXADiskmQL0tiE4SDscYMydirydbTytY6CuaV3mPhn0HZaloJkuoZYPME6p17AQvI5kODVug8IXTa2E0PwMm5CZf-B1knjet0auvzS7Gvn8eDjV3_lkR6ccoavl0ZdSAs2kdKgbVUk9DHv0uhLwvHkhHVsN-nNBmMCYSWCENn4RPKoIvvYMjRqmiwRgEHilznw-b5kbhRi7DnXq05_lPymUxlxbo7_VGPF0EhnBR4BZuQZptZwqLa1SuoK4Hgt1p4hfN3wn1xXMLz2oNxtWRYBNa17rdI9cM1R5ONHRyW2KJ3UFD6R7VhlEsqwbcZOJ29rymQxNubr-0ym8AAHDU60b59twt8Z_WW9IE…RN27I0rTd1Fe5s_BW7VfVgYCIiWr0kwxhR5OOluu1alhle7P6xAKdT5hmoZJ4zmiydU8SCcQQr05vFopjfqvwwou3OZ__1yZT8LEcL7ihGV-t6FAbw7iTg5aSi_NsNacmL20vTqpDY2BzSRlii8-nwEhqqUY8vtXiIS2bVx_PvTdWRRBF9AAUiswVk0WTOt82qdwrhBD_hYDJ1Phrvv3aDvhU72BKqiM5lJVwYtofiEiNdQLfAJGcna9jNrU-ri3XQly60JPTbWQzMuVhJ7d0O4rcgtOZqeJ0I1Ik-h5-a727Etzb6BV76-C_7gNkEMjz-vBpi44howvMzFbo3BaEuqpdRlPM3dZ9EnD7OfCLtuy0CV7fygy017rRMuVBZR_4wg5Zp8o91IDNKJtCzid7bUEsozDUhgqvYUxEZVMvOQBUfhr4IPBysNRCsUm00NEvHMb7WOrVCH38R3BWk9ZsfroyBl-YYJzhh-0QRNi5XkRFJWV_5noJOvqo40oQg",
    "tt": "406167b99c4ab0ff4fd2766ec90430a7"
}
jsdata = json.dumps(payload)
with requests.Session() as s:
    p = s.post(url, data = jsdata)
    print(p.status_code)
    pprint(p.text)

    with open('pixiv.html', 'w') as f:
        f.write(p.text)
        f.close()

import requests
import random


def send_otp_to_phone(phone):
    mOTP = random.randint(1000, 9999)
    params = {
        'authkey': '9cead05e00bf81ac',
        'country_code': '91',
        'mobile': str(phone),
        'otp': str(mOTP),
        'sid': '1082',
        'time': '30 Seconds',
        'company': 'RIT',
    }
    x = requests.get('https://api.authkey.io/request', params)
    return (mOTP, x.text)

# requests.get('https://api.authkey.io/request?authkey=9cead05e00bf81ac&mobile='+str(phone) +'&country_code=91&otp='+str(code)+'&sid=1082&time=5seconds&company=RIT')
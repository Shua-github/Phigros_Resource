import hashlib
from http.client import HTTPSConnection
import json
import random
import string
import time
import urllib.parse
import uuid

sample = string.ascii_lowercase + string.digits

def taptap(appid):
    uid = uuid.uuid4()
    X_UA = "V=1&PN=TapTap&VN=2.40.1-rel.100000&VN_CODE=240011000&LOC=CN&LANG=zh_CN&CH=default&UID=%s&NT=1&SR=1080x2030&DEB=Xiaomi&DEM=Redmi+Note+5&OSV=9" % uid
    
    conn = HTTPSConnection("api.taptapdada.com")
    conn.request(
        "GET",
        "/app/v2/detail-by-id/%d?X-UA=%s" % (appid, urllib.parse.quote(X_UA)),
        headers={"User-Agent": "okhttp/3.12.1"}
    )
    r = json.load(conn.getresponse())
    print(r["data"]["download"])
    apkid = r["data"]["download"]["apk_id"]

    print("")

    nonce = "".join(random.sample(sample, 5))
    t = int(time.time())
    byte = "X-UA=%s&abi=arm64-v8a,armeabi-v7a,armeabi&id=%d&node=%s&nonce=%s&sandbox=1&screen_densities=xhdpi&time=%sPeCkE6Fu0B10Vm9BKfPfANwCUAn5POcs" % (X_UA, apkid, uid, nonce, t)
    md5 = hashlib.md5(byte.encode()).hexdigest()
    body = "node=%s&sandbox=1&sign=%s&abi=arm64-v8a%%2Carmeabi-v7a%%2Carmeabi&time=%s&id=%d&nonce=%s&screen_densities=xhdpi" % (uid, md5, t, apkid, nonce)

    conn.request(
        "POST",
        "/apk/v1/detail?X-UA=" + urllib.parse.quote(X_UA),
        body=body.encode(),
        headers={"Content-Type": "application/x-www-form-urlencoded", "User-Agent": "okhttp/3.12.1"}
    )
    r = json.load(conn.getresponse())
    print(r)

# Phigros app id = 165287
if __name__ == "__main__":
    taptap(165287)


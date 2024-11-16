import time,logging

from mycelery.main import app

log = logging.getLogger("django")

@app.task
def start_pay(code):
    print("{}开始支付".format(code))
    time.sleep(5)
    return "{}支付完成".format(code)
import time

import flask


app = flask(__name__)

app.router("/",methods["GET"])
def index():
        print("ping")


if __main__ in __name__ :
    app.run(0.0.0.0:5000)
    print("现在时间时",time.time())

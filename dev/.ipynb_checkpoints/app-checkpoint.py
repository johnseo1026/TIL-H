from flask import Flask, render_template, Response
import cv2 as cv2


cam = cv2.VideoCapture(0)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/info')
def info():
    return render_template('info.html')


def stream():
    while 1 :
        __,frame = cam.read()
        imgencode = cv2.imencode('.jpg',frame)[1]
        stringData = imgencode.tostring()
        yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')
        

@app.route('/video')
def video():
    return Response(stream(),mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    # debug를 True로 세팅하면, 해당 서버 세팅 후에 코드가 바뀌어도 문제없이 실행됨. 
    app.run(host='127.0.0.1', port=8000, debug = True)
    
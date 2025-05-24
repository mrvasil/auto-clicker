from flask import Flask, render_template, jsonify
import pyautogui
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/press_right', methods=['POST'])
def press_right():
    pyautogui.press('right')
    return jsonify(success=True)

@app.route('/press_left', methods=['POST'])
def press_left():
    pyautogui.press('left')
    return jsonify(success=True)

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5252, debug=True)
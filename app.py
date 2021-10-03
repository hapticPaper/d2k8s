import platform, os
from flask import Flask, render_template, send_file

uname = platform.uname()
name = uname.node
systemOS = uname.system
release = uname.release
osVersion = uname.version
processor = uname.processor
pyver = platform.python_version()
machine = uname.machine
architecture = platform.architecture()

print(f"{platform.uname()=}")

print(f"\n\n{name=}, OS='{systemOS} {osVersion}', {processor=}\n")

FLASK_HOST = os.getenv('FLASK_HOST', '127.0.0.1')
FLASK_PORT = os.getenv('FLASK_PORT', 5001)

app = Flask("system info")


@app.route('/favicon.ico')
def foff():
    return send_file('favicon.ico')


@app.route('/')
def system_info():
    return render_template('system.html', name=name, os = f'{systemOS} {release}', osver=osVersion, machine = f'{machine}:{architecture}  {processor}', py=pyver)



if __name__=="__main__":
    app.run(FLASK_HOST, FLASK_PORT, debug=True)
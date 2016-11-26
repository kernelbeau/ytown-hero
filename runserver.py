import socket

from ytown import app


DEV_SERV = False
if socket.gethostname() in ['x551m',]: DEV_SERV = True

if DEV_SERV:
    app.run(debug=True)
else:
    app.run()

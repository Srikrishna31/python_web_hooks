from flask import Flask
import uuid
app = Flask(__name__, template_folder='templates')

app.secret_key = app.config['SECRET_KEY']
app.config.from_object('config')

# Setup the Flask SocketIO integration while mapping the Redis Server.
from flask_socketio import SocketIO
socketio = SocketIO(app, logger=True, engineio_logger=True, message_queue=app.config['BROKER_URL'])

# Createa a unique session ID and store it within the application configuration file
if not hasattr(app.config, 'uid'):
    sid = str(uuid.uuid4())
    app.config['uid'] = sid
    print(f"initialize_params - Session ID stored = {sid}")
from project import socketio
import threading
from datetime import datetime
from project.camera import capture_image
from project.database import save_to_db

@socketio.on('mouse_move')
def handle_mouse_move(json):
    x = json['x']
    y = json['y']

@socketio.on('mouse_click')
def handle_mouse_click(json):
    x = json.get('x')
    y = json.get('y')
    def process_click(x, y):
        image_path = capture_image()
        if image_path:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_to_db(timestamp, x, y, image_path)
            socketio.emit('new_image', {'image_path': image_path})

    threading.Thread(target=process_click, args=(x, y)).start()

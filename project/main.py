from project import app, socketio
from project.database import init_db

# Initialize the database
init_db()

if __name__ == '__main__':
    print("Starting server...")
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)

from app import app, db
from app.models import Day
from datetime import date

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

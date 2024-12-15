from app import app

if __name__ == '__main__':
    app.config['SERVER_NAME']='localhost:5000'
    app.run(host='0.0.0.0', port=5000)

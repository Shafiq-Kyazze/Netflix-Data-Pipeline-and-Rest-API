from main.init import _init_app

app = _init_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)    #Port set to 5000 since app is in development
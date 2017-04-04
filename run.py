from application import create_app

app = create_app(dict(
    TESTING=True,  # Propagate exceptions
    BOOKCLOUD_URL_PREFIX = '',
))

app.run(debug=True)

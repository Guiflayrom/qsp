SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Basic': {
            'type': 'basic',
            'authorizationUrl': '/api/v1/token',
        },
        'Bearer': {'type': 'apiKey', 'name': 'Authorization', 'in': 'header'},
    }
}

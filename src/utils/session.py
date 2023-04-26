from flask import Flask, request, session, jsonify

class SessionVerifier:
    def __init__(self, app):
        self.app = app

    def __call__(self, request):
        if not request.session or not request.session.valid:
            return jsonify({'error': 'Session invalid'})
        return self.app.response_class(request)


class Response:
    header = {
        'Access-Control-Allow-Origin':"*"
    }
    def __init__(self, body=None, message="", status="success"):
        if body is None:
            body = {}
        self.body = body
        self.message = message
        self.status = status

    def json(self):
        return {"body": self.body, "message": {"string": self.message}, "status": self.status}


users_schema ={
        "id": {'type': 'integer', 'required': True},
        "name": {'type': 'string'},
        "email": {'type': 'string'},
        "gender": {'type': 'string'},
        "status": {'type': 'string'}
    }

posts_schema ={
        "id": {'type': 'integer', 'required': True},
        "user_id": {'type': 'integer', 'required': True},
        "title": {'type': 'string'},
        "body": {'type': 'string'}
    }
from cerberus import Validator  # A library used to help schema validations


def schema_data_validator(response, schema):
    if type(response) is list:
        for post in response:
            validator = Validator(schema, required_all=True)
            is_valid = validator.validate(post)
            return is_valid, validator.errors

    validator = Validator(schema, required_all=True)
    is_valid = validator.validate(response)
    return is_valid, validator.errors




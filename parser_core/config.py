import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

def kafka_broker():
    return env("KAFKA_BROKER")

def kafka_coupon_parser_queue_via_api():
    return env("KAFKA_COUPON_PARSER_VIA_API_TOPIC")

def kafka_coupon_parser_queue():
    return env("KAFKA_COUPON_PARSER_TOPIC")
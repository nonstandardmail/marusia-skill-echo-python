import json


def webhook(event, context):
    request_message = json.loads(event['body'])
    derived_session_fields = ['session_id', 'user_id', 'message_id']
    response_message = {
        "response": {
            "text": request_message['request']['original_utterance'],
            "tts": request_message['request']['original_utterance'],
            "end_session": False
        },
        "session": {derived_key: request_message['session'][derived_key] for derived_key in derived_session_fields},
        "version": request_message['version']
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response_message)
    }

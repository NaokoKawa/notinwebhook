def lambda_handler(event, context):
    
    # Slack��Event API�̔F��
    if "challenge" in event:
        return event["challenge"]
    
    return "OK"    
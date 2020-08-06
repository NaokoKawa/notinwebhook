def lambda_handler(event, context):
    
    # Slack‚ÌEvent API‚Ì”FØ
    if "challenge" in event:
        return event["challenge"]
    
    return "OK"    
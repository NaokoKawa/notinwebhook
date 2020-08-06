import os
import json
import logging
import urllib.request

# ���O�ݒ�
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle_slack_event(slack_event: dict, context) -> str:

    # �󂯎�����C�x���g����Cloud Watch���O�ɏo��
    logging.info(json.dumps(slack_event))

    # Event API�̔F��
    if "challenge" in slack_event:
        return slack_event.get("challenge")
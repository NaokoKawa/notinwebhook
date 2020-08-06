import os
import json
import logging
import urllib.request

# ログ設定
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle_slack_event(slack_event: dict, context) -> str:

    # 受け取ったイベント情報をCloud Watchログに出力
    logging.info(json.dumps(slack_event))

    # Event APIの認証
    if "challenge" in slack_event:
        return slack_event.get("challenge")
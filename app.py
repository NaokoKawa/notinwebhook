import os
import json
import logging
import urllib.request

# ログ設定
logger = logging.getLogger()
logger.setLevel(logging.INFO)

@app.route('/create_todo', methods=['GET'])
def create_todo(slack_event: dict, context) -> str:

    # 受け取ったイベント情報をCloud Watchログに出力
    logging.info(json.dumps(slack_event))

    # Event APIの認証
    if "challenge" in slack_event:
        return slack_event.get("challenge")
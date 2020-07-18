from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('54ba17966a993fc3683b024177b1e531', None)
channel_access_token = os.getenv('cRVRJumImCqMw/C1rYMhrKlYwqVVfxOareWpJYgyi1GEpt+HoulZrhqhxckPDFPaDn9sUBwrDQelKhutRqQeMtv2hmaebevwj0GQjEZAPjhCUskFf1OcZhvSZkG06bdJOvM9X68xYwGbc0FTiuNjRgdB04t89/1O/w1cDnyilFU=', None)
if channel_secret is None or channel_access_token is None:
    print('Specify 54ba17966a993fc3683b024177b1e531 and cRVRJumImCqMw/C1rYMhrKlYwqVVfxOareWpJYgyi1GEpt+HoulZrhqhxckPDFPaDn9sUBwrDQelKhutRqQeMtv2hmaebevwj0GQjEZAPjhCUskFf1OcZhvSZkG06bdJOvM9X68xYwGbc0FTiuNjRgdB04t89/1O/w1cDnyilFU= as environment variables.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

# 此為 Webhook callback endpoint
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body（負責）
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

# decorator 負責判斷 event 為 MessageEvent 實例，event.message 為 TextMessage 實例。所以此為處理 TextMessage 的 handler
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 決定要回傳什麼 Component 到 Channel
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == '__main__':
    app.run()
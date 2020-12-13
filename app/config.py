import traceback
import json
import sys
import os


try:
    port = 8080
except ValueError:
    port = -1
if not 1 <= port <= 65535:
    print("Please make sure the PORT environment variable is an integer between 1 and 65535")
    sys.exit(1)

try:
    api_id =1064864
    api_hash = "5f3eeab0e6108731551e6a93598b654c"
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the API_ID and API_HASH environment variables correctly")
    print("You can get your own API keys at https://my.telegram.org/apps")
    sys.exit(1)

try:
    # index_settings_str = os.environ["INDEX_SETTINGS"].strip()

    # index_settings = json.loads(index_settings_str)

    index_settings = {
      "index_all":  True,
      "index_private":True,
      "index_group": True,
      "index_channel": True,
      "exclude_chats": [],
      "include_chats": "{1023178134,476789253}",#my index chat
      "otg": {
          "enable": True,
          "include_private": True,
          "include_group": True,
          "include_channel": True
      }
    }
    otg_settings = index_settings['otg']
    enable_otg = otg_settings['enable']
except:
    traceback.print_exc()
    print("\n\nPlease set the INDEX_SETTINGS environment variable correctly")
    sys.exit(1)

try:
    session_string = "1BVtsOGYBu1ijKv7wR_zpGJZxsJ4kSyfRONQ_6_Qg7aqH9fgoFq0kkiDjku9S8po0Q7rNmxSi28-nAs4mMUVvoPMxLYEaMSL9rozXfIl_hejtUoIvNIE7YEsjUqGAQHSQeKysdUcE2b4gmxKJAPDM7vGoSkb8bdOFCVryvpGHObePHAPiFSZJp0D0nz7bx33CyA4fLegOhkVuO5Mjz50BGiOGItC-UBjHyCkoii0bBEaGMLUfO8ZsHol7eIz3dj1bT_nv5WFDf25booFz888-VcwnKcwVX-DuK8hRnoVWO5XpNjWojeAHMe66mAEY_Gts___iBs8LXrhkm_wi1u7Zxz4o7wrJxqg="
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the SESSION_STRING environment variable correctly")
    sys.exit(1)

# try:
#     bot_token = os.environ["BOT_TOKEN"]
# except (KeyError, ValueError):
#     traceback.print_exc()
#     print("\n\nPlease set the BOT_TOKEN environment variable correctly")
#     sys.exit(1)



host = "162.241.87.250"
debug = bool(os.environ.get("DEBUG"))
chat_ids = []
alias_ids = []

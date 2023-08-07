from clauderevised.claude import ClaudeAPIWrapper
import requests
import json
import random






response = requests.get('https://huggingface.co/datasets/qinzhu/cyber_config/raw/main/config/sd_server_config.txt')
configs = json.loads(response.text)


start = 0
for session_key_config in configs['free_session_keys']:
  session_key = session_key_config['sessionKey']
  api = ClaudeAPIWrapper(session_key)
  organizations = api.get_organizations()
  print(organizations)
  if len(organizations[0]["active_flags"])>0:
    api.get_flags(organizations[0]["uuid"],organizations[0]["active_flags"])

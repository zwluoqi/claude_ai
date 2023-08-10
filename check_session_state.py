from clauderevised.claude import ClaudeAPIWrapper
import requests
import json
import random

import collections




response = requests.get('https://huggingface.co/datasets/qinzhu/cyber_config/raw/main/config/sd_server_config.txt')
configs = json.loads(response.text)


start = 0
for session_key_config in configs['free_session_keys']:
  start +=1
  if start<42:
    continue
  session_key = session_key_config['sessionKey']
  api = ClaudeAPIWrapper(session_key)
  organizations = api.get_organizations()
  print(organizations)
  # if isinstance(organizations, collections.abc.Sequence):
  #   continue
  try:
    if len(organizations[0]["active_flags"])>0:
      api.diss_flags(organizations[0]["uuid"],organizations[0]["active_flags"])
  except Exception as e:
    print('error')
    with open('failed.txt', 'a') as file:
      # 添加一行数据
      file.write(str(session_key_config)+'\n')     


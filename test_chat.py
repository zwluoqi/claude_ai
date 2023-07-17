from myclaude.claude import ClaudeAPIWrapper

session_key = "sessionKey=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; intercom-device-id-lupk8zyo=9293f49e-fdf2-4cf2-b91f-fbcdc1535cd6; __cf_bm=RkJAj_t0XMWQ_EqN8nazSkKoWD1GihDx2AhkMWwDy64-1689556735-0-Ab5BJgrbMoPTB7KXjfLR6ZniCMMIPbgA01JWt5Lu5K8ysKbAJcHqDPrEfdZYkL+w+RfiDIl6yvNBRd7TKUMd4K8=; intercom-session-lupk8zyo=UVJoVCtiMTQrSDMzTk52UWxOWndEa056aGJQRzcxejFhUi9CS0FKckU2NmpzNkNXWjhPSDFwU0ptSklzYnRCeC0tejl4STNoZmVteDVEQkxYazZ6amo2QT09--f0962ef87ec385257e6cd0ea4000e810441c5fbc"
api = ClaudeAPIWrapper(session_key)

# 获取组织
organizations = api.get_organizations()
print(organizations)

organization_uuid = organizations[0]["uuid"]

# 获取对话
conversations = api.get_chat_conversations(organization_uuid)
print(conversations)

# 创建对话
# conversation = api.add_chat_conversation(organization_uuid)
# print(conversation)


conversation_uuid = conversations[0]["uuid"]

# 发送消息
attachments = []
while True:
  message = input("You>>> ")
  # 如果是 /u 就是上传文件，获取文件路径
  if message.startswith("/u"):
    file_path = message[3:]
    # 去掉文件路径两边的空格
    file_path = file_path.strip()
    response = api.convert_document(file_path, organization_uuid)
    print(response)
    if response is not None:
      attachments.append(response)
      continue
  response = api.send_message(organization_uuid, conversation_uuid, message,
                              attachments)
  attachments = []
  print('Claude>>> ', end='')
  for message in response:
    print(message, end='', flush=True)
  print()

from clauderevised.claude import ClaudeAPIWrapper

#{"sessionKey": "sessionKey=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", "org": "b1a98f4c-c809-40d6-bbc6-3ed3fa9ab1e3"},
session_key = "sessionKey=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"
api = ClaudeAPIWrapper(session_key)

# organizations = api.get_organizations()
# print(organizations)

# organization_uuid = organizations[0]["uuid"]
organization_uuid = 'b1a98f4c-c809-40d6-bbc6-3ed3fa9ab1e3'

conversations = api.add_chat_conversation(organization_uuid,"good")
print(conversations)

conversation_uuid = conversations["uuid"]

attachments = []
while True:
  message = input("You>>> ")
  # If it's /u, then it's uploading a file, get the file path
  if message.startswith("/u"):
    file_path = message[3:]
    # Remove spaces from the file path
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
from clauderevised.claude import ClaudeAPIWrapper
import requests

# headers = {
#   'Content-Type': 'application/json',
#   'Cache-Control': 'no-cache',
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
#   }
# response = requests.get('https://api.openai.com/v1/chat/completions',headers=headers)
# print(response.json())


session_key = "sessionKey=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"
api = ClaudeAPIWrapper(session_key)

organizations = api.get_organizations()
print(organizations)

organization_uuid = organizations[0]["uuid"]
# organization_uuid = 'b2a66215-c7ea-4844-b9bf-ea5b9b100c86'


conversations = api.get_chat_conversations(organization_uuid)
print(conversations)

conversation_uuid = conversations[0]["uuid"]

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
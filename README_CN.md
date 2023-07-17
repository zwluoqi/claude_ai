# Claude AI Python Wrapper 用户指南

这个库提供了一个简单的方式来与Claude AI API进行交互。你可以使用它来获取组织，获取对话，发送消息和上传文件。

## 安装

首先，你需要安装这个库。你可以通过pip来进行安装：

```bash
pip install claude_ai
```

## 使用

首先，你需要从`claude_ai.claude`中导入`ClaudeAPIWrapper`类。然后，你可以使用你的会话密钥创建一个`ClaudeAPIWrapper`对象。

```python
from claude_ai.claude import ClaudeAPIWrapper

session_key = "你的会话密钥"
api = ClaudeAPIWrapper(session_key)
```

你可以在claude.ai网页上的任何请求的Cookie中找到会话密钥。它通常以"sessionKey=sk-ant-sid"开始。只需复制整个Cookie并将其粘贴作为你的会话密钥。

### 如何获取Cookie

1. 打开你的浏览器并访问claude.ai网站。
2. 使用你的凭据进行登录。
3. 打开浏览器的开发者工具（在大多数浏览器中是F12键）。
4. 转到Network（网络）选项卡。
5. 刷新页面。
6. 点击左侧的任何请求，然后在头部找到'Cookies'部分。
7. 复制整个Cookie。

然后，你可以使用这个对象获取你的组织：

```python
organizations = api.get_organizations()
print(organizations)

organization_uuid = organizations[0]["uuid"]
```

你也可以获取你的对话：

```python
conversations = api.get_chat_conversations(organization_uuid)
print(conversations)

conversation_uuid = conversations[0]["uuid"]
```

你可以使用`create_chat_conversation`函数来创建一个新的对话。你需要提供你的 `organization_uuid`，这是你的组织的唯一标识符。然后，这个函数会返回一个包含新对话信息的字典。

```python
new_conversation = api.create_chat_conversation(organization_uuid)
print(new_conversation)

conversation_uuid = new_conversation["uuid"]
```


这样修改后的用户指南应该包含了你提供的函数。如果你有其他的问题或者需要进一步的帮助，欢迎你随时向我提问。

然后，你可以发送消息。如果你需要上传文件，你可以使用`/u`命令，后面跟着文件路径：

```python
attachments = []
while True:
  message = input("You>>> ")
  # 如果是/u，那么它正在上传文件，获取文件路径
  if message.startswith("/u"):
    file_path = message[3:]
    # 从文件路径中删除空格
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
```

在这个例子中，你将从命令行输入你的消息。如果你的消息以`/u`开始，那么库将尝试上传你指定的文件。然后，它将把上传文件的响应添加到附件列表中。然后，它将发送一个新的消息，包含你的消息和所有附件。最后，它将打印出响应。

## 注意事项

确保你正确设置了你的会话密钥，否则你可能无法与Claude AI API进行交互。
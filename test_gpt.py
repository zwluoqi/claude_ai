import requests

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Authorization": "Bearer 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",
    "content-type": "application/json"
}
data = {
    "messages": "\n\system: Hello",
    "model": "gpt-3.5-turbo",
    "max_tokens_to_sample": 300,
}

response = requests.post(url, headers=headers, json=data)
print(response.text)
# cloudflare_ai_call
cloudflareで利用できるAIの呼び出しがほんの少しだけ楽になるモジュールです。
.envは下の.envを参考にしてください。
```.env
ACCOUNT_ID=YOUR_CLOUDFLARE_ACCOUNT_ID
API_TOKEN=YOUR_CLOUDFLARE_WORKERS_AI_API_TOKEN
```
使用例:
```python
from cloudflare_ai_call import call

if __name__ == "__main__":
    inputs = [
        { "role": "system", "content": "You are a friendly assistan that helps write stories" },
        { "role": "user", "content": "Write a short story about a llama that goes on a journey to find an orange cloud in japanese"}
    ];
    output = call("@cf/meta/llama-3-8b-instruct", inputs)
    print(output["result"]["responcse"])
```

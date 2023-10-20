
# import openai
#
#
#
# # Read the image file from disk and resize it
#
#
# OPENAI_API_KEY = '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'
#
# openai.api_key = OPENAI_API_KEY
#
#
# response =  openai.Completion.create(
#   engine="davinci",
#   prompt="Make a list of astronomical observatories:"
# )
#
# # res = response['choices'][0]['message']['content']
#
# print(response)

import openai

# 设置API凭证
# openai.api_key = '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'
openai.api_key = "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"
# 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
# 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

# 生成文本
prompt = "加拿大移民条件"
model = "text-davinci-003"
# model = "gpt-3.5-turbo"
response = openai.Completion.create(
    model=model,
    prompt=prompt,
    max_tokens=2048,
    temperature=0.9,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6
    )
generated_text = response.choices[0].text

# 打印生成的文本
print(generated_text)

# 参数说明：
# https://platform.openai.com/docs/api-reference/completions/create
# model: 要使用的模型的 ID，访问 OpenAI Docs Models 页面可以查看全部可用的模型
# prompt: 生成结果的提示文本，即你想要得到的内容描述
# max_tokens: 生成结果时的最大 tokens 数，不能超过模型的上下文长度
# temperature: 控制结果的随机性，如果希望结果更有创意可以尝试 0.9，或者希望有固定结果可以尝试 0.0
# https://blog.csdn.net/qq_42038623/article/details/129028552
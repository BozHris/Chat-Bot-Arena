import anthropic
from anthropic import HUMAN_PROMPT, AI_PROMPT
Clause_API_KEY = "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"

# output = anthropic.Anthropic(api_key=Clause_API_KEY).completions.create(
#     model="claude-2.1",
#     max_tokens_to_sample=100,
#     prompt=f"{HUMAN_PROMPT} What is the best way to quit smoking{AI_PROMPT}",
# )
# print(output.completion)
from wrapper.llm import MistralLLM

llm = MistralLLM()

response = llm.generate(
    "Explain Machine learning in brief."
)

print("\n")
print("=" * 80)
print(response)
print("=" * 80)
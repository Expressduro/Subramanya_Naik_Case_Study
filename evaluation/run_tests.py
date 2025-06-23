import json
from main import analyze_article

with open("evaluation/test_cases.json", "r") as f:
    test_cases = json.load(f)

for i, article in enumerate(test_cases):
    print(f"\n--- Test Case {i + 1} ({article['article_id']}) ---")
    full_text = f"{article['headline']}\n\n{article['content']}"
    result = analyze_article(full_text)
    print(result.model_dump_json(indent=2))

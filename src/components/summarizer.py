import re
from operator import mod
from transformers import pipeline

from src.components.title_generation import title_generation


def summarize(data):
    print("[!] Server logs: Summarizer Engine has started")
    text = data["article"]
    to_tokanize = text
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    summarized = summarizer(to_tokanize, min_length=75, max_length=300)
    tmp = " ".join([str(i) for i in summarized])
    tmp = tmp.replace("{", "")
    tmp = tmp.replace("''", "")
    tmp = tmp.replace("\x92", "")
    regex_pattern = r"(?<='summary_text': ' )(.*)(?='})"
    result = re.search(regex_pattern, tmp).group(0)
    data["summary"] = result
    print("[!] Server logs: Summarized article")
    data = title_generation(data)
    return data
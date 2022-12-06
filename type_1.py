# Load Packages
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer


def summarize_text(text):
    # Creating text parser using tokenization
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    # Summarize using sumy TextRank
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, 2)

    text_summary = ""
    for sentence in summary:
        text_summary += str(sentence)

    return text_summary
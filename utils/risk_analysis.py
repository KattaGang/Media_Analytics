import spacy
from newsapi import NewsApiClient
API_KEY = 'd83a0fb9e3104414a3693c6c4fdab735'
COMPANY_NAME = 'exxon-mobile'


nlp = spacy.load('en_core_web_md')

RISK_WORDS = ['delayed', 'snag', 'effectiveness', 'safety', 'injured',
              'security', 'emergency', 'technical issue', 'safety cocerns']
RISK_TOKENS = []


def setup():
    for risk_word in RISK_WORDS:
        doc = nlp(risk_word)
        for risk_token in doc:
            RISK_TOKENS.append(risk_token)
        for risk_token in doc.ents:
            print(risk_token)
            RISK_TOKENS.append(risk_token)
    print(RISK_TOKENS)


def get_score_text(text, company_name):
    doc = nlp(text)
    score = 0
    for risk_token in RISK_TOKENS:
        score = max(score, risk_token.similarity(doc))
    return score


def get_score_token(token, company_name):
    score = 0
    for risk_token in RISK_TOKENS:
        score = max(score, token.similarity(risk_token))
    return score


def get_score_sentence(sentence, company_name):
    score = 0
    for token in sentence:
        score += get_score_token(token, company_name)
    score /= len(sentence)
    return int(100 * score)


def get_score_article(article, company_name):
    doc = nlp(article)
    score = 0
    for sentence in doc.sents:
        score += get_score_sentence(sentence, company_name)
    score /= len(list(doc.sents))
    return score

def get_risky_lines_article(article, threshold, company_name):
    numlines = 0
    for sent in nlp(article).sents:
        if get_score_sentence(sent, company_name) >= threshold:
            numlines += 1
    return numlines



setup()

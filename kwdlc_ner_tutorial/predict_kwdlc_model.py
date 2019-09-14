import nagisa

ner_tagger = nagisa.Tagger(
    vocabs="data/kwdlc_ner_model.vocabs",
    params="data/kwdlc_ner_model.params",
    hp="data/kwdlc_ner_model.hp"
)

text = "FacebookのAIラボ所長でもあるヤン・ルカン博士"
tokens = ner_tagger.tagging(text)
print(tokens)

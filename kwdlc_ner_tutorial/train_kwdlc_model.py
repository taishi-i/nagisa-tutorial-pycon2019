import nagisa

nagisa.fit(
    train_file="data/kwdlc.train",
    dev_file="data/kwdlc.dev",
    test_file="data/kwdlc.test",
    model_name="data/kwdlc_ner_model"
)

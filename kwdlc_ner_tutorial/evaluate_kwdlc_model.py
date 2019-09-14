import nagisa

from seqeval.metrics import classification_report


def main():
    ner_tagger = nagisa.Tagger(
        vocabs='data/kwdlc_ner_model.vocabs',
        params='data/kwdlc_ner_model.params',
        hp='data/kwdlc_ner_model.hp'
    )

    fn_in_test = "data/kwdlc.test"
    test_X, test_Y = nagisa.utils.load_file(fn_in_test)

    true_Y = []
    pred_Y = []
    for x, true_y in zip(test_X, test_Y):
        pred_y = ner_tagger.decode(x)
        true_Y += true_y
        pred_Y += pred_y

    report = classification_report(true_Y, pred_Y)
    print(report)


if __name__ == "__main__":
    main()

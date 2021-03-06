<p align="center"><img width="40%" src="/data/images/pycon2019.png" /></p>


# Python による日本語自然言語処理  〜系列ラベリングによる実世界テキスト分析〜
- 発表スケジュール: 2019/09/16 14:40-15:10 (30min)
- 場所: [D会議室](https://www.pio-ota.net/facilities/kaigi_d/)
- レベル: Beginner
- 発表/資料: JP
- 発表スライド: [nagisa-tutorial-pycon2019.pdf](nagisa-tutorial-pycon2019.pdf)
- Speaker Deck: [Slides](https://speakerdeck.com/taishii/pycon-jp-2019)


## nagisa による単語分割と品詞タグ付けの実装方法
1. 基本的な使い方: [basic_usage.ipynb](notebooks/basic_usage.ipynb) [[Colab notebook](https://colab.research.google.com/github/taishi-i/nagisa-tutorial-pycon2019/blob/master/notebooks/basic_usage.ipynb?hl=ja)]
2. ワードクラウドの作成: [word_cloud.ipynb](notebooks/word_cloud.ipynb) [[Colab notebook](https://colab.research.google.com/github/taishi-i/nagisa-tutorial-pycon2019/blob/master/notebooks/word_cloud.ipynb?hl=ja)]

<a href="nagisa-tutorial-pycon2019.pdf">
    <p align="center">
        <img width="75%" src="/data/images/nagisa_example.png" />
    </p>
</a>


## Python による固有表現抽出モデルの実装方法
1. 事前準備: [Speaker Deck](https://speakerdeck.com/taishii/pycon-jp-2019?slide=66)
2. 京都大学ウェブ文書リードコーパスの前処理: [preprocess_kwdlc.py](kwdlc_ner_tutorial/preprocess_kwdlc.py)
3. 固有表現抽出モデルの学習: [train_kwdlc_model.py](kwdlc_ner_tutorial/train_kwdlc_model.py)
4. 学習済みモデルの利用方法: [predict_kwdlc_model.py](kwdlc_ner_tutorial/predict_kwdlc_model.py)
5. 固有表現ごとの正解率の確認: [evaluate_kwdlc_model.py](kwdlc_ner_tutorial/evaluate_kwdlc_model.py)


<a href="nagisa-tutorial-pycon2019.pdf">
    <p align="center">
        <img width="75%" src="/data/images/ner_example.png" />
    </p>
</a>


## 参考リンク
- [nagisa](https://github.com/taishi-i/nagisa)
- [Pythonで動く形態素解析ツール「nagisa」を使ってみた](https://upura.hatenablog.com/entry/2018/09/18/203540)
- [【かなり便利】形態素解析ツールのnagisa（なぎさ）を知っていますか？【Mecabより簡単】](https://yolo.love/nlp/nagisa/)
- [PyCon2019 レポート Python による日本語自然言語処理 〜系列ラベリングによる実世界テキスト分析〜](https://qiita.com/hassaku_63/items/a08fdaf5c7268415984e)
- [Windows でインストールに失敗する場合: "pip install nagisa"でいろいろやった話](https://qiita.com/F_murasaki/items/9359cab8dd56a30c885e)

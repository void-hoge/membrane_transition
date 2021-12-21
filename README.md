# MEMBRANE TRANSITION

## 実行
- Python3, pygame, Pillow, matplotlibを使用。
  - pygameはゲームを作るためのクロスプラットフォームモジュール群
  - `$ pip3 install pygame`でインストール
- `$ ./main.py`で実行
  - レンダリング、グラフの構成、GUIでの表示を全て行える。

---
## プログラム構成
### render.py
- DBfigures/allpics.txtに記載された数式をレンダリングする。
- 前回実行時の数式などの状態をprev.txtに保存しておき、更新があった要素のみをレンダリングする。
- prev.txtを削除すると、全ての式をレンダリングし直す。

### graph.py
- DBfigures/graph.txtに記載された辺の情報からgraphクラスのインスタンスを生成する。

### main.py
- 上記2つのプログラムを用いてGUIを操作する。

---
## 画像の用意

使用する画像は、全て`DBfigures/`直下に置く必要がある。

拡張子は`.png`のみをサポートしている。

---
## 式の制約
`DBfigures/allpics.txt`と`DBfigures/graph.txt`に記入するlatexの式は全て、スペースやタブ文字を含むことができない。

---
## DBfigures/allpics.txt
画像を一括で読み込むためのテーブル。行ごとの順序は問わない。

各行は`画像のbasename latex式`か、`rule_変換規則名 latex式`で構成される。
- `画像のbasename latex式`
  - 読み込みたい画像と、その状態を表す式を表現する。
  - 画像のbasenameとは、拡張子を除いた名前のこと
    - 例えば、`figX.png`が、`$hogepoyo$`の時、その行は`figX $hogepoyo$`となる。
    - この時、`DBfigures/figX.png`がmain.pyで読み込まれ、render.pyで`DBfigures/figX_fml.png`が生成される。
- `rule_変換規則名 latex式`
  - 変換規則と、その状態を表す式を表現する。
  - 変換規則名はファイルとして保存するためだけのもので、先頭が`rule_`となっていて、重複がないならなんでも良い。(main.pyでは、式そのものをキーとした辞書を使うため)
    - 例えば、`$(TU)$`というルールの式を生成するとき、`rule_TU $(TU)$`とする。(`rule_TU`のところは`rule_*`の形を満たせばなんでも良い。)
    - この時、`DBfigures/rule_TU_fml.png`が生成される。

---
## DBfigures/graph.txt
遷移を行う有向辺を記述するテーブル。1行目は初期状態から始まる辺である必要があるが、その他の順序は自由

各行は`src dst highlighted x y rule`で構成される。
- `src`
  - 遷移前の画像のbasename
- `dst`
  - 遷移後の画像のbasename
- `highlighted`
  - 変化する部分をハイライトした画像のbasename
- `x y`
  - 選択するときに中心とする座標(highlightedのハイライトされた場所の中心)
  - 画像の左上を(0,0)、右下を(1,1)とする(下図)
```
(0,0)---(1,0)
　|       |
　|       |
　|       |
(0,1)---(1,1)
```

- `rule`
  - 使用するルールの式(画像の名前ではない)
- 例
  - `fig1.png`から`fig2.png`への辺で、ハイライトされた画像が`fig1_fig2.png`、座標が(0.5, 0.2)、ルールが`$(Cm^{+})$`の時
  - `fig1 fig2 fig1_fig2 0.5 0.2 $(Cm^{+})$`
  - この行をファイルの先頭に置くと、それが初期状態になる。

---
## 操作
- 左上から画像が表示される。
- 最も下にある画像にマウスオーバーすると、マウスの場所と最も近い変化点を持つ候補が表示される。
- その状態でクリックすると、その状態が適用され、変化を行なった画像が一つ追加される。
- j, kまたはマウスホイールでスクロール、qで終了(lessと同じ操作)
- h, lで左右に移動
- uでundo、rでreset

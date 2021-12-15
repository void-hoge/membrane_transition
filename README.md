# MEMBRANE TRANSITION

## 実行
- Python3, pygame, Pillow, matplotlibを使用。
  - pygameはゲームを作るためのクロスプラットフォームモジュール群
  - `$ pip3 install pygame`でインストール
- `$ ./main.py`で実行

## DB設定
- `DBfigures/graph.txt`に辺の情報を記述
  - 1行は`src dst highlighted x y`のように記述される。
  - src, dstは有向辺のsrcとdst
  - highlightedはdstに至るために変形するsrcの部分をハイライトした画像
  - x, yはhighlightedの場所を選択するための座標(画像の左上を(0,0)、右下を(1,1)とした座標)
- `DBfigures/allpics.txt`に画像ファイルの一覧と、数式一覧
  - 各行は、`画像の名前 式`で記述する。
    - 式は、スペースを含まないように記述する必要がある。(そのうち改善するかも)
  - これを使って画像を一括で読み込む。
  - 式は、matplotlibでlatexをレンダリングして、espに出力して、その後Pillowでpngに変換、そのpngをpygameで読み込んでいる。
    - matplotlibでeps,psへの出力でしか`\textcolor`が使えない問題があり、それによってこのようなことをやる羽目になっている。
    - https://github.com/matplotlib/matplotlib/issues/6724

## 操作
- 左上から画像が表示される。
- 最も下にある画像にマウスオーバーすると、マウスの場所と最も近い変化点を持つ候補が表示される。
- その状態でクリックすると、その状態が適用され、変化を行なった画像が一つ追加される。
- j, kまたはマウスホイールでスクロール、qで終了(lessと同じ操作)
- h, lで左右に移動
- uでundo、rでreset

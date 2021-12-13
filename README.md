# MEMBRANE TRANSITION

## 実行
- Python3, pygameを使用。
  - pygameはゲームを作るためのクロスプラットフォームモジュール群
  - `$ pip3 install pygame`でインストール
- `$ ./main.py`で実行

## DB設定
- `DBfigures/graph.txt`に辺の情報を記述
  - 1行は`src dst highlighted x y`のように記述される。
  - src, dstは有向辺のsrcとdst
  - highlightedはdstに至るために変形するsrcの部分をハイライトした画像
  - x, yはhighlightedの場所を選択するための座標(画像の左上を(0,0)、右下を(1,1)とした座標)
- `DBfigures/allpics.txt`に画像ファイルの一覧
  - これを使って画像を一括で読み込む

## 操作
- 左上から画像が表示される。
- 最も下にある画像にマウスオーバーすると、マウスの場所と最も近い変化点を持つ候補が表示される。
- その状態でクリックすると、その状態が適用され、変化を行なった画像が一つ追加される。
- j, kでスクロール、qで終了(lessと同じ操作)

$S_0: M^{+}m^{+}M^{+}m^{+}M^{+}\textcolor{red}{m^{+}}M^{+}m^{+}$

\quad $\Downarrow$ \quad ($Cm^{+}$)

$S_1: M^{+}m^{+}M^{+}m^{+}M^{+}m^{-}M^{+}m^{+}$

$S_1: M^{+}\textcolor{red}{m^{+}}M^{+}m^{+}M^{+}\textcolor{red}{m^{-}}M^{+}m^{+}$

\quad $\Downarrow$ \quad ($TU$)

$S_2: M^{+}\dot{m^{+}}M^{+}m^{+}M^{+}\dot{m^{-}}M^{+}m^{+}$

$S_2: M^{+}\textcolor{red}{\dot{m^{+}}}M^{+}m^{+}M^{+}\textcolor{red}{\dot{m^{-}}}M^{+}m^{+}$

\quad $\Downarrow$ \quad ($R(m^{+},m^{-})$)

$S_3: \dot{M^{+}}m^{+}M^{+}m^{+}M^{+}m^{+} \:||\: \dot{M^{+}}m^{+}M^{+}m^{+}M^{+}m^{+}$

$S_3: \textcolor{red}{\dot{M^{+}}}m^{+}M^{+}m^{+}M^{+}m^{+} \:||\: \textcolor{red}{\dot{M^{+}}}m^{+}M^{+}m^{+}M^{+}m^{+}$

\quad $\Downarrow$ \quad ($SE$)

 $S_4: M^{+}m^{+}M^{+}m^{+}M^{+}m^{+} \:||\: M^{+}m^{+}M^{+}m^{+}M^{+}m^{+}$

FIGURE

系列２（眼の形成）


$S_{0}: M^{+}m^{+}M^{+}m^{+}M^{+}\textcolor{red}{m^{+}}M^{+}m^{+}$

\quad $\Downarrow$ \quad ($Cm^{+}$)

$S'_0: M^{+}m^{+}M^{+}m^{+}M^{+}m^{-}M^{+}m^{+}$

$S'_0: M^{+}m^{+}M^{+}m^{+}M^{+}\textcolor{red}{m^{-}}M^{+}m^{+}$

\quad $\Downarrow$ \quad ($Bm^{-}$)

$S_1: M^{+}m^{+}M^{+}m^{+}M^{+}m^{-}M^{-}m^{-}M^{+}m^{+}$

$S_1: M^{+}m^{+}M^{+}m^{+}\textcolor{red}{M^{+}}m^{-}M^{-}m^{-}\textcolor{red}{M^{+}}m^{+}$

\quad $\Downarrow$ \quad ($TO$)

$S_2: M^{+}m^{+}M^{+}m^{+}\dot{M^{+}}m^{-}M^{-}m^{-}\dot{M^{+}}m^{+}$

$S_2: M^{+}m^{+}M^{+}m^{+}\textcolor{red}{\dot{M^{+}}}m^{-}M^{-}m^{-}\textcolor{red}{\dot{M^{+}}}m^{+}$

\quad $\Downarrow$ \quad ($R(M^{+},M^{+})$)

$S_3: M^{+}m^{+}M^{+}m^{+}M^{+}\dot{m^{-}}M^{+}m^{+}[m^{-}\dot{M^{-}}m^{-}M^{-}]$

$S_3: M^{+}m^{+}M^{+}m^{+}M^{+}\textcolor{red}{\dot{m^{-}}}M^{+}m^{+}[m^{-}\textcolor{red}{\dot{M^{-}}}m^{-}M^{-}]$

\quad $\Downarrow$ \quad ($SI$)

 $S_4: M^{+}m^{+}M^{+}m^{+}M^{+}m^{-}M^{+}m^{+}[m^{-}M^{-}m^{-}M^{-}]$

FIGURE


系列３（ゴルジ小胞分離）

$S_0: M^{+}\textcolor{red}{m^{+}}M^{+}m^{+}M^{+}\textcolor{red}{m^{+}}M^{+}m^{+}$

\quad $\Downarrow$ \quad ($Cm^{+}$)

$S_1: M^{+}m^{-}M^{+}m^{+}M^{+}m^{-}M^{+}m^{+}$

$S_1: M^{+}\textcolor{red}{m^{-}}M^{+}m^{+}M^{+}\textcolor{red}{m^{-}}M^{+}m^{+}$

\quad $\Downarrow$ \quad ($TH$)

$S_2: M^{+}\dot{m^{-}}M^{+}m^{+}M^{+}\dot{m^{-}}M^{+}m^{+}$

$S_2: M^{+}\textcolor{red}{\dot{m^{-}}}M^{+}m^{+}M^{+}\textcolor{red}{\dot{m^{-}}}M^{+}m^{+}$

\quad $\Downarrow$ \quad ($R(m^{-},m^{-})$)

$S_3: M^{+}\dot{m^{+}}M^{+}m^{+} \:||\: M^{+}m^{+}M^{+}\dot{m^{+}}$

$S_3: M^{+}\textcolor{red}{\dot{m^{+}}}M^{+}m^{+} \:||\: M^{+}m^{+}M^{+}\textcolor{red}{\dot{m^{+}}}$

\quad $\Downarrow$ \quad ($SE$)

 $S_4: M^{+}m^{+}M^{+}m^{+} \:||\: M^{+}m^{+}M^{+}m^{+}$

FIGURE

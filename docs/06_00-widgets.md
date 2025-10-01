# Built-in Widgets


## 概要

私は2画面を前提にQtileのコンフィグレーションを行っています。Qtileの起動やコンフィグレーションの起点となる`config.py`からは、下記になります。

```
from modules.screens_bar import screens
```

そして、`modules/screens_bar.py`は下記。

```
from modules.screens_bar__main import screen_main
from modules.screens_bar__sub_01 import screen_sub_01

screens = [
  screen_main,
  screen_sub_01,
]
```

`screen_main`、`modules/screens_bar__main.py`は、メインの画面の設定になります。なお、`modules/screens_bar___common.py`は、各画面で共通の設定を記述しています。

別途、私が記述した通り、普段は1画面でQtileを使っているので、`screen_sub_01`は、ほとんど使いません。


## 動的な追加・削除の切り替え

2画面目を追加・削除下段階で、動的に設定の読み込み・廃棄の設定ができると思いますが、現在は組み込んでいません。


## 現在、どの画面に居るのか？を明示的に

`libqtile.widget.CurrentScreen`の導入は必須だと思います。


いずれにせよ、2画面（以上）をキーボード主体で操作するのは管理無理があるかもしれません。これに関しては、マウス操作に軍配が上がると思います。





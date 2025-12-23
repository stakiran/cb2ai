# cb2ai
クリップボード内容を OpenAI API に問うて、その結果をテキストファイルに書き込んでからそのファイルを開くツール。

自分用なのであまり公開用には整備されていないが、[Cline が書いた README](README_by_cline.md) もある。

## スニペットをつくる
- xxx.md を書く
- xxx.bat を書いて、cb2ai.py を呼び出す形に
    - tokens.bat は個人的なやつ。OpenAI API token などトークン系をロードするもので PATH 通ってる
    - モデル名は API 指定時に使う文字列をそのまま書く

## クイックに呼び出せるようにする
クイックランチに置く:

<img width="209" height="106" alt="Image" src="https://github.com/user-attachments/assets/d14a1eae-a4f9-4deb-ac18-b2358897c6bc" />

手順は[Windows11にはクイックランチがない - stao](https://scrapbox.io/stao/Windows11%E3%81%AB%E3%81%AF%E3%82%AF%E3%82%A4%E3%83%83%E3%82%AF%E3%83%A9%E3%83%B3%E3%83%81%E3%81%8C%E3%81%AA%E3%81%84)

別に AutoHotkey などでホットキーを割り当ててもいい。

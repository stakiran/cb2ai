# 🐰gpt-o4-miniだからAPI周りが古い（API keyは今は`sk-`じゃないとか）……

---

# cb2ai

クリップボード内容を OpenAI Chat Completions API に送信し、結果を Markdown ファイルに書き込んでブラウザ（または既定のビューア）で開く Python スクリプト。

## 前提

- Python 3.7 以上  
- 環境変数 `OPENAI_API_KEY` に OpenAI API キーを設定  
  - Windows の場合:
    ```cmd
    setx OPENAI_API_KEY "sk-..."
    ```
  - PowerShell の場合:
    ```powershell
    [Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "sk-...", "User")
    ```

## インストール

依存パッケージをインストール:

```bash
pip install -r requirements.txt
```

## 使い方

```bash
python cb2ai.py --prompt <プロンプトファイル> [--model <モデル名>] [--timeout <秒>]
```

- `--prompt`, `-p` : プロンプトを記載したファイルのパス（必須）  
- `--model`, `-m`   : 使用するモデル名（デフォルト: `gpt-3.5-turbo`）  
- `--timeout`, `-t` : リクエストタイムアウト秒数（デフォルト: `130`）

### プロンプトファイル例

```markdown
%cb%

上記のテキストを要約してください。
```

`%cb%` が現在のクリップボード内容に置換されます。

## 実行例

```bash
python cb2ai.py --prompt sample-prompt.md --model gpt-4 --timeout 120
```

実行後、テンポラリフォルダ（Windows では `%TEMP%`）に `cb2aiXXXX.md` というファイル名で結果が保存され、自動で開きます。

## ライセンス

MIT

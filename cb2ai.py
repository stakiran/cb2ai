import argparse
import os
import sys
import uuid
import tempfile
import pyperclip
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]
client = openai.OpenAI()

def parse_args():
    parser = argparse.ArgumentParser(
        description="クリップボード内容をOpenAI APIに送信して結果をMarkdownファイルで開く"
    )
    parser.add_argument("--prompt", "-p", required=True, help="プロンプトファイルのパス")
    parser.add_argument("--model", "-m", default="gpt-3.5-turbo", help="使用するモデル名")
    parser.add_argument("--timeout", "-t", type=int, default=130, help="APIリクエストのタイムアウト(秒)")
    return parser.parse_args()

def request_to_model(model_name, prompt, timeout=130):
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[{'role': 'user', 'content': prompt}],
            timeout=timeout
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[ERROR in {model_name}]: {str(e)}"

def main():
    args = parse_args()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("環境変数 OPENAI_API_KEY が設定されていません。", file=sys.stderr)
        sys.exit(1)
    openai.api_key = api_key

    # クリップボード取得
    cb_content = pyperclip.paste()

    # プロンプトファイル読み込み
    try:
        with open(args.prompt, "r", encoding="utf-8") as f:
            prompt_template = f.read()
    except Exception as e:
        print(f"プロンプトファイルの読み込みに失敗しました: {e}", file=sys.stderr)
        sys.exit(1)

    # %cb% を置換
    prompt = prompt_template.replace("%cb%", cb_content)

    # OpenAI API 呼び出し
    result_text = request_to_model(args.model, prompt, args.timeout)

    # Markdownファイル作成
    temp_dir = tempfile.gettempdir()
    filename = f"cb2ai{uuid.uuid4().hex[:3]}.md"
    filepath = os.path.join(temp_dir, filename)
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(result_text)
    except Exception as e:
        print(f"ファイル書き込みに失敗しました: {e}", file=sys.stderr)
        sys.exit(1)

    # ファイルを開く（Windows の関連付けで起動）
    try:
        os.startfile(filepath)
    except Exception as e:
        print(f"ファイルを開く際にエラーが発生しました: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from openai import OpenAI

app = Flask(__name__)
CORS(app)

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


@app.route('/generate-recipe', methods=['POST'])
def generate_recipe():
    data = request.json
    ingredients = data.get('ingredients', [])
    genre = data.get('genre', '')

    if not ingredients:
        return jsonify({"error": "Ingredients not provided"}), 400
    
    ingredients_text = "、".join(ingredients)  # 食材リストを日本語のテキストに変換
    if not genre:
      prompt = f"ランダムな料理のジャンルから、以下の食材を使用するレシピを教えてください。食材リストには、レシピに必要なすべての食材とその分量も記載してください。\n- 使用する食材: {ingredients_text}\n\n==出力フォーマット==\n料理名:\n【料理名】\n\n食材リスト:\n【食材】\n\n手順:\n【手順】\n"
    elif genre == "和食" or "洋食" or "中華":
      prompt = f"以下の情報を含む{genre}のレシピを教えてください。レシピに必要なすべての食材とその分量も記載してください。\n- 使用する食材: {ingredients_text}\n\n==出力フォーマット==\n料理名:\n【料理名】\n\n食材リスト:\n【食材】\n\n手順:\n【手順】\n"
    elif genre == "その他" or "洋食" or "中華":
      prompt = f"以下の情報を含む和食、洋食、中華料理以外の料理のジャンルのレシピを提供して下さい。レシピに必要なすべての食材とその分量も記載してください。\n- 使用する食材: {ingredients_text}\n\n==出力フォーマット==\n料理名:\n【料理名】\n\n食材リスト:\n【食材】\n\n手順:\n【手順】\n"

    try:
      res = client.chat.completions.create(
          messages=[
            {
              "role": "system",
              "content": "あなたはシェフです。提供された食材を使って、指定されたフォーマットでレシピを作成してください。",
            },
            {
              "role": "user",
              "content": prompt
            }
          ],
          model="gpt-3.5-turbo",
      )
      recipe = res.choices[0].message.content

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({
      "recipe": recipe
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)

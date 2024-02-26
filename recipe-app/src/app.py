from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from openai import OpenAI

app = Flask(__name__)
CORS(app)
api_key = "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"
client = OpenAI(api_key=api_key)

@app.route('/generate-recipe', methods=['POST'])
def generate_recipe():
    data = request.json
    ingredients = data.get('ingredients', [])
    genre = data.get('genre', '')

    if not ingredients or not genre:
        return jsonify({"error": "Ingredients or genre not provided"}), 400
    
    ingredients_text = "、".join(ingredients)  # 食材リストを日本語のテキストに変換
    prompt = f"{genre}のレシピを教えてください。使用する食材は{ingredients_text}です。レシピは作る料理名、使う食材、食材の分量、具体的な手順を含めてください。"

    try:
      res = client.chat.completions.create(
          messages=[
            {
              "role": "system",
              "content": "あなたはシェフです。以下の食材を使ったレシピを提供してください。",
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
        "status": "success",
        "ingredients": ingredients,
        "genre": genre,
        "recipe": recipe
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)

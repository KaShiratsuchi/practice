<template>
  <div class="flex gap-4">
    <div id="inputArea" class="container w-1/2 max-w-md mx-auto">
      <input type="text" v-model="newIngredient" v-on:keyup.enter="addIngredient" placeholder="食材名を入力してください" class="input border border-gray-300 p-2 rounded-lg w-full mb-4">
      <button @click="addIngredient" class="btn bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mr-2">追加</button>
      <button @click="removeAllIngredient" class="btn bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded ">全件削除</button>
      <div class="my-4">
          <h2 class="text-lg font-bold mb-2">食材リスト</h2>
          <ul class="min-h-96 list-none p-0">
            <li v-for="(ingredient, index) in ingredients" :key="index" class="flex items-center justify-between mb-3 bg-gray-100 p-2 rounded-lg">
              <p class="inline-block min-w-80 text-left mr-20">
                {{ ingredient }}
              </p>
              <button @click="removeIngredient(index)" class="flex items-center justify-center ">
                <img src="../assets/circle-xmark-regular.svg" alt="" class="w-6 h-6">
              </button>
            </li>
          </ul>
      </div>
      <input list="genres" v-model="selectedGenre" name="genre" id="genre" class="select border border-gray-300 p-2 rounded-lg w-full" placeholder="ジャンルを選択または入力してください">
      <datalist id="genres">
        <option value="和食"></option>
        <option value="洋食"></option>
        <option value="中華"></option>
        <option value="スイーツ"></option>
        <option value="その他"></option>
      </datalist>
      <p class="my-4 text-red-500">{{ errorMessage }}</p>
      <button @click="generateRecipe" class="btn bg-indigo-500 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded">レシピを生成する</button>
    </div>
    <div class="container w-1/2 mx-auto flex flex-col items-center">
      <div id="outputArea" class=" bg-blue-50 rounded-2xl px-8 py-4 h-full w-full">
        <div v-if="showDefaultMessage">
          <p class="text-xl text-gray-800">入力した食材を使ったレシピが表示されます</p>
        </div>
        <div v-else-if="loading">
          <p class="text-xl text-gray-800">レシピを生成中…</p>
        </div>
        <div v-else>
          <h1 class="text-2xl font-bold text-gray-800 mb-4">{{ recipeTitle }}</h1>
          <h2 class="text-left text-xl font-semibold text-gray-700 mb-2">食材リスト</h2>
          <ul class="text-left pl-5 mb-4">
            <li v-for="(ingredient, index) in recipeIngredients" :key="`ingredient-${index}`" class="mb-1 text-gray-600">
              {{ ingredient }}
            </li>
          </ul>
          <h2 class="text-left text-xl font-semibold text-gray-700 mb-2">調理手順</h2>
          <ul class="text-left pl-5">
            <li v-for="(step, index) in recipeSteps" :key="`step-${index}`" class="mb-1 text-gray-600">
              {{ step }}
            </li>
          </ul>
        </div>
      </div>
      <div class="flex gap-4">
        <button @click="clearRecipe" class="btn bg-yellow-500 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded mt-4">レシピをクリア</button>
        <button @click="saveRecipe" class="btn bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded mt-4">レシピを保存</button>
      </div>
    </div>
    <div class="container w-1/4 mx-auto">
      <div class="">
        <h2 class="text-lg font-bold mb-4">保存したレシピ</h2>
        <ul class="space-y-3">
          <li v-for="(recipe, index) in savedRecipes" :key="`saved-${index}`" class="flex justify-between py-1.5 px-4">
            <p class="bg-white rounded-lg  items-center cursor-pointer " @click="() => showRecipe(recipe)">
              {{ recipe.title }}
            </p>
            <button @click="deleteRecipe(index)" class="text-sm bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-2 rounded-lg shadow">
              削除
            </button>
          </li>
        </ul>
      </div>
    </div>
  </div>

</template>

<script setup>
/* eslint-disable */
import { ref, onMounted } from 'vue';
import axios from 'axios';

// 食材リスト
const ingredients = ref([]);
// 入力した食材
const newIngredient = ref("");
// ジャンル
const selectedGenre = ref("");
// レシピ
const recipeData = ref();
// エラーメッセージ
const errorMessage = ref("");

// レシピの情報
const recipeTitle = ref("");
const recipeIngredients = ref([]);
const recipeSteps = ref([]);

// ロード関連
const loading = ref(false);
const showDefaultMessage = ref(true);

// 食材追加
const addIngredient = () => {
  if(newIngredient.value !== ""){
    ingredients.value.push(newIngredient.value);
    newIngredient.value = "";
  } 
}

// 食材削除
const removeIngredient = (index) =>{
  ingredients.value.splice(index, 1);
}

// 全件削除
const removeAllIngredient = () => {
  ingredients.value = [];
}

// レシピ生成
const generateRecipe = async () => {
  // 食材が空の場合APIをコールせずにエラーメッセージを表示
  if (ingredients.value.length === 0) {
    errorMessage.value = '食材を入力してください';
    return;
  } else {
    errorMessage.value = "";
    loading.value = true;
    showDefaultMessage.value = false;
  }

  // APIをコール
  try {
    const response = await axios.post('http://localhost:5000/generate-recipe', {
      ingredients: ingredients.value,
      genre: selectedGenre.value
    });
    console.log(response.data);
    recipeData.value = response.data.recipe;

    const parseRecipeData = (data) => {
      // レシピデータの初期化
      recipeTitle.value = "";
      recipeIngredients.value = [];
      recipeSteps.value = [];

      // タイトルを正確に抽出
      const titleEndIndex = data.indexOf("食材リスト:");
      recipeTitle.value = data.substring(5, titleEndIndex).trim(); // "料理名:" と "食材リスト:" の間

      // 食材リストを抽出
      const ingredientsStartIndex = titleEndIndex + 7;
      const stepsStartIndex = data.indexOf("手順:");
      const ingredientsText = data.substring(ingredientsStartIndex, stepsStartIndex).trim();
      recipeIngredients.value = ingredientsText.split('-').slice(1).map(i => i.trim()); // 最初の空要素を除外

      // 手順を抽出して改行を調整
      const stepsText = data.substring(stepsStartIndex + 3).trim(); // "手順:" を除去
      recipeSteps.value = stepsText.split(/(?=\d\.)/).map(s => s.trim()); // 数字の前で分割
    };

    // generateRecipe関数内でparseRecipeDataを呼び出す
    recipeData.value = parseRecipeData(response.data.recipe);
    loading.value = false;
  } catch (error) {
    console.error(error);
    loading.value = false;
  }
};

// レシピをクリア
const clearRecipe = () => {
  // レシピデータのクリア
  recipeTitle.value = "";
  recipeIngredients.value = [];
  recipeSteps.value = [];
  removeAllIngredient()
  selectedGenre.value = "";
  // デフォルトメッセージを表示
  showDefaultMessage.value = true;
};

// レシピの保存
const savedRecipes = ref([]);

const saveRecipe = () => {
  if (savedRecipes.value.length >= 11) {
    alert('保存できるレシピの最大数に達しました。');
    return;
  }
  
  const newRecipe = {
    title: recipeTitle.value,
    ingredients: recipeIngredients.value,
    steps: recipeSteps.value
  };
  
  savedRecipes.value.push(newRecipe);
  localStorage.setItem('savedRecipes', JSON.stringify(savedRecipes.value));
};

const loadSavedRecipes = () => {
  const recipes = localStorage.getItem('savedRecipes');
  if (recipes) {
    savedRecipes.value = JSON.parse(recipes);
  }
};

const deleteRecipe = (index) => {
  savedRecipes.value.splice(index, 1);
  localStorage.setItem('savedRecipes', JSON.stringify(savedRecipes.value));
};

onMounted(() => {
  loadSavedRecipes();
});

const showRecipe = (recipe) => {
  recipeTitle.value = recipe.title;
  recipeIngredients.value = recipe.ingredients;
  recipeSteps.value = recipe.steps;
  showDefaultMessage.value = false;
};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

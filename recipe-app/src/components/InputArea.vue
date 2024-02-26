<template>
  <div class="container max-w-md mx-auto">
    <input type="text" v-model="newIngredient" v-on:keyup.enter="addIngredient" placeholder="食材名を入力してください" class="input border border-gray-300 p-2 rounded-lg w-full mb-4">
    <button @click="addIngredient" class="btn bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mr-2">追加</button>
    <button @click="removeAllIngredient" class="btn bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded ">全件削除</button>
    <ul class="min-h-96 list-none p-0 my-4">
      <li v-for="(ingredient, index) in ingredients" :key="index" class="flex items-center justify-between mb-3">
        <p class="inline-block min-w-80 text-left mr-20">
          {{ ingredient }}
        </p>
        <button @click="removeIngredient(index)" class="flex items-center justify-center ">
          <img src="../assets/circle-xmark-regular.svg" alt="" class="w-6 h-6">
        </button>
      </li>
    </ul>
    <select v-model="selectedGenre" name="genre" id="genre" class="select border border-gray-300 p-2 rounded-lg w-full mb-4">
      <option value="">ジャンルを選択してください</option>
      <option value="和食">和食</option>
      <option value="洋食">洋食</option>
      <option value="中華">中華</option>
      <option value="その他">その他</option>
    </select>
    
    <button @click="sendData" class="btn bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">レシピを生成する</button>
  </div>
</template>

<script setup>
/* eslint-disable */
import { ref } from 'vue';
import axios from 'axios';

const ingredients = ref([]);
const newIngredient = ref("");
const selectedGenre = ref("");

const addIngredient = () => {
  if(newIngredient.value !== ""){
    ingredients.value.push(newIngredient.value);
    newIngredient.value = "";
  } 
}

const removeIngredient = (index) =>{
  ingredients.value.splice(index, 1);
}

const removeAllIngredient = () => {
  ingredients.value = [];
}

const sendData = async () => {
  try {
    const response = await axios.post('http://localhost:5000/generate-recipe', {
      ingredients: ingredients.value,
      genre: selectedGenre.value
    });
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

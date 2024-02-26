<template>
  <div class="container mx-auto w-1/2 p-4 bg-white shadow-lg rounded-lg">
    <input type="text" v-model="newIngredient" v-on:keyup.enter="addIngredient" placeholder="食材名を入力してください" class="w-full p-2 border-2 border-gray-200 rounded-md focus:outline-none focus:border-blue-500 transition duration-150 ease-in-out">
    <button @click="addIngredient" class="mt-2 px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50 transition duration-150 ease-in-out">追加</button>
    <ul class="min-h-96 mt-4">
      <li v-for="(ingredient, index) in ingredients" :key="index" class="flex items-center justify-between mb-2">
        <p class="inline-block min-w-80 text-left mr-20 p-2 bg-gray-100 rounded-md">
          {{ ingredient }}
        </p>
        <button @click="removeIngredient(index)" class="p-2 bg-red-500 rounded-md hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-opacity-50 transition duration-150 ease-in-out">
          <img src="../assets/circle-xmark-regular.svg" alt="" class="w-4 h-4">
        </button>
      </li>
    </ul>
    <select name="genre" id="genre" class="w-full p-2 border-2 border-gray-200 rounded-md focus:outline-none focus:border-blue-500 transition duration-150 ease-in-out mt-4">
      <option value="">ジャンルを選択してください</option>
      <option value="和食">和食</option>
      <option value="洋食">洋食</option>
      <option value="中華">中華</option>
      <option value="その他">その他</option>
    </select>
    <div class="mt-4 flex justify-end space-x-2">
      <button @click="removeAllIngredient" class="px-4 py-2 bg-gray-500 text-white rounded-md hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-opacity-50 transition duration-150 ease-in-out">全件削除</button>
      <button @click="sendData" class="px-4 py-2 bg-green-500 text-white rounded-md hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-opacity-50 transition duration-150 ease-in-out">レシピを生成する</button>
    </div>
  </div>
</template>

<script setup>
/* eslint-disable */
import { ref } from 'vue';
import axios from 'axios';

const ingredients = ref([]);
const newIngredient = ref("");

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
    const response = await axios.post('http://localhost:5000/receive-data', { data: ingredients });
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

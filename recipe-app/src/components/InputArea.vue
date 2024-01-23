<template>
  <div class="container w-1/2">
    <input type="text" v-model="newIngredient" v-on:keyup.enter="addIngredient" placeholder="食材名を入力してください" class="outline border-black p-2 mr-10">
    <button @click="addIngredient" class="bg-gray-100 px-10 py-3 rounded-md">追加</button>
    <ul>
      <li v-for="(ingredient, index) in ingredients" :key="index">
        {{ ingredient }}
        <button @click="removeIngredient">削除</button>
      </li>
    </ul>
    <button @click="removeAllIngredient">全件削除</button>
    <button @click="sendData">レシピを生成する</button>
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
    console.log(newIngredient.value);
    ingredients.value.push(newIngredient.value);
    newIngredient.value = "";
  } else {
    console.log("empty");
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

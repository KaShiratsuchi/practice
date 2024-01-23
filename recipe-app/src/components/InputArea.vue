<template>
  <div class="container">
    <input type="text" v-model="newIngredient">
    <button @click="addIngredient">追加</button>
  </div>
</template>

<script setup>
/* eslint-disable */
import { defineProps } from 'vue'
const props = defineProps({
  msg: String
})

function addIngredient(){
  console.log("clicked");
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
  width: 50%;
}
</style>

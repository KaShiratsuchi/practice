<template>
  <div class="container">
    <h1>test</h1>
  </div>
</template>

<script setup>
/* eslint-disable */
import { defineProps } from 'vue'
const props = defineProps({
  msg: String
})

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
  width: 50%;
  background-color: aquamarine;
}
</style>

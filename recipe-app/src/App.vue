
<template>
  <div class="container m-auto gap-4">
    <InputArea/>
    <!-- <OutputArea/> -->
  </div>
</template>

<script setup>
 /* eslint-disable */
import InputArea from './components/InputArea.vue'
import OutputArea from './components/OutputArea.vue'

</script>

<style >
@tailwind base;
@tailwind components;
@tailwind utilities;
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@100..900&display=swap');
#app {
  font-family: "Noto Sans JP", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.container {
  /* display: flex; */
}
</style>

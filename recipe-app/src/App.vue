
<template>
  <div class="container flex m-auto gap-4">
    <InputArea/>
    <OutputArea/>
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
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

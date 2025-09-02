<template>
  <div>
    <p>{{ inputText1 }}</p>
    <input :value="inputText1" @input="onInput">
    <!-- 단방향 바인드 -->

    <p>{{ inputText2 }}</p>
    <input v-model="inputText2">
    <!-- 양방향, 한국어 반영에 불편함 있음 -->
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  
  const inputText1 = ref('')
  const inputText2 = ref('')
  
  const onInput = function (event) {
    inputText1.value = event.currentTarget.value
  }
</script>

<style scoped>

</style>
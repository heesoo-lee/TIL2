<template>
  <div>
    <!-- Inline Handlers -->
    <button @click="count++">Add 1</button>
    <p>Count: {{ count }}</p>

    <!-- Method Handlers -->
    <button @click="myFunc">Hello</button>

    <!-- Calling Methods in Inline Handlers -->
    <button @click="greeting('hello')">Say hello</button>
    <button @click="greeting('bye')">Say bye</button>

    <!-- Accessing Event Argument in Inline Handlers -->
    <button @click="warning('경고입니다.', $event)">Submit</button>
    <!-- $ 붙어 있는 애들은 대체적으로 전역변수 개념, 구분용 -->

    <!-- event modifiers -->
    <form @submit.prevent="onSubmit">...</form>
    <a @click.stop.prevent="onLink">...</a>

    <!-- key modifiers -->
    <input @keyup.enter="onSubmit">
    <!-- keyup : 키를 눌렀다 떼는 순간 (눌렸다가 다시 올라오는 순간) -->
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const count = ref(0)

  const name = ref('Alice')
  const myFunc = function (event) {
    console.log(event)
    console.log(event.currentTarget)
    console.log(`Hello ${name.value}!`)
  }

  const greeting = function (message) {
    console.log(message)
  }
  
  const warning = function (message, event) {
    console.log(message)
    console.log(event)
  }
</script>

<style scoped>

</style>
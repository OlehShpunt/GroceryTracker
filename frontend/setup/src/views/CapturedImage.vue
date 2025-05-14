<template>
    <div class="captured-image">
      <img :src="imageSrc" alt="Captured" />
    </div>
  </template>
  
  <script setup>
  import { computed } from 'vue'
  import { useRoute } from 'vue-router'
  
  const route = useRoute()
  const imageSrc = computed(() => route.query.img)
  </script>
  
  <style scoped>
  .captured-image {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  img {
    max-width: 90%;
    max-height: 90%;
    border: 2px solid #000;
    border-radius: 10px;
  }
  </style>
  
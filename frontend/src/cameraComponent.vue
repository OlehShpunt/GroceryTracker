<template>
    <div>
      <video ref="video" autoplay playsinline></video>
      <button @click="startCamera">Start Camera</button>
      <button @click="stopCamera" v-if="stream">Stop Camera</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'CameraComponent',
    data() {
      return {
        stream: null,
      };
    },
    methods: {
      async startCamera() {
        try {
          const stream = await navigator.mediaDevices.getUserMedia({ video: true });
          this.stream = stream;
          this.$refs.video.srcObject = stream;
        } catch (error) {
          console.error('Error accessing camera:', error);
          alert('Camera access denied or unavailable');
        }
      },
      stopCamera() {
        if (this.stream) {
          this.stream.getTracks().forEach(track => track.stop());
          this.stream = null;
          this.$refs.video.srcObject = null;
        }
      },
    },
    beforeUnmount() {
      this.stopCamera();
    },
  };
  </script>
  
  <style scoped>
  video {
    width: 100%;
    max-width: 600px;
    border: 2px solid #000;
    /* transform: scaleX(-1); */
  }
  button {
    margin: 10px;
    padding: 5px 10px;
    font-size: 16px;
  }
  </style>
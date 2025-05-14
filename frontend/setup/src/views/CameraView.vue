<template>
    <div class="camera-view">
      <video ref="video" autoplay playsinline></video>
      <button @click="takePicture">Scan</button>
      <canvas ref="canvas" style="display: none;"></canvas>
    </div>
    <p class="text-gray-800 dark:text-gray-100">You  a new message!</p>
    <p class="text-red-500">This text should be red</p>
</template>
  
<script setup>
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'

const video = ref(null)
const canvas = ref(null)
const router = useRouter()

onMounted(async () => {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true })
    video.value.srcObject = stream
    await video.value.play()
  } catch (error) {
    console.error('Error accessing camera:', error)
  }
})

const takePicture = () => {
  const videoEl = video.value
  const canvasEl = canvas.value

  // Ensure video is ready
  if (videoEl.videoWidth === 0 || videoEl.videoHeight === 0) {
    console.warn('Video not ready yet')
    return
  }

  canvasEl.width = videoEl.videoWidth
  canvasEl.height = videoEl.videoHeight
  const ctx = canvasEl.getContext('2d')
  ctx.drawImage(videoEl, 0, 0, canvasEl.width, canvasEl.height)

  const imageData = canvasEl.toDataURL('image/png')

  // Navigate to captured view with image data
  router.push({ name: 'CapturedImage', query: { img: imageData } })
}
</script>

<style scoped>
.camera-view {
  display: flex;
  flex-direction: column;
  align-items: center;
}
video {
  width: 100%;
  max-width: 500px;
  border-radius: 10px;
}
button {
  margin-top: 10px;
  padding: 10px 20px;
}
</style>
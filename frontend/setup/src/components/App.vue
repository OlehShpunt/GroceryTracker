<template>
    <div>
        <video v-if="!isCaptured" ref="videoRef" class="m-auto mt-10 w-100 h-160 bg-blue-100 rounded object-cover" autoplay playsinline></video>
        <canvas v-if="isCaptured" class="m-auto mt-10 w-100 h-160 bg-blue-100 rounded border-4 border-green-600" :style="{ backgroundImage: `url(${imageURL})` }"></canvas>
        <button @click="capturePhoto" class="mt-10 m-auto p-2 bg-blue-600 text-white rounded block">Capture</button>
    </div>
</template>

<script setup>
import { defineProps, defineEmits, onMounted, ref } from 'vue';

const videoRef = ref(null);
let imageURL = null;
const isCaptured = ref(false);

onMounted(() => {
    navigator.mediaDevices
        .getUserMedia(
            { 
                video: true,
                width: { ideal: 1920, max: 1280 },
                height: { ideal: 1080, max: 720 }
            }
        )
        .then(stream => {
            videoRef.value.srcObject = stream;
        })
        .catch(error => {
            alert('Error accessing camera:', error);
        });
});

/**
 * Capture a photo from the video stream and display it on a canvas
 * with the canvas width and height calculated at runtime to achieve
 * correct display in the container with the same size as the <video> tag.
 */
const capturePhoto = () => {
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');

    // Get the dimensions of the video
    const videoWidth = videoRef.value.videoWidth;
    const videoHeight = videoRef.value.videoHeight;

    // Set the canvas dimensions to match the container
    const canvasWidth = videoRef.value.offsetWidth;
    const canvasHeight = videoRef.value.offsetHeight;

    canvas.width = canvasWidth;
    canvas.height = canvasHeight;

    // Calculate cropping dimensions to maintain aspect ratio
    const videoAspectRatio = videoWidth / videoHeight;
    const canvasAspectRatio = canvasWidth / canvasHeight;

    let cropWidth, cropHeight, cropX, cropY;

    if (videoAspectRatio > canvasAspectRatio) {
        // Video is wider than canvas, crop horizontally
        cropHeight = videoHeight;
        cropWidth = videoHeight * canvasAspectRatio;
        cropX = (videoWidth - cropWidth) / 2;
        cropY = 0;
    } else {
        // Video is taller than canvas, crop vertically
        cropWidth = videoWidth;
        cropHeight = videoWidth / canvasAspectRatio;
        cropX = 0;
        cropY = (videoHeight - cropHeight) / 2;
    }

    // Draw the cropped image onto the canvas
    context.drawImage(
        videoRef.value, // Source video element
        cropX, cropY,   // Cropping start point (x, y)
        cropWidth, cropHeight, // Cropping dimensions (width, height)
        0, 0,           // Canvas start point (x, y)
        canvasWidth, canvasHeight // Canvas dimensions (width, height)
    );

    // Convert the canvas content to a data URL
    imageURL = canvas.toDataURL('image/png');

    console.log(imageURL); // You can send this data URL to your server or use it as needed

    isCaptured.value = true;
};

</script>

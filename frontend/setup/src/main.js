import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import './style.css'


import App from './App.vue'
import myCode from '../../src/text.vue'

import CameraComponent from '../../src/cameraComponent.vue'
import CameraView from './views/CameraView.vue'
import CapturedImage from './views/CapturedImage.vue'

const routes = [
    { path: '/', name: 'CameraView', component: CameraView },
    { path: '/captured', name: 'CapturedImage', component: CapturedImage }
]

export default createRouter({
    history: createWebHistory(),
    routes
})

createApp(CameraView).mount('#app')
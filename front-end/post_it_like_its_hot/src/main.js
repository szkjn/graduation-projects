import { createApp } from 'vue'
// import { createStore } from 'vuex';

import App from './App.vue'
import router from './router'
// import axios from 'axios';

// const store = createStore({
//     state() {
//         return {
//         }
//     },
//     mutations: {
//     },
//     actions: {
//     }
// })

createApp(App)
    .use(router)
    .mount('#app')

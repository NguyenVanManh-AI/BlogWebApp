import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'  
import router from './router/routes' 

import 'bootstrap/dist/css/bootstrap.min.css'
import 'jquery/src/jquery.js'
import 'bootstrap/dist/js/bootstrap.min.js'
import Paginate from "vuejs-paginate-next";

import storeConfigs  from './store/store'


const app = createApp(App);

app.use(router);
app.use(VueAxios, axios)
app.use(storeConfigs)
app.use(Paginate)
app.mount('#app')

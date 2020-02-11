import Vue from 'vue'
import App from './App.vue'
import router from "./router"
import 'bootstrap/dist/css/bootstrap.min.css'
import $ from "jquery"
import 'bootstrap/dist/js/bootstrap.min.js'
import 'font-awesome/css/font-awesome.min.css'
import VueCookies from 'vue-cookies'
import qs from 'qs'
import axios from 'axios'
import VueHttp from "vue-resource";
Vue.use(VueHttp);
Vue.prototype.qs = qs;
Vue.use(VueCookies);
Vue.prototype.$axios = axios;
$;

Vue.config.productionTip = false;
new Vue({
    router,
    render: h => h(App),
}).$mount('#app');

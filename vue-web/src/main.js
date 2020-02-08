import Vue from 'vue'
import App from './App.vue'
import router from "./router"
import 'bootstrap/dist/css/bootstrap.min.css'
import $ from "jquery"
import 'bootstrap/dist/js/bootstrap.min.js'
import 'font-awesome/css/font-awesome.min.css'
$;

Vue.config.productionTip = false;
new Vue({
    router,
    render: h => h(App),
}).$mount('#app');

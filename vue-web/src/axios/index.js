import Vue from "vue"
import axios from "axios"

xsrfCookieName : 'XSRF-TOKEN';
axios.defaults.headers.post['Content-Type'] = 'application/x-www-fromurlencodeed';
axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
axios.defaults.baseURL = "http://localhost:5000";
Vue.prototype.$http = axios;

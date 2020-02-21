import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import login from '../login/login'
import registe from "../login/registe"
import logininfo from "../login/logininfo"

Vue.use(Router);

export default new Router({
    mode: 'history',
    routes: [
        {
            path: "/login",
            component: login
        },
        {
            path: "/registe",
            component: registe
        },
        {
          path: "/logininfo",
          component: logininfo
        }
    ]
})

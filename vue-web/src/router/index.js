import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import login from '../login/login'
import registe from "../login/registe"
import logininfo from "../login/logininfo"

Vue.use(Router);
// const login = r => require.ensure([],() => r(require("../login/login.vue")),"login");
// const registe = r => require.ensure([],() => r(require("../login/registe.vue")),"registe");
// const logininfo = r => require.ensure([],() => r(require("../login/logininfo.vue")),"logininfo");
export default new Router({
    mode: 'history',
    // hash: 'history',
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

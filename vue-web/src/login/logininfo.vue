<template>
    <div>
        <div v-for="(item,index) in this.loginInfoList.login_text" :key="(item,index)">

        <p>{{index}}:{{item}}</p>

    </div>
    </div>

</template>

<script>
    export default {
        name: "logininfo",
        data() {
            return {
                loginInfoList: {
                    "login_text": ""
                }
            }
        },
        created() {
            window.addEventListener('load', () => {
                var login = this.$cookies.get("login");
                if (login == null){
                    window.location.href='/login'
                }
                var data = {
                    "login": login,
                };
                this.$axios({
                    methods: "GET",
                    url: "/api" + "/logininfo",
                    dataType: "jsonp",
                    data: this.qs.stringify(data)
                }).then((data) => {
                    if (data.data[0].success == "registe" && typeof data.data[0].success == "string"){
                        alert(data.data[0].success + '跳转页面')
                    } else if (data.data[0].success != "registe" && typeof data.data[0].success == "object")
                    {window.console.log(data.data[0].success);
                    this.loginInfoList.login_text = data.data[0].success;
                    }
                    // alert(data.data)
                }).catch((error) => {
                    alert(error);
                    window.console.log(error)
                })
            })
        },
        methods:
            {}
    }
</script>

<style scoped>

</style>

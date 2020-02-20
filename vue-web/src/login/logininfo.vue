<template>
    <dev>
        <p v-model="this.loginInfoList.login_text"></p>
    </dev>
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
            window.addEventListener('scroll', () => {
                var login = this.$cookies.get("login");
                var data = {
                    "login": login,
                };
                this.$axios({
                    methods: "GET",
                    url: "/api" + "/logininfo",
                    dataType: "jsonp",
                    data: this.qs.stringify(data)
                }).catch((data) => {
                    this.loginInfoList.login_text = data.data.success;
                    alert(data.data.success)
                }).then((error) => {
                    alert(error)
                })
            })
        },
        methods:
            {}
    }
</script>

<style scoped>

</style>

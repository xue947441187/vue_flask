<template>
    <div>
        <p v-text="this.loginInfoList.login_text"></p>
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
                var data = {
                    "login": login,
                };
                this.$axios({
                    methods: "GET",
                    url: "/api" + "/logininfo",
                    dataType: "jsonp",
                    data: this.qs.stringify(data)
                }).then((data) => {
                    window.console.log(data.data[0].success);
                    this.loginInfoList.login_text = data.data[0].success;
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

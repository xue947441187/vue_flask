<template>
    <div class="login">
        <div class="container">
            <div class="modal-dialog" style="margin-top: 10%;">
                <div class="modal-content">
                    <div class="modal-header">

                        <h4 class="modal-title text-center" id="myModalLabel">登录</h4>
                    </div>
                    <div class="modal-body" id="model-body">
                        <div class="form-group">

                            <input v-model="Upfrom.name" type="text" class="form-control" placeholder="用户名"
                                   autocomplete="off">
                        </div>
                        <div class="form-group">

                            <input v-model="Upfrom.password" type="password" class="form-control" placeholder="密码"
                                   autocomplete="off">
                        </div>
                    </div>
                    <div class="modal-footer">
                        <div class="form-group">
                            <button @click="this.loginUp" type="button" class="btn btn-primary form-control">登录</button>
                        </div>
                        <div class="form-group">
                            <button type="button" class="btn btn-default form-control" @click="this.Upregiste">注册
                            </button>
                        </div>

                    </div>
                </div><!-- /.modal-content -->
            </div><!-- /.modal -->
        </div>
    </div>
</template>

<script>
    export default {
        name: "login",
        data() {
            return {
                Upfrom: {
                    name: "",
                    password: ""
                }
            }
        },
        created() {
            window.addEventListener("scroll", () => {
                var login = this.$cookies.get("login");
                var date = {
                    "login": login,
                };
                if (login != null) {
                    this.$axios({
                        methods: "GET",
                        url: "/api" + "/login",
                        dataType: "jsonp",
                        data: this.qs.stringify(date)
                    }).then((data) => {
                        // alert(data.data.code)
                        if (data.data.code == 200) {
                            this.window.href("/logininfo");
                            // window.location.href = "/logininfo";
                        } else {
                            this.$cookies.remove("login");

                        }
                    }).catch((error) => {
                        alert("错误信息" + error)
                    })
                }

            })
        },
        methods: {
            Upregiste: function () {
                this.$router.push("/registe")
                // this.location.href = '/registe'
            },
            loginUp: function () {
                var date = {
                    "userid": this.Upfrom.name,
                    "password": this.Upfrom.password
                };
                this.$axios({
                    method: "POST",
                    url: "/api" + "/login",
                    dataType: "jsonp",
                    data: this.qs.stringify(date)
                }).then((data) => {
                    if (data.data.code == 200) {
                        this.$cookies.set("login", data.data.cookie, 7 * 24 * 60 * 60);
                        alert("成功");
                        // this.$router.push("/login")
                        window.location.href = "/login"
                    } else {
                        alert("账号或者密码输入错误")
                    }
                }).catch((error) => {
                    alert(error)
                })
            }
        }
    }
</script>

<style scoped>

</style>

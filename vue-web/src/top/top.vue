<template>
    <div class="top">
        <div class="dropdown">
            <!--      <li role="presentation" class="active"><a href="#"><img class="logo"-->
            <!--                                                              alt="测试背景"></a></li>-->
            <ul class="nav  nav-tabs">
                <li role="presentation"><a href="/" title="点击进入主页"><span
                        class="glyphicon glyphicon-home "
                        aria-hidden="false"></span>首页</a></li>

                <li><a class="dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true"
                       aria-expanded="false">
                    详细选项 <span class="caret"></span>
                </a>
                    <ul class="dropdown-menu">

                        <li role="presentation"><a class="" href="#" title="查看详细信息"><span
                                class="glyphicon glyphicon-user"
                                aria-hidden="false"></span> 个人信息</a></li>
                        <li role="presentation"><a class="jc col-xs-6 col-md-4" href="#" title="查看公共消息"><span
                                class="glyphicon glyphicon-th-large"
                                aria-hidden="false"></span>我们的故事</a></li>
                    </ul>
                </li>
                <!--        音乐控件-->
                <audio src="" controls="controls"></audio>
                <li role="presentation" class="login-reght" style="display: none" id="login"><a   href="/login" title="点击进行登录"><span
                        class="glyphicon glyphicon glyphicon-user "
                        aria-hidden="false"></span>登录</a></li>
                <li style="display: none" id="login-list" role="presentation" class="dropdown login-reght">
                    <a class=" dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true"
                       aria-expanded="false">
                        用户管理 <span class="caret"></span>
                    </a>
                    <ul class="dropdown-menu">
                        <li role="presentation"><a href="#">个人信息</a></li>
                        <li role="presentation"><a href="#" @click="this.logout">退出登录</a></li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</template>


<script>
    // import $ from "jquery"
    export default {
        name: "top",
        created() {
            window.addEventListener("load",() =>{
                if (this.$cookies.get("login") != null){
                    $("#login").css("display","none")
                    $("#login-list").css("display","inline")
                } else {
                     $("#login").css("display","inline")
                     $("#login-list").css("display","none")
                }
            })
        },
        methods: {
            login: function () {
                var login = $.cookie("login");
                if (login != null) {
                    var success = $.get("/login/loginAuth", function (date) {
                        return date.success
                    });
                    if (success === true) {
                        $("#login-list").show();
                        $("#login").hide();
                    } else if (success === false) {
                        $("#login").show();
                        $("#login-list").hide();
                        $.cookie("login", null)
                    }
                } else {
                    $("#login").show();
                    $("#login-list").hide();
                }

            },
            logout: function () {
                this.$cookies.remove("login");
                window.location.reload()
            }
        },
        components: {}

    }
</script>

<style scoped>
    .login-reght {
        float: right;

    }

</style>

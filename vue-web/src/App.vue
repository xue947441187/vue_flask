<template>
    <div id="app" class="container-fluid">
        <top></top>
        <!--<login></login>-->
        <router-view></router-view>
        <!--<button type="button" @click="test">test</button>-->
        <div class="container">
            <div class="row">
                <div class="col-md-6">
                    <button class="btn btn-primary"  @click="test">测试按钮</button>
                </div>
            </div>
        </div>
    </div>

</template>


<script>
    import top from './top/top';
    // import login from './login/login'
    // import $ from  "jquery"
    export default {
        name: 'App',
        methods: {
            test: function () {
                $.ajax(
                    "http://127.0.0.1:5000" + '/test',
                    {
                        type: "GET",
                        changeOrigin: true,
                        success: function (date) {
                            alert(date.success)
                        }
                    }
                )
            }
        },
        components: {
            top: top,
            // login: login
        },
        created() {
        },
    }
</script>

<style>
    App {

    }

</style>

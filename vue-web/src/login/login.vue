<template>
  <div class="login">
   <div class="container">



    <div class="modal-dialog" style="margin-top: 10%;">
        <div class="modal-content">
            <div class="modal-header">

                <h4 class="modal-title text-center" id="myModalLabel">登录</h4>
            </div>
            <div class="modal-body" id = "model-body">
                <div class="form-group">

                    <input type="text" class="form-control" placeholder="用户名" autocomplete="off">
                </div>
                <div class="form-group">

                    <input type="password" class="form-control" placeholder="密码" autocomplete="off">
                </div>
            </div>
            <div class="modal-footer">
                <div class="form-group">
                    <button type="button" class="btn btn-primary form-control">登录</button>
                </div>
                <div class="form-group">
                    <button type="button" class="btn btn-default form-control" @click="this.loadFro" >注册</button>
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

  }
</script>

<style scoped>

</style>

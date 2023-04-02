<template>
	<div id="header">
      <button class="btn btn-primary" @click="this.$router.push({name:'Post'});">Home</button>
      <button class="btn btn-primary" @click="this.$router.push({name:'Register'});">Register</button>
  </div>
  <br><br><br>
	<div>
    <h1>Login</h1>
    <div class="row mx-auto">
		<form class="mx-auto" style="max-width: 450px" action="https://m-fake-rest-api-nodejs.herokuapp.com/login" @submit.prevent="login()">
          <div class="alert alert-danger" v-if="error">
           {{error.response.data.message}}
          </div>
          <div class="form-group">
            <input v-model="loginUser.email" type="email" class="form-control" placeholder="Enter email">
          </div>
          <div class="form-group">
            <input v-model="loginUser.password" type="password" class="form-control" placeholder="Enter password">
          </div>
          <div class="form-group">
            <button style="width: 100%" role="button" class="btn btn-primary btn-block">Login</button>
          </div>
        </form>
      </div>
	</div>
</template>

<script>

import LoginRequest from '../requests/LoginRequest'

export default{
	name : "CompLogin",
	data(){
		return{
			loginUser:{
				email:'',
				password:''
			},
			error:null,
		}
	},
	mounted(){

	},
	computed:{

	},
	methods:{
		login:function(){
			LoginRequest.post('login',this.loginUser)
			.then( data => {
				console.log("login success !");
        window.localStorage.setItem('user',JSON.stringify(data));
				this.$router.push({name:'Post'}); 
        this.error = null ;
			})
			.catch( error => {
        this.error = error;
				console.log(error.message);
				console.log("login false !");
			})
		},
	}
}
</script>

<style scoped>
#header{
  position: fixed;
  top: 10px;
  left: 30px;
  background-color: #edf2ff;
  width: 180px;
  height: 60px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  line-height: 60px;
  border-radius: 6px;
  padding-left: 10px;
  padding-right: 10px;
}
</style>
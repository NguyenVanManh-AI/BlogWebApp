<template>
  <div>
    <div class="header" id="li2" v-if="user!=null">
      <button class="btn btn-success" @click="this.$router.push({name:'PostNew'});">New</button>
      <button class="btn btn-primary" @click="this.$router.push({name:'Post'});">Home</button>
      <button class="btn btn-secondary" @click="logout">Logout</button>
    </div>
    <div id="header2" v-if="user==null">
      <button class="btn btn-outline-primary" @click="this.$router.push({name:'Post'});">Home</button>
    </div>
    <h1>Post Detail</h1>
    <br><hr><br>
    <div id="post">
        <h1 class="alert alert-primary" role="alert">{{post.title}}</h1>
        <p id="content" class="alert alert-secondary" role="alert">{{post.content}}</p>
        <img :src="post.link_img" >
        <p>{{post.read_number}}</p>
        <p class="alert alert-success" role="alert" >Tác giả : {{post.auth}}</p>
        <!-- <p>ID_USER : {{post.id_user}}</p> -->
        Status <input type="checkbox" v-model="post.status" disabled>
        <div v-if="check"> 
            <button class="btn btn-primary" @click="editPost(post.id)">Edit</button> 
            <button class="btn btn-danger" @click="deletePost(post.id,post.title)" style="margin-left: 10px;">Delete</button> 
        </div>
        <br><hr><br>
    </div>
  </div>
</template>


<script scoped>

import BaseRequest from '@/core/BaseRequest';

export default {
    name : "DetailPost",
    data(){
        return{
            post:{
                id:null,
                id_user:null,
                auth:'',
                title: '',
                content: '',
                read_number: null,
                link_img :'', 
                status: null
            },
            user:null,
            check:false,
        }
    },
    computed(){

    },
    mounted(){
        this.user = JSON.parse(window.localStorage.getItem('user'));
        this.getPosts(window.location.pathname);
    },
    methods:{
        editPost:function(id_post){
            console.log(id_post);
            this.$router.push({name:'PostEdit'}); 
            window.localStorage.setItem('id_post',id_post);
        },
        deletePost:function(id_post,title){
            let text = "Bạn có chắc chắn muốn xóa bài viết : '"+title+"' !\nNhấn OK or Cancel.";
            if (confirm(text) == true) {
                BaseRequest.delete('posts/'+id_post)
                .then(()=>{
                    alert('Xóa bài viết : "'+title+'" thành công !');
                    this.$router.push({name:'Post'}); 
                })
                .catch(error => {
                    console.log(error.reponse.status)
                })
            } 
        },
        logout:function(){
			localStorage.clear();
			this.$router.push({name:'Login'});
		},
        getPosts:function(pathn){
            // BaseRequest.get(pathn.substring(1,pathn.length))
            BaseRequest.get('posts/'+pathn.slice(7,pathn.length))
                .then( data=>{
                    this.post = data ; 
                    if(this.user != null && this.post.id_user == this.user.id){
                        this.check = true ;
                    }
                }) 
                .catch(error=>{
                    console.log(error.reponse.status);
                })
        }
    }
}
</script>

<style>
#header2{
  position: fixed;
  top: 10px;
  left: 30px;
  background-color: #edf2ff;
  height: 60px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  line-height: 60px;
  border-radius: 6px;
  padding-left: 10px;
  padding-right: 10px;
}
.header{
  position: fixed;
  top: 10px;
  left: 30px;
  background-color: #edf2ff;
  height: 60px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  line-height: 60px;
  border-radius: 6px;
  padding-left: 10px;
  padding-right: 10px;
}
#li1 {
  width: 180px;
}
#li2{
  width: 260px;
}
#post {
    margin: 30px;
}
#content {
    margin-left: 100px;
    margin-right: 100px;
}
#post img {
    width: 500px;
}
</style>
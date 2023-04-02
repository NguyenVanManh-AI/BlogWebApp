<template>
    <div class="header" id="li1" v-if="user==null">
      <button class="btn btn-outline-primary" @click="this.$router.push({name:'Login'});">Login</button>
      <button class="btn btn-outline-primary" @click="this.$router.push({name:'Register'});">Register</button>
    </div>

    <h1>Home</h1>
    <h1 class="alert alert-success" role="alert" v-if="user==null">Signin to create a post !</h1>
    <div class="header" id="li2" v-if="user!=null">
      <button class="btn btn-success" @click="this.$router.push({name:'PostNew'});">New</button>
      <button class="btn btn-primary" @click="this.$router.push({name:'MyPost'});">My Posts</button>
      <button class="btn btn-secondary" @click="logout">Logout</button>
    </div>
    <br><hr><br>
    <div class="article">
      <div v-for="(postt,index) in list_post" :key="index">
        <button class="showm btn-outline-primary" @click="showMore(postt.id)">Show More</button>
        <p class="back-gr"></p>
        <img :src="postt.link_img" >
        <h3>{{postt.title}}</h3>
        <p>{{postt.content}}</p>
        <p>{{postt.read_number}}</p>
        <p>Tác giả : {{postt.auth}}</p>
        <!-- <p>ID_USER : {{postt.id_user}}</p> -->
        <p>Id Post : {{postt.id}}</p>
        Status <input type="checkbox" v-model="postt.status" disabled>
        <br><hr><br>
      </div>
    </div>
    
    <paginate class="pag"
      :page-count="Math.ceil(this.number_post/6)"
      :page-range="3"
      :margin-pages="2"
      :click-handler="clickCallback"
      :prev-text="'Prev'"
      :next-text="'Next'"
      :container-class="'pagination'"
      :page-class="'page-item'">
    </paginate>
</template>


<script scoped>

import Paginate from 'vuejs-paginate-next';
import BaseRequest from '@/core/BaseRequest';

export default {
    name : "CompPost",
    components:{
        paginate: Paginate
    },
    data(){
        return{
            posts:null,
            user:null,
            number_post:null,
            list_post:null,
            show:true,
        }
    },
    computed:{

    },
    mounted(){
        BaseRequest.get('posts')
        .then( data =>{
            this.posts = data ; 
            this.number_post = this.posts.length;
            this.list_post = this.posts.slice(0, 6);
        }) 
        .catch(error=>{
            console.log(error.reponse.status);
        }),
        this.user = window.localStorage.getItem('user');

    },
    methods:{
      logout:function(){
        localStorage.clear();
        this.$router.push({name:'Login'});
      },
      clickCallback : function(pageNum){
        if(pageNum == 1){
          this.list_post = this.posts.slice(0, 6);
        }
        else {
          this.list_post = this.posts.slice((pageNum-1)*6, 6*pageNum);
        }
      },
      showMore:function(id_post){
				this.$router.push({name:'DetailPost',params:{id:id_post}}); 
      }
    }

}
</script>

<style scoped>

/* google font */
@import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');/* font */
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
.pag {
  margin-left:41%;
  margin-bottom: 60px;
}
.article{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  padding: 20px;
}
.article h3 {
  margin-top: 10px; /* font */
  font-family: 'Lobster', cursive;
}
.article div {
  width: 30%;
  border-top: 6px solid white;
  border-left: 6px solid white;
  box-shadow: 20px 20px 10px -10px gray;
  border-radius:20px ;
  height: 360px;
  margin: 10px;
  overflow: hidden;
  position: relative;
}
.article div img {
  width: 100%;
}
.article div:hover {
  width: 32%;
  cursor: pointer;
  /* box-shadow: none; */
}
.article div:hover > .back-gr{
  display: none;
}
.article div:hover > .showm{
  display: block;
}
.showm{
  position: absolute;
  top: 6%;
  right: 5%;
  display: none;
  background-color: transparent;
  border-radius: 6px;
}

.back-gr{
  position:absolute;
  bottom:-20px;
  left:0px;
  background: rgb(209,137,137);
  background: linear-gradient(0deg, rgb(94 168 239) 0%, rgba(245,177,33,0) 100%);
  width: 100%;
  height: 60%;
}


</style>
<template>
  <div>
    <div class="header" id="li2" v-if="user!=null">
      <button class="btn btn-success" @click="this.$router.push({name:'PostNew'});">New</button>
      <button class="btn btn-primary" @click="this.$router.push({name:'Post'});">Home</button>
      <button class="btn btn-secondary" @click="logout">Logout</button>
    </div>
    <h1>My Posts</h1>
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
  </div>
</template>


<script scoped>

import BaseRequest from '@/core/BaseRequest';
import Paginate from 'vuejs-paginate-next';

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
            myPosts:[],
            list_post:null,
        }
    },
    computed(){
        console.log(this.posts);
    },
    mounted(){
        this.user = window.localStorage.getItem('user');
        this.getPosts();
    },
    methods:{
        editPost:function(id_post){
            console.log(id_post);
            window.location="https://blog-nvm.herokuapp.com/post/edit"
            window.localStorage.setItem('id_post',id_post);
        },
        deletePost:function(id_post,title){
            let text = "Bạn có chắc chắn muốn xóa bài viết : '"+title+"' !\nNhấn OK or Cancel.";
            if (confirm(text) == true) {
                console.log(id_post);
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
        getPosts:function(){
            BaseRequest.get('posts')
                .then( data=>{
                    this.posts = data ; 
                    this.filt(this.posts);
                }) 
                .catch(error=>{
                    console.log(error.reponse.status);
                })
        },
        filt:function(posts){
            for(let i=0;i<posts.length;i++){
                if(posts[i].id_user == JSON.parse(this.user).id){
                    this.myPosts.push(posts[i]);
                }
            }
            this.number_post = this.myPosts.length;
            this.list_post = this.myPosts.slice(0, 6);
        },
        clickCallback : function(pageNum){
            if(pageNum == 1){
                this.list_post = this.myPosts.slice(0, 6);
            }
            else {
                this.list_post = this.myPosts.slice((pageNum-1)*6, 6*pageNum);
            }
        },
        showMore:function(id_post){
            this.$router.push({name:'DetailPost',params:{id:id_post}}); 
        }
    }
}
</script>

<style scoped>
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
  background: linear-gradient(0deg, rgb(211, 180, 249) 0%, rgba(245,177,33,0) 100%);
  width: 100%;
  height: 60%;
}

</style>
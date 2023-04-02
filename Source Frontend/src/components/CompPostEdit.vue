<template>
    <div id="header">
      <button class="btn btn-outline-primary" @click="this.$router.push({name:'Post'});">Home</button>
    </div>
  <div>
    <h1>Edit Post</h1>
    <br><hr><br>
    <h1>Title</h1>
    <input v-model="post.title" style="width:600px;font-weight: bold;">
    <h2>Content</h2>
    <textarea v-model="post.content" style="width:600px;height: 300px;"></textarea>
    <h3>Link Img</h3>
    <input v-model="post.link_img" style="width:600px">
    <h3>Reader Number</h3>
    <input v-model="post.read_number">
    <h3>Status</h3>
    <input type="checkbox" v-model="post.status">
    <div> <button class="btn btn-primary" @click="savePost(post.id)">Save</button> </div>

    <br><hr><br>
  </div>
</template>

<script>

import BaseRequest from '@/core/BaseRequest';

export default {
    name : "PostEdit",
    data(){
        return{
            id_post:null,
            post:{
                id:null,
                title: '',
                content: '',
                read_number: null,
                link_img :'', 
                status: null
            }
        }
    },
    mounted(){
        this.id_post = window.localStorage.id_post;
        BaseRequest.get('posts/'+this.id_post)
        .then( data =>{
            this.post = data;
        }) 
        .catch(error=>{
            console.log(error.reponse.status);
        })

    },
    methods:{
        savePost:function(id_post){
            BaseRequest.put('posts/'+id_post,this.post)
            .then( () =>{
                alert("Chỉnh sửa bài viết thành công !");
                this.$router.push({name:'Post'}); 
                window.localStorage.removeItem('id_post');
            }) 
            .catch(error=>{
                console.log(error.reponse.status);
            })
        }
    },
    components:{

    }

}
</script>

<style scoped>
#header{
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
</style>
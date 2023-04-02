<template>
    <div id="header">
      <button class="btn btn-outline-primary" @click="this.$router.push({name:'Post'});">Home</button>
    </div>
  <div>
    <h1>New Post</h1>
    <br><hr><br>
    <h1>Title</h1>
    <input v-model="post.title" style="width:600px;font-weight: bold;" placeholder="Title">
    <h2>Content</h2>
    <textarea v-model="post.content" style="width:600px;height: 300px;" placeholder="Content"></textarea>
    <!-- <RichTextEditorVue v-model="post.content" style="width:600px;height: 300px;" placeholder="Content"></RichTextEditorVue> -->
    <h3>Link Img</h3>
    <input v-model="post.link_img" style="width:600px" placeholder="Link img">
    <h3>Reader Number</h3>
    <input v-model="post.read_number">
    <h3>Status</h3>
    <input type="checkbox" v-model="post.status">
    <div> <button class="btn btn-primary" @click="addPost()">Add</button> </div>

    <br><hr><br>
    <!-- <TinymceEditorVue></TinymceEditorVue> -->
  </div>
</template>

<script>
import BaseRequest from '@/core/BaseRequest';
// import RichTextEditorVue from './RichTextEditor.vue';
// import TinymceEditorVue from './TinymceEditor.vue'

export default {
    
    name : "PostNew",
    components:{
        // RichTextEditorVue,
        // TinymceEditorVue
    },
    data(){
        return{
            id_post:null,
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
        }
    },
    mounted(){

    },
    methods:{
        addPost:function(){
            this.post.id_user = JSON.parse(window.localStorage.getItem('user')).id;
            this.post.auth = JSON.parse(window.localStorage.getItem('user')).lastName + 
                            JSON.parse(window.localStorage.getItem('user')).firstName;
            BaseRequest.post('posts',this.post)
            .then(()=>{
                alert("Thêm bài viết thành công !");
				this.$router.push({name:'Post'}); 
            }) 
            .catch(error=>{
                console.log(error.reponse.status);
            })
        }
    }

}
</script>

<style scoped>

#d1{
    width: 600px;
    height: 600px;
    display: inline-block;
}
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
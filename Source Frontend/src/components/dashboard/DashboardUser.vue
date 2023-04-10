<template>
    <div id="dashboard_user">
      <div id="title_blog"><i class="fa-solid fa-blog"></i> Blog App</div>
      <div id="post_article" v-if="user" data-toggle="modal" data-target="#modalPostArticle">
        <div id="avatar"><img :src="user.avatar" /></div>
        <div id="post">Hey {{ user.fullname }} , what are you thinking ?</div>
      </div>
      <!-- Model Post Aticle -->
      <div class="modal fade" id="modalPostArticle" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">New Article</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <ModalPostArticle></ModalPostArticle>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
              <!-- <button type="button" class="btn btn-primary">Save changes</button> -->
            </div>
          </div>
        </div>
      </div>



      <div v-for="(article,index) in articles" :key="index">

        <div style="border: 1px solid red;padding: 20px;">
          <p style="background-color: pink;"> <br> article.article.id : {{ article.article.id }} </p>
          <p style="background-color: blue;"> <br> article.article.id_user : {{ article.article.id_user }} </p>
          <p style="background-color: red;"> <br> article.article.title : {{ article.article.title }} </p>
          <p style="background-color: green;" v-html="article.article.content"></p>
          <p style="background-color: yellow;" > <br> article.article.created_at : {{ article.article.created_at }} </p>
        </div>
        <br>
        <div style="border: 1px solid red;padding: 20px;">
          {{ article.user.id }}
          {{ article.user.fullname }}
          {{ article.user.avatar }}
        </div>


        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
      </div>






      
        <div v-for="comment in comments" :key="comment.id">
        <div v-if="!editingComment || editingComment.id !== comment.id">
            <p>{{ comment.content }}</p>
            <button @click="showEditModal(comment)">Edit</button>
            <button @click="deleteComment(comment)">Delete</button>
        </div>
        <div v-else>
            <h3>Edit comment</h3>
            <textarea v-model="editingComment.content"></textarea>
            <button @click="saveComment()">Save</button>
            <button @click="cancelEdit()">Cancel</button>
        </div>
        </div>
        <Notification></Notification>
    </div>
</template>
<script>

import BaseRequest from '../../restful/user/core/BaseRequest';
import useEventBus from '../../composables/useEventBus';
import Notification from './../Notification';
import config from '../../config.js';
// import ParticleVue32 from "../particle/ParticleVue32.vue";
// import FilePicker from './FilePicker.vue';

import ModalPostArticle from './ModalPostArticle'

export default {
    name : "DashboardUser",
    components: {
      Notification,
      ModalPostArticle
    },
    data(){
        return{
          user:{
            id:null,
            email:null,
            date_of_birth:null,
            gender:null,
            fullname:null,
            avatar:null,
            access_token:null,
          },
          articles:null,
          pageN:1,
          quantity:null,


          comments: [
            { id: 1, content: "Comment 1" },
            { id: 2, content: "Comment 2" },
            { id: 3, content: "Comment 3" },
          ],
      showModal: false,
      editingComment: null,
        }
    },
    created(){

    },
    mounted(){
      this.user = JSON.parse(window.localStorage.getItem('user'));
      if(this.user){
        if(this.user.avatar) this.user.avatar = config.API_URL + this.user.avatar ;
      }
      BaseRequest.get('articles')
      .then( data => {
        this.articles = data.results;
        this.quantity = data.count;
        const { emitEvent } = useEventBus();
        emitEvent('eventSuccess','Get All Article Success !');
      })
      .catch( () => {
        const { emitEvent } = useEventBus();
        emitEvent('eventError','Get All Article Fail !');
      })
    },
    methods:{
showEditModal(comment) {
      this.editingComment = comment;
      this.showModal = true;
    },
    saveComment() {
      // Save edited comment to the backend
      // ...
      this.showModal = false;
      this.editingComment = null;
    },
    cancelEdit() {
      this.showModal = false;
      this.editingComment = null;
    },
    deleteComment(comment) {
      // Delete comment from the backend
      // ...
      this.comments = this.comments.filter((c) => c.id !== comment.id);
    },
    },
}
</script>
<style scoped>
#title_blog {
  font-size: 30px;
  display: flex;
  justify-content: center;
  font-weight: bold;
  text-transform: uppercase;
  letter-spacing: 5px;
  color: #0085FF;
  background-color: white;
  margin-bottom: 10px;
  border-radius: 10px;
  border: 1px solid silver;
  align-items: center;
  padding: 3px;
}
#title_blog i {
  margin-right: 10px;
}
#dashboard_user {
  /* border: 1px solid green; */
  padding: 10px;
  background-color: #F2F4F6;
  overflow: hidden;
  overflow-y: scroll;
  height: 100vh;
}
#post_article {
  display: flex;
  padding: 10px;
  border-radius: 10px;
  border: 1px solid silver;
  background-color: white;
  cursor: pointer;
  margin-bottom: 10px;
}
#avatar img {
  cursor: pointer;
  max-width: 150% !important;
  width: 40px;
  height: 40px;
  object-fit:cover;
  border-radius: 20px;
}
#post {
  padding-left: 20px;
  display: flex;
  align-items: center;
  height: 40px;
  margin-left: 10px;
  width: -webkit-fill-available;
  background-color: #F2F4F6;
  border-radius: 20px;
}
</style>
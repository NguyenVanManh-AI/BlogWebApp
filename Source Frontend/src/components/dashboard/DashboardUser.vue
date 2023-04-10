<template>
    <div id="dashboard_user">
      <div id="title_blog"><i class="fa-solid fa-blog"></i> Blog App</div>
      <div id="post_article" v-if="user" data-toggle="modal" data-target="#modalPostArticle">
        <div id="avatar">
          <img :src="user.avatar" alt="Avatar" v-if="user.avatar != null" />
          <img src='../../assets/avatar.png' alt="Avatar" v-if="user.avatar == null"> 
        </div>
        <div id="post">Hey {{ user.fullname }} , what are you thinking ?</div>
      </div>
      <!-- Model Post Aticle -->
      <div v-if="user" class="modal fade" id="modalPostArticle" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel" style="font-weight: bold;color: #0076e5;font-size: 20px;"><i class="fa-solid fa-feather"></i> New Article</h5>
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
      <!-- Model Post Aticle -->

      <!-- Article -->
      <div v-for="(article,index) in articles" :key="index" class="big_article">
        <div class="header_article">
          <div class="avatar_article">
            <img :src="process_url(article.user.avatar)" alt="Avatar" v-if="article.user.avatar != null" />
            <img src='../../assets/avatar.png' alt="Avatar" v-if="article.user.avatar == null"> 
          </div>
          <div class="infor_article">
            <div class="infor_left">
              <p class="infor_fullname">{{ article.user.fullname }}</p>
              <p class="infor_created">{{ process_date(article.article.created_at) }}</p>
            </div>
            <div class="infor_right">
              <button class="btn_setting" @click="showSetting(index)"><i class="fa-solid fa-ellipsis" ></i></button>
              <div class="show_setting" v-if="show_setting[index]">
                <li data-toggle="modal" data-target="#modalDeleteArticle"><span class="setting_icon"><i class="fa-solid fa-trash"></i></span> <span>Delete Article</span></li>
                <li><span class="setting_icon"><i class="fa-solid fa-bookmark"></i></span> <span>Save Articlee</span></li>
                <li><span class="setting_icon"><i class="fa-solid fa-user-xmark"></i></span> <span>Unfollow</span></li>
                <li><span class="setting_icon"><i class="fa-solid fa-flag"></i></span> <span>Report Article</span></li>
              </div>
            </div>
          </div>
        </div>
        <div class="content_main_article">
          <div @click="get_article_detail(article)" class="main_title" data-toggle="modal" data-target="#modalArticleDetails" >
            <i class="fa-solid fa-play"></i> {{ article.article.title }}
          </div>
          <div class="main_center">
            <i class="fa-solid fa-blog"></i>
          </div>
          <div class="main_content" >
            <div v-html="article.article.content"></div>
          </div>
        </div>
        <div class="footer_article">
          <div @click="get_article_detail(article)" class="footer_number_comment" data-toggle="modal" data-target="#modalArticleDetails" >
              <!-- {{ article.comment.length }} -->
            9999 Comments
          </div>
          <div class="footer_comment_article">
            <div @click="get_article_detail(article)" data-toggle="modal" data-target="#modalArticleDetails" ><span><i class="fa-regular fa-message"></i></span> <span>Comments</span></div>
            <div @click="get_article_detail(article)" data-toggle="modal" data-target="#modalArticleDetails"><span><i class="fa-regular fa-eye"></i></span> <span>View Details</span></div>
          </div>
        </div>


      <!-- Article -->

      
      <!-- Model Post Aticle -->

        <!-- <div >
          <p> <br> article.article.id : {{ article.article.id }} </p>
          <p> <br> article.article.id_user : {{ article.article.id_user }} </p>
          <p> <br> article.article.title : {{ article.article.title }} </p>
          <p v-html="article.article.content"></p>
          <p><br> article.article.created_at : {{ article.article.created_at }} </p>
        </div>
        <br>
        <div >
          {{ article.user.id }}
          {{ article.user.fullname }}
          {{ article.user.avatar }}
        </div> -->
      </div>

      <!-- Model Aticle Detail -->
      <div v-if="user" class="modal fade" id="modalArticleDetails" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog fix_width_modal" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel" style="font-weight: bold;color: #0076e5;font-size: 20px;"><i class="fa-solid fa-feather"></i> Details Article</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <ModalArticle v-bind:article="this.article_detail"></ModalArticle>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
              <!-- <button type="button" class="btn btn-primary">Save changes</button> -->
            </div>
          </div>
        </div>
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

        <div id="divpaginate">
          <paginate class="pag" id="nvm"
              :page-count="Math.ceil(this.quantity/6)"
              :page-range="3"
              :margin-pages="2"
              :click-handler="clickCallback"
              :initial-page="this.pageN"
              :prev-text="'Prev'"
              :next-text="'Next'"
              :container-class="'pagination'"
              :page-class="'page-item'">
          </paginate>
      </div>
      <Notification></Notification>
    </div>
</template>
<script>

import BaseRequest from '../../restful/user/core/BaseRequest';
import useEventBus from '../../composables/useEventBus';
import Notification from './../Notification';
import config from '../../config.js';
import Paginate from 'vuejs-paginate-next';

// import ParticleVue32 from "../particle/ParticleVue32.vue";
// import FilePicker from './FilePicker.vue';

import ModalPostArticle from './ModalPostArticle'
import ModalArticle from './ModalArticle'

export default {
    name : "DashboardUser",
    components: {
      Notification,
      ModalPostArticle,
      paginate: Paginate,
      ModalArticle
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
          article_detail:null,
          // length_articles:null,
          // show_setting: new Array(this.length_articles).fill(false),
          show_setting: new Array(10).fill(false), // vì mỗi lần mình lấy ra 10 bài viết nên k cần tính nữa, thiếu thì ít hơn 10 bài viết thôi 
          //  đôi khi chỗ này có thể để 9999 thay vì 10 => lấy bao nhiêu bài viết cũng được , miễn <= 9999 là nó hoạt động 
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
        // this.length_articles = Object.keys(this.article).length;
        this.quantity = data.count;
        const { emitEvent } = useEventBus();
        emitEvent('eventSuccess','Get All Article Success !');
      })
      .catch( () => {
        const { emitEvent } = useEventBus();
        emitEvent('eventError','Get All Article Fail !');
      })

      // click bất cứ thứ gì ngoài button show setting đều làm cho ẩn show setting đó 
      document.addEventListener('click', this.handleOutsideClick);
    
    },
    
    beforeUnmount() {

      // click bất cứ thứ gì ngoài button show setting đều làm cho ẩn show setting đó 
      document.removeEventListener('click', this.handleOutsideClick);
    },


    methods:{
      process_url(path){
        return config.API_URL + path.slice(1);
      },
      showSetting(index){
        // giúp cho khi click vào bài khác thì bài đó tự ẩn cái đang hiện ra 
        if(this.show_setting[index] == true) this.show_setting[index] = false;
        else {
          this.show_setting = new Array(10).fill(false);
          this.show_setting[index] = true;
        }
      },
      process_date(day){
        const dateString = day;
        const date = new Date(Date.parse(dateString));
        const month = date.toLocaleString('default', { month: 'short' });
        // const formattedDate = `${("0" + date.getDate()).slice(-2)} month, ${date.getFullYear()}`;
        const formattedDate = `${("0" + date.getDate()).slice(-2)} ${month}, ${date.getFullYear()}`;
        return formattedDate;
      },

      // click bất cứ thứ gì ngoài button show setting đều làm cho ẩn show setting đó 
      handleOutsideClick(event) {
        if (!event.target.closest('button')) {
          this.show_setting = new Array(10).fill(false);
        }
      },

      clickCallback:function(pageNum){
        this.pageN = pageNum;
        this.getArticles(pageNum);
      },
      get_article_detail(article){
        this.article_detail = article;
        // console.log(this.article_detail);
      },


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

/* Post Article */
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
  padding-left: 25px;
  padding-right: 25px;
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
  transition: all 0.5s ease;
}
#post:hover {
  background-color: #e0e0e0;
}


/* Article */

.big_article {
  background-color: white;
  border-radius: 10px;
  border: 1px solid silver;
  margin-bottom: 10px;
  padding: 10px;
}
.header_article {
  border-bottom: 2px solid rgb(219, 219, 219);
  display: flex;
  padding-bottom: 10px;
}
.avatar_article img {
  cursor: pointer;
  max-width: 150% !important;
  width: 40px;
  height: 40px;
  object-fit:cover;
  border-radius: 20px;
}
.infor_article {
  display: flex;
  align-items: center;
  height: 40px;
  margin-left: 10px;
  width: -webkit-fill-available;
  border-radius: 20px;
  transition: all 0.5s ease;
  justify-content: space-between;
}
.infor_right {
  position: relative;
}
div.show_setting {
  padding: 10px;
  position: absolute;
  top: 36px;
  right: 0px;
  background-color: white;
  width: max-content;
  border: 1px solid silver;
  border-radius: 10px;
}
div.show_setting li {
  margin: 3px ;
  display: flex;
  align-items: center;
  cursor: pointer;
  padding: 5px 10px;
}
div.show_setting li:hover {
  color: #F84B2F;
  background-color: #ebebeb;
  border-radius: 10px;
}
div.show_setting li .setting_icon{
  display: inline-block;
  width: 10%;
  align-items: center;
  text-align: center;
  margin-right: 16px;
}

.infor_fullname {
  font-weight: bold;
}
.infor_fullname:hover {
  text-decoration: underline;
  cursor: pointer;
}
.infor_created {
  font-size: 14px;
  cursor: pointer;
}
.infor_created:hover {
  /* text-decoration: underline; */
  color: #0085FF;
}
.btn_setting {
  border-radius: 20px;
  padding: 6px;
  width: 30px;
  height: 30px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.btn_setting:hover {
  background-color: #e0e0e0;
}


/* content_main_article */
.content_main_article {

}

.main_title {
  font-weight: bold;
  font-style: italic;
  padding-top: 10px;
  margin-bottom: 10px;
  /* cursor: pointer; */
  
  /* Sử dụng kỹ thuật clamp() để giới hạn chiều cao */
  height: clamp(0px, 60px, auto);
  
  /* Ẩn dấu ba chấm ban đầu */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  -webkit-line-clamp: 2; /* giới hạn số dòng */
}

.main_center {
  display: flex;
  justify-content: center;
  margin-bottom: 10px;
}
.main_content {
  max-height: 500px;
  overflow: hidden;
  overflow-y: scroll;
}

/* footer */
.footer_article {
  margin-top: 10px;
  border-top: 1px solid silver;
}

.footer_number_comment {
  display: flex;
  justify-content: end;
  padding: 10px;
  border-bottom: 1px solid silver;
  font-size: 15px;
  color: #767676;
}
.footer_number_comment:hover {
  text-decoration: underline;
  cursor: pointer;
  color: #0085FF;
}

.footer_comment_article {
  display: flex;
  justify-content: space-between;
  padding: 10px 30%;
  padding-bottom: 0px;
}

.footer_comment_article > div {
  border-radius: 6px;
  padding: 3px 10px;
  cursor: pointer;
}

.footer_comment_article > div:hover {
  background-color: #e0e0e0;
  color: #0085FF;
}


/* paginate */

#divpaginate {
  /* bottom: 10px; */
  position: absolute;
  width: 100%;
  display: flex;
  justify-content: center;
  right: 0px;
  bottom: 10px;
}
.pagination {
  margin-left: 150% !important;
  z-index: 999;
  cursor: pointer;
}


/* ModalArticle */
.fix_width_modal {
  width: 60% !important;
}







</style>
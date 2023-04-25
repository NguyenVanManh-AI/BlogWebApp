<template>
    <div id="dashboard" class="row m-0">
        <div id="left" class="col-3 p-0"><DashboardLeft></DashboardLeft></div>
        <div class="col-6 p-0" style="background-color: #F2F4F6;">
            <div id="dashboard_user">
                <div id="modal_article" v-if="full_article">
                    <div class="big_article">
                        <div class="header_article">
                            <div class="avatar_article">
                                <img :src="process_url(full_article.user.avatar)" alt="Avatar" v-if="full_article.user.avatar != null" />
                                <img src='../../assets/avatar.png' alt="Avatar" v-if="full_article.user.avatar == null"> 
                            </div>
                            <div class="infor_article">
                                <div class="infor_left">
                                    <p class="infor_fullname" @click="goInforAccount(full_article.user.id)">{{ full_article.user.fullname }}</p>
                                    <p class="infor_created" @click="goArticle(full_article.article.id)">{{ process_date(full_article.article.created_at) }}</p>
                                </div>
                                <div class="infor_right" v-if="user">
                                <button class="btn_setting" @click="show_setting = !show_setting"><i class="fa-solid fa-ellipsis" ></i></button>
                                    <div class="show_setting" v-if="show_setting">
                                        <li class="li_edit" v-if="user.id == full_article.article.id_user" @click="editArticle(full_article.article.id)"><span class="setting_icon"><i class="fa-solid fa-pen-nib"></i></span> <span>Edit Article</span></li>
                                        <li class="li_delete" v-if="user.id == full_article.article.id_user" @click="openModel(full_article.article.id);" data-toggle="modal" data-target="#exampleModalDelete"><span class="setting_icon"><i class="fa-solid fa-trash"></i></span> <span>Delete Article</span></li>
                                        <li class="li_save" v-if="user.id != full_article.article.id_user" @click="saveArticle" ><span class="setting_icon"><i class="fa-solid fa-bookmark"></i></span> <span>Save Articlee</span></li>
                                        <li class="li_unfollow" v-if="user.id != full_article.article.id_user" @click="unfollowUser" ><span class="setting_icon"><i class="fa-solid fa-user-xmark"></i></span> <span>Unfollow</span></li>
                                        <li class="li_report" v-if="user.id != full_article.article.id_user" @click="reportArticle" ><span class="setting_icon"><i class="fa-solid fa-flag"></i></span> <span>Report Article</span></li>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="content_main_article">
                            <div @click="get_article_detail(article)" class="main_title" data-toggle="modal" data-target="#modalArticleDetails" >
                                <i class="fa-solid fa-play"></i> {{ full_article.article.title }}
                            </div>
                            <div class="main_center">
                                <i class="fa-solid fa-blog"></i>
                            </div>
                            <div class="main_content" >
                                <div v-html="full_article.article.content"></div>
                            </div>
                        </div>
                        <div id="list_comment">
                            <div class="comment_article" v-for="(comment,index) in full_article.comment" :key="comment.di">
                                <div class="avatar_comment">
                                    <img :src="process_url(comment.avatar)" alt="Avatar" v-if="comment.avatar != null" />
                                    <img src='../../assets/avatar.png' alt="Avatar" v-if="comment.avatar == null"> 
                                </div>
                                <div class="main_infor_comment" v-if="!editingComment || editingComment.id !== comment.id">
                                <div class="infor_comment">
                                    <div class="infor_left">
                                        <p class="author" v-if="full_article.user.id == comment.id_user"><i class="fa-solid fa-at"></i> Author</p>
                                        <p class="infor_fullname_comment" @click="goInforAccount(comment.id_user)">{{ comment.fullname }}</p>
                                        <p class="comment_content infor_created_comment">{{ comment.content }}</p>
                                    </div>
                                </div>
                                <div class="setting_cmt" v-if="user">
                                    <button class="btn_setting_cmt" @click="showSetting(index)"><i class="fa-solid fa-ellipsis" ></i></button>
                                    <div class="show_setting_cmt" v-if="show_setting_cmt[index]">
                                    <li class="li_edit" v-if="user.id == comment.id_user" @click="showEditModal(comment)"><span class="setting_icon"><i class="fa-solid fa-pen-to-square"></i></span> <span>Edit Comment</span></li>
                                    <li class="li_delete" v-if="user.id == comment.id_user" @click="deleteComment(index)" ><span class="setting_icon"><i class="fa-solid fa-trash"></i></span> <span>Delete Comment</span></li>
                                    <li class="li_report" v-if="user.id != comment.id_user" @click="reportComment()" ><span class="setting_icon"><i class="fa-solid fa-flag"></i></span> <span>Report Comment</span></li>
                                    </div>
                                </div>
                                </div>
                                <div v-else>
                                <div class="infor_comment">
                                    <div class="infor_left">
                                        <p class="author" v-if="full_article.user.id == comment.id_user"><i class="fa-solid fa-at"></i> Author</p>
                                        <p class="infor_fullname_comment">{{ comment.fullname }}</p>
                                        <textarea class="edit_content" v-model="editingComment.content"></textarea>
                                        <button class="btn_save" @click="saveComment()"><i class="fa-solid fa-check"></i> Save</button>
                                        <button class="btn_cancel" @click="cancelEdit()"><i class="fa-solid fa-xmark"></i> Cancel</button>
                                    </div>
                                </div>
                                </div>
                            </div>
                        </div>
                        <div id="add_comment" v-if="user">
                            <div class="header_comment ">
                                <div class="avatar_article">
                                    <img :src="user.avatar" alt="Avatar" v-if="user.avatar != null" />
                                    <img src='../../assets/avatar.png' alt="Avatar" v-if="user.avatar == null"> 
                                </div>
                                <div class="send_content_comment">
                                    <div >
                                        <div class="input-group">
                                        <form @submit.prevent="addCmt">
                                            <textarea @keydown.enter.prevent="handleEnter" style="background-color: #F0F2F5;" v-model="addComment.content" type="text" class="form-control input_content" id="inlineFormInputGroup" placeholder="Write a comment..."></textarea>
                                            <button type="submit" class="input-group-prepend" ></button>
                                            <p style="font-size: 12px;padding-left: 6px;color: #515151;margin-top: 2px;">Tip : Press the key combination <span style="font-weight: bold;"><i class="fa-brands fa-windows"></i> + .</span> for more icons . For Mac OS, press <span style="font-weight: bold;">Command + Control + Space</span> .</p>
                                        </form>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                <div >
                </div>
                <br>
                <!-- <Notification></Notification> -->
                </div>
            </div>
            <!-- Model Delete Admin -->
            <div style="background-color: #3d3d3d99;" class="modal fade" id="exampleModalDelete" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog" role="document" >
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="exampleModalLabel">Warning</h5>
                            <button style="padding-right: 50px;padding-top: 30px;" type="button" class="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true" >&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                            <div class="alert alert-warning" role="alert">
                                Are you sure you want to delete this article ? <br>
                                This article will be permanently deleted from the system !
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button type="button" id="close_btn" class="btn btn-outline-secondary" data-dismiss="modal" @click="closeDelete" >Close</button>
                            <button type="button" class="btn btn-outline-danger" @click="deleteArticle"><i class="fa-solid fa-trash"></i> Delete</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div id="right" class="col-3 p-0"><DashboardRight></DashboardRight></div>
        <div id="toTop" @click="scrollToTop" v-if="showButton">
          <button >
            <i class="fa-solid fa-chevron-up"></i>
          </button>
        </div>
    </div>
</template>
<script>

import BaseRequest from '../../restful/user/core/BaseRequest';
import useEventBus from '../../composables/useEventBus';
// import Notification from './../Notification';
import config from '../../config.js';
// import Paginate from 'vuejs-paginate-next';

// import ParticleVue32 from "../particle/ParticleVue32.vue";
// import FilePicker from './FilePicker.vue';

import DashboardLeft from './DashboardLeft.vue'
import DashboardRight from './DashboardRight.vue'

export default {
    name : "ArticleDetails",
    components: {
        // Notification,
        DashboardLeft,
        DashboardRight,
    },
    data(){
        return{
            show_setting:false,
            show_setting_cmt:[],
            count_cmt:null,
            user:{
              id:null,
              email:null,
              date_of_birth:null,
              gender:null,
              fullname:null,
              avatar:null,
              access_token:null,
            },
            full_article:{
              user:{
                id:null,
                fullname:null,
                avatar:null
              },
              article:{
                id:null,
                title:null,
                content:null,
                created_at:null,
                updated_at:null
              },
              comment:[]
            },
            showModal: false,
            editingComment: null,
            addComment:{
              id_user:null,
              id_article:null,
              content:''
            },
            id_article_delete:null,
            showButton: true
        }
    },
    // props: ['full_article'],
    setup() {
      // setup() receives props as the first argument.
    },
    created(){
    },
    mounted(){
        window.addEventListener("scroll", this.handleScroll);
        // this.full_article = this.article; 
        // console.log(this.full_article);
        // click bất cứ thứ gì ngoài button show setting đều làm cho ẩn show setting đó 
        if (document.body.style.paddingLeft !== "0px") {
          document.body.style.paddingLeft = "0px";
        }

        this.user = JSON.parse(window.localStorage.getItem('user'));
        if(this.user){
          if(this.user.avatar) this.user.avatar = config.API_URL + this.user.avatar ;
        }

        var id_article = this.$route.params.id

        document.addEventListener('click', this.handleOutsideClick);
        BaseRequest.get('articles/'+id_article)
        .then( data => {
            this.full_article = data.results[0];
            window.document.title=this.full_article.article.title;
            // this.list_comment = article.comment;
            // this.count_cmt = this.list_comment.length;
            this.count_cmt = this.full_article.comment.length;
            this.show_setting_cmt = new Array(this.count_cmt).fill(false);

            // add Comment 
            this.addComment.id_user = this.user.id;
            this.addComment.id_article = this.full_article.article.id;
        })
        .catch( () => {
          // Để chuyển đến component NotFound mà không thay đổi path hiện tại, bạn có thể sử dụng phương thức replace() thay vì push() như sau:
          // this.$router.push({ name: 'NotFound' }); 
          // this.$router.replace({ name: 'NotFound' });
        })
    },
    beforeUnmount() {
        // click bất cứ thứ gì ngoài button show setting đều làm cho ẩn show setting đó 
        document.removeEventListener('click', this.handleOutsideClick);
        // this.count_cmt = this.full_article.comment.length;
        // console.log(this.count_cmt);
        // this.show_setting_cmt = new Array(this.count_cmt).fill(false);
        var dashboard_user = document.getElementById("dashboard_user");
        dashboard_user.removeEventListener("scroll", this.handleScroll);
    },
    methods:{
      scrollToTop() {
        var dashboard_user = document.getElementById("dashboard_user");
        dashboard_user.scrollTo({
          top: 0,
          behavior: "smooth"
        });
      },
      handleScroll() {
        var dashboard_user = document.getElementById("dashboard_user");
        if (dashboard_user.pageYOffset > 10) {
          this.showButton = true;
        } else {
          this.showButton = false;
        }
      },
      // click bất cứ thứ gì ngoài button show setting đều làm cho ẩn show setting đó 
      handleOutsideClick(event) {
          if (!event.target.closest('button.btn_setting_cmt')) {
              this.show_setting_cmt = new Array(this.count_cmt).fill(false);
          }

          if (!event.target.closest('button')) {
              this.show_setting = false;
          }
      },
      process_url(path){
          return config.API_URL + path.slice(1);
      },
      showSetting(index){
        if(this.show_setting_cmt[index] == true) this.show_setting_cmt[index] = false;
        else {
          this.show_setting_cmt = new Array(this.count_cmt).fill(false);
          this.show_setting_cmt[index] = true;
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

      // edit and delete Comment 
      showEditModal(comment) {
        this.editingComment = comment;
        this.showModal = true;
      },
      saveComment() {
        BaseRequest.patch('comments/'+this.editingComment.id,this.editingComment)
        .then( () => {
          this.showModal = false;
          this.editingComment = null;
          const { emitEvent } = useEventBus();
          emitEvent('eventSuccess','Edit Comment Success !');
        })
        .catch( () => {
          const { emitEvent } = useEventBus();
          emitEvent('eventError','Edit Comment Fail !');
        })
      },
      cancelEdit() {
        this.showModal = false;
        this.editingComment = null;
      },
      deleteComment(index) {
        BaseRequest.delete('comments/'+this.full_article.comment[index].id)
        .then( () => {
          this.full_article.comment.splice(index, 1);
          const { emitEvent } = useEventBus();
          emitEvent('eventSuccess','Delete Comment Success !');
          emitEvent('deleteCmt',this.full_article.article.id);
        })
        .catch( () => {
          const { emitEvent } = useEventBus();
          emitEvent('eventError','Delete Comment Fail !');
        })
      },

      // add Comment 
      // cho textarea chỉ được tự xuống dòng khi hết dòng, còn lại khi enter trên đó thì submit form như input 
      handleEnter(event) {
        if (!event.shiftKey) {
          event.preventDefault();
          this.addCmt();
        }
      },

      addCmt(){
        BaseRequest.post('comments',this.addComment)
        .then( data => {
          this.full_article.comment.push(data);
          const { emitEvent } = useEventBus();
          this.addComment.content = '';
          emitEvent('eventSuccess','Comment Success !');
          emitEvent('addCmt',data);
        })
        .catch( () => {
          const { emitEvent } = useEventBus();
          emitEvent('eventError','Comment Fail !');
        })
      },
      reportComment(){
        const { emitEvent } = useEventBus();
        emitEvent('eventSuccess','Report Comment Success !');
      },

      editArticle(id){
        this.$router.push({name:'ArticleEdit',params:{id:id}}); 
      },
      openModel(id){
        this.id_article_delete = id;
      },
      deleteArticle(){
        BaseRequest.delete('articles/'+this.id_article_delete+'/')
        .then( () => {
          var close_btn = window.document.getElementById('close_btn');
          close_btn.click();
          const { emitEvent } = useEventBus();
          emitEvent('eventSuccess','Delete Article Success !');
          this.$router.push({name:"DashboardMain"});
        })
        .catch( () => {
            const { emitEvent } = useEventBus();
            emitEvent('eventError','Delete Article Fail !');
        })
      },
      saveArticle(){
        const { emitEvent } = useEventBus();
        emitEvent('eventSuccess','Save Article Success !');
      },
      unfollowUser(){
        const { emitEvent } = useEventBus();
        emitEvent('eventSuccess','Unfollow User Success !');
      },
      reportArticle(){
        const { emitEvent } = useEventBus();
        emitEvent('eventSuccess','Report Article Success!');
      },
      goInforAccount(id){
        this.$router.push({name:'InforAccount',params:{id:id}});
      },
      goArticle(id){
        this.$router.push({name:'ArticleDetails',params:{id:id}});
      },
    },
    watch:{

    }
}
</script>
<style scoped>
#toTop {
  position: absolute;
  right: 20px;
  bottom: 20px;
  background-color: rgb(144, 220, 255);
  font-size: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: 5px solid white;
  cursor: pointer;
  transition: all 0.5s ease;
}
#toTop:hover {
  border: 5px solid white;
  border: 5px solid #0085FF;
  background-color: white;
}
#modal_article {
    /* background-color: red; */
}

/* Article */
#dashboard_user {
  /* border: 1px solid green; */
  padding: 8px;
  background-color: #F2F4F6;
  overflow: hidden;
  max-height: 100vh;
  overflow: hidden;
  overflow-y: scroll;
  /* padding-left: 25px; */
  /* padding-right: 25px; */
  /* margin-right: 15px; */
}
#dashboard_user::-webkit-scrollbar-track { 
  background: transparent !important;  
}
#dashboard_user::-webkit-scrollbar {
  display: none !important;
}
.big_article {
  background-color: white;
  border-radius: 10px;
  border: 1px solid silver;
  margin-bottom: 10px;
  padding: 10px;
}
.header_article {
  border-bottom: 1px solid rgb(219, 219, 219);
  display: flex;
  padding-bottom: 10px;
}
.header_comment {
  border-top: 1px solid rgb(219, 219, 219);
  display: flex;
  padding-top: 20px;
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
.infor_right,.setting_cmt {
  position: relative;
}
div.show_setting {
  padding: 10px;
  position: absolute;
  top: 36px;
  right: 0px;
  background-color: white;
  z-index: 3;
  width: max-content;
  /* border: 1px solid silver; */
  border-radius: 10px;
  /* box-shadow: #c7e2fc 0px 7px 29px 0px; */
  /* box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px; */
  box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;
  /* box-shadow: rgba(17, 17, 26, 0.05) 0px 1px 0px, rgba(17, 17, 26, 0.1) 0px 0px 8px; */
}
div.show_setting_cmt {
  padding: 10px;
  position: absolute;
  top: 36px;
  right: 0px;
  background-color: white;
  z-index: 3;
  width: 200px;
  /* border: 1px solid silver; */
  border-radius: 10px;
  /* box-shadow: #c7e2fc 0px 7px 29px 0px; */
  /* box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px; */
  box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;
  /* box-shadow: rgba(17, 17, 26, 0.05) 0px 1px 0px, rgba(17, 17, 26, 0.1) 0px 0px 8px; */
}
div.show_setting li,div.show_setting_cmt li {
  margin: 3px ;
  display: flex;
  align-items: center;
  cursor: pointer;
  padding: 5px 10px;
}
div.show_setting li:hover {
  /* color: #F84B2F; */
  background-color: #ebebeb;
  border-radius: 10px;
}

div.show_setting_cmt .li_edit:hover {
  color:#0085FF;
  background-color: #ebebeb;
  border-radius: 10px;
}

div.show_setting_cmt .li_delete:hover {
  color: #F84B2F;
  background-color: #ebebeb;
  border-radius: 10px;
}

div.show_setting_cmt .li_report:hover {
  color: #ff0000;
  background-color: #ebebeb;
  border-radius: 10px;
}

div.show_setting_cmt li .setting_icon{
  display: inline-block;
  width: 10%;
  align-items: center;
  text-align: center;
  margin-right: 16px;
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
.btn_setting,.btn_setting_cmt {
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
.btn_setting_cmt:hover {
  background-color: #F0F2F5;
}



/* content_main_article */
.content_main_article {
  padding-bottom: 10px;
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
  word-wrap: break-word;
  cursor: pointer;
}
.main_title:hover {
  color: #0085FF;
}

.main_center {
  display: flex;
  justify-content: center;
  margin-bottom: 10px;
}
.main_content {
  word-wrap: break-word;
}


/* list comment */
#list_comment {
  margin-top: 10px;
  padding: 10px 0px;
  /* border: 1px solid silver; */
  border-top: 1px solid rgb(219, 219, 219);
  margin-top: 10px;
  min-height: 180px;
}


.comment_article {
  /* border-bottom: 2px solid rgb(219, 219, 219); */
  display: flex;
  padding-top: 10px;
  padding-bottom: 10px;
}

.avatar_comment {
  min-width: fit-content;
}
.avatar_comment img {
  cursor: pointer;
  max-width: 120% !important;
  width: 35px;
  height: 35px;
  object-fit:cover;
  border-radius: 20px;
}


.main_infor_comment {
  display: flex;
}

.infor_comment {
  display: flex;
  align-items: center;
  /* height: 40px; */
  margin-left: 5px;
  width: -webkit-fill-available;
  border-radius: 20px;
  transition: all 0.5s ease;
  justify-content: space-between;
  background-color: #F0F2F5;
  padding: 6px 10px;
}

.infor_fullname_comment {
  font-weight: 600;
  font-size: 14px;
}
.infor_fullname_comment:hover {
  text-decoration: underline;
  cursor: pointer;
}
.infor_created_comment {
  font-size: 14px;
}

.author {
    font-size: 12px;
    color: #616161;
}

/* Edit or Delete Comment */
.setting_cmt {

}

.edit_content {
  border-radius: 5px;
  width: 42vw;
  display: block;
  height: 15vh;
}

.btn_save,.btn_cancel {
  padding: 0px 5px;
  border: 1px solid silver;
  border-radius: 5px;
  margin-top: 6px;
  margin-bottom: 6px;
  margin-right: 6px;
}
.btn_save:hover {
  /* background-color: rgb(237, 237, 237); */
  /* color: #009717; */
  background-color: #009717;
  color: white;
}
.btn_cancel:hover{
  /* background-color: rgb(237, 237, 237); */
  color: white;
  background-color:#F84B2F;
}
.comment_content {
  max-width: 50vw;
  word-wrap: break-word;
}

/* Send Comment */
.input_content {
  width: 42vw;
  margin-left: 6px;
  display: block;
  border-radius: 10px;
}
div.show_setting li:hover {
  background-color: #ebebeb;
  border-radius: 10px;
}
.li_edit:hover {
  color: #0085FF;
}
.li_delete:hover {
  color: #F84B2F;
}
.li_save:hover {
  color: #0dcc23;
}
.li_unfollow:hover {
  color: #bac100;
}
.li_report:hover {
  color: #ff0000;
}


</style>
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
        <div class="modal-dialog fix_width_modal" role="document">
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
            <!-- <div class="modal-footer"> -->
              <!-- <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button> -->
              <!-- <button type="button" class="btn btn-primary">Save changes</button> -->
            <!-- </div> -->
          </div>
        </div>
      </div>
      <!-- Model Post Aticle -->

      <!-- Article -->
      <div v-for="(article,index) in articles" :key="index" class="big_article">
        <div class="header_article">
          <div class="avatar_article" @click="goInforAccount(article.user.id)">
            <img :src="process_url(article.user.avatar)" alt="Avatar" v-if="article.user.avatar != null" />
            <img src='../../assets/avatar.png' alt="Avatar" v-if="article.user.avatar == null"> 
          </div>
          <div class="infor_article">
            <div class="infor_left">
              <p class="infor_fullname" @click="goInforAccount(article.user.id)">{{ article.user.fullname }}</p>
              <p class="infor_created" @click="goArticle(article.article.id)" >{{ process_date(article.article.created_at) }}</p>
            </div>
            <div class="infor_right" v-if="user">
              <button class="btn_setting" @click="showSetting(index)"><i class="fa-solid fa-ellipsis" ></i></button>
              <div class="show_setting" v-if="show_setting[index]">
                <li class="li_edit" v-if="user.id == article.article.id_user" @click="editArticle(article.article.id)"><span class="setting_icon"><i class="fa-solid fa-pen-nib"></i></span> <span>Edit Article</span></li>
                <li class="li_delete" v-if="user.id == article.article.id_user" @click="openModel(article.article.id);" data-toggle="modal" data-target="#exampleModalDelete"><span class="setting_icon"><i class="fa-solid fa-trash"></i></span> <span>Delete Article</span></li>
                <li class="li_save" @click="saveArticle" v-if="user.id != article.article.id_user"><span class="setting_icon"><i class="fa-solid fa-bookmark"></i></span> <span>Save Articlee</span></li>
                <li class="li_unfollow" @click="unfollowUser" v-if="user.id != article.article.id_user"><span class="setting_icon"><i class="fa-solid fa-user-xmark"></i></span> <span>Unfollow</span></li>
                <li class="li_report" @click="reportArticle" v-if="user.id != article.article.id_user"><span class="setting_icon"><i class="fa-solid fa-flag"></i></span> <span>Report Article</span></li>
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
              {{ article.comment.length }} Comments
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
      <div class="modal fade" id="modalArticleDetails" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog fix_width_modal" role="document">
          <div class="modal-content">
            <!-- <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel" style="font-weight: bold;color: #0076e5;font-size: 20px;"><i class="fa-solid fa-cannabis"></i> Details Article</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div> -->
            <div class="modal-body">
              <!-- <ModalArticle v-bind:full_article="this.article_detail"></ModalArticle> -->
              <ModalArticle :full_article="this.article_detail"></ModalArticle>
            </div>
            <!-- <div class="modal-footer"> -->
              <!-- <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button> -->
              <!-- <button type="button" class="btn btn-primary">Save changes</button> -->
            <!-- </div> -->
          </div>
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

        <div id="divpaginate">
          <paginate class="pag" id="nvm"
              :page-count="Math.ceil(this.quantity/10)"
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
      <div id="toTop">
        <button @click="scrollToTop" v-if="showButton">
          <i class="fa-solid fa-chevron-up"></i>
        </button>
      </div>
      <!-- <Notification></Notification> -->
    </div>
</template>
<script>

import BaseRequest from '../../restful/user/core/BaseRequest';
import useEventBus from '../../composables/useEventBus';
// import Notification from './../Notification';
import config from '../../config.js';
import Paginate from 'vuejs-paginate-next';

// import ParticleVue32 from "../particle/ParticleVue32.vue";
// import FilePicker from './FilePicker.vue';

import ModalPostArticle from './ModalPostArticle'
import ModalArticle from './ModalArticle'

export default {
    name : "DashboardUser",
    components: {
      // Notification,
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
        id_article_delete:null,
        showButton: true
      }
    },
    created(){

    },
    mounted(){
      this.user = JSON.parse(window.localStorage.getItem('user'));
      if(this.user){
        if(this.user.avatar) this.user.avatar = config.API_URL + this.user.avatar ;
      }
      BaseRequest.get('articles?page=1')
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

      // Reload the article
      const { onEvent } = useEventBus()
      onEvent('ReloadArticle',(val)=>{
        console.log(val);
        BaseRequest.get('articles?page='+this.pageN)
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
      })

      onEvent('addCmt',(comment)=>{
        for (let index = 0; index < this.articles.length; index++) {
          if(this.articles[index].article.id == comment.id_article){
            this.articles[index].comment.push(comment);
          }
        }
      })
      onEvent('deleteCmt',(id_article)=>{
        for (let index = 0; index < this.articles.length; index++) {
          if(this.articles[index].article.id == id_article){
            this.articles[index].comment.pop();
          }
        }
      })
      window.addEventListener("scroll", this.handleScroll);
    },
    
    beforeUnmount() {
      // click bất cứ thứ gì ngoài button show setting đều làm cho ẩn show setting đó 
      document.removeEventListener('click', this.handleOutsideClick);
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
      getArticles(pageNum){
        BaseRequest.get('articles?page='+pageNum)
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
      },

      clickCallback:function(pageNum){
        this.pageN = pageNum;
        this.getArticles(pageNum);
      },
      get_article_detail(article){
        this.article_detail = article;
        // console.log(this.article_detail);
        const { emitEvent } = useEventBus();
        emitEvent('ShowArticle',article.article.id);
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

          // không cần reload lại trang 
          BaseRequest.get('articles?page='+this.pageN)
          .then( data => {
            this.articles = data.results;
            this.quantity = data.count;
          })
          .catch( () => {
          })
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

      goArticle(id){
        this.$router.push({name:'ArticleDetails',params:{id:id}});
      },
      goInforAccount(id){
        this.$router.push({name:'InforAccount',params:{id:id}});
      }
    },
}
</script>
<style scoped>

#toTop {
  position: absolute;
  right: -300px;
  bottom: 60px;
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
  padding: 8px;
  background-color: #F2F4F6;
  overflow: hidden;
  overflow-y: scroll;
  height: 100vh;
  /* padding-left: 25px;
  padding-right: 25px; */
  /* margin: 0px 25px; */
  /* margin-left: 15px; */
}
#post_article {
  display: flex;
  padding: 10px;
  border-radius: 10px; 
  border: 1px solid silver;
  background-color: white;
  cursor: pointer;
  margin-bottom: 16px;
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
  margin-bottom: 16px;
  padding: 10px;
}
.header_article {
  /* border-bottom: 2px solid rgb(219, 219, 219); */
  border-bottom: 1px solid rgb(219, 219, 219);
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
  /* border: 1px solid silver; */
  border-radius: 10px;
  /* box-shadow: #c7e2fc 0px 7px 29px 0px; */
  /* box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px; */
  box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;
  /* box-shadow: rgba(17, 17, 26, 0.05) 0px 1px 0px, rgba(17, 17, 26, 0.1) 0px 0px 8px; */
}
div.show_setting li {
  margin: 3px ;
  display: flex;
  align-items: center;
  cursor: pointer;
  padding: 5px 10px;
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
  max-height: 500px;
  overflow: hidden;
  overflow-y: scroll;
  word-wrap: break-word;
}

/* footer */
.footer_article {
  margin-top: 10px;
  border-top: 1px solid rgb(219, 219, 219);
}

.footer_number_comment {
  display: flex;
  justify-content: end;
  padding: 10px;
  border-bottom: 1px solid rgb(219, 219, 219);
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
  max-width: 60% !important;
}







</style>
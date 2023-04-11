<template>
    <div id="modal_article" v-if="article">
        <div class="big_article">
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
                    <button class="btn_setting" @click="show_setting = !show_setting"><i class="fa-solid fa-ellipsis" ></i></button>
                        <div class="show_setting" v-if="show_setting">
                            <li @click="goto_edit(article.article.id)"><span class="setting_icon"><i class="fa-solid fa-pen-nib"></i></span> <span>Edit Article</span></li>
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
            <div id="list_comment">
                <div class="comment_article" v-for="(comment,index) in article.comment" :key="index">
                    <div class="avatar_comment">
                        <img :src="process_url(article.user.avatar)" alt="Avatar" v-if="article.user.avatar != null" />
                        <img src='../../assets/avatar.png' alt="Avatar" v-if="article.user.avatar == null"> 
                    </div>
                    <div class="infor_comment">
                        <div class="infor_left">
                            <!-- {{ article.user.id }} -->
                            <!-- {{ comment.id_user }} -->
                            <p class="author" v-if="article.user.id == comment.id_user"><i class="fa-solid fa-at"></i> Author</p>
                            <!-- <p class="infor_fullname_comment">{{ comment.fullname }}</p> -->
                            <p class="infor_fullname_comment">Nguyen Van Manh</p>
                            <p class="infor_created_comment">{{ comment.content }}</p>
                        </div>
                    </div>
                </div>

                <!-- <div v-for="(comment,index) in article.comment" :key="index">
                    {{ comment.id }}
                    {{ comment.id_article }}
                    {{ comment.id_user }}
                    {{ comment.content }}
                </div> -->
            </div>

            <div id="add_comment">
                <div class="header_article">
                    <div class="avatar_article">
                        <img :src="process_url(article.user.avatar)" alt="Avatar" v-if="article.user.avatar != null" />
                        <img src='../../assets/avatar.png' alt="Avatar" v-if="article.user.avatar == null"> 
                    </div>
                    <div class="send_content_comment">
                        <div >
                            <div class="input-group">
                                <input style="background-color: #F0F2F5;" type="text" class="form-control" id="inlineFormInputGroup" placeholder="Write a comment...">
                                <div class="input-group-prepend"><div class="input-group-text"><i class="fa-solid fa-paper-plane"></i></div></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>





                <div >
          <!-- <p> <br> article.article.id : {{ article.article.id }} </p> -->
          <!-- <p> <br> article.article.id_user : {{ article.article.id_user }} </p> -->
        </div>
        <br>
        <!-- <div >
          {{ article.user.id }}
          {{ article.user.fullname }}
          {{ article.user.avatar }}
        </div> -->
        <!-- <div v-for="(comment,index) in article.comment" :key="index">
            {{ comment.id }}
            {{ comment.id_article }}
            {{ comment.id_user }}
            {{ comment.content }}
        </div> -->
        <!-- <br>
        <br>
        <br>
        <br> -->
        <Notification></Notification>
    </div>
</template>
<script>

// import BaseRequest from '../../restful/user/core/BaseRequest';
// import useEventBus from '../../composables/useEventBus';
import Notification from './../Notification';
import config from '../../config.js';
// import Paginate from 'vuejs-paginate-next';

// import ParticleVue32 from "../particle/ParticleVue32.vue";
// import FilePicker from './FilePicker.vue';

export default {
    name : "ModalArticle",
    components: {
        Notification
    },
    data(){
        return{
            show_setting:false,
        }
    },
    props: ['article'],
    created(){

    },
    mounted(){
        console.log(this.article);
        // click bất cứ thứ gì ngoài button show setting đều làm cho ẩn show setting đó 
        document.addEventListener('click', this.handleOutsideClick);
    },
    beforeUnmount() {
        // click bất cứ thứ gì ngoài button show setting đều làm cho ẩn show setting đó 
        document.removeEventListener('click', this.handleOutsideClick);
    },
    methods:{
        // click bất cứ thứ gì ngoài button show setting đều làm cho ẩn show setting đó 
        handleOutsideClick(event) {
            if (!event.target.closest('button')) {
                this.show_setting = false;
            }
        },
        process_url(path){
            return config.API_URL + path.slice(1);
        },
        process_date(day){
            const dateString = day;
            const date = new Date(Date.parse(dateString));
            const month = date.toLocaleString('default', { month: 'short' });
            // const formattedDate = `${("0" + date.getDate()).slice(-2)} month, ${date.getFullYear()}`;
            const formattedDate = `${("0" + date.getDate()).slice(-2)} ${month}, ${date.getFullYear()}`;
            return formattedDate;
        },
    },
    watch:{

    }
}
</script>
<style scoped>
#modal_article {
    /* background-color: red; */
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


/* list comment */
#list_comment {
    margin-top: 10px;
    padding: 10px 0px;
    /* border: 1px solid silver; */
}


.comment_article {
  /* border-bottom: 2px solid rgb(219, 219, 219); */
  display: flex;
  padding-top: 10px;
  padding-bottom: 10px;
}

.avatar_comment img {
  cursor: pointer;
  max-width: 120% !important;
  width: 35px;
  height: 35px;
  object-fit:cover;
  border-radius: 20px;
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

/* Send Comment */



</style>
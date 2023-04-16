<template>
    <div id="dashboard_left">
        <div class="main_right col-12 d-flex pt-2 pb-2" >
            <div class="logo_blog" @click="goMain"><img :src="logo"/></div>
            <div class="form_search">
                <div class="input-group">
                    <input v-model="text_search" type="text" class="shadow-none form-control" id="text_search" placeholder="Search mame or title article">
                    <div class="input-group-prepend">
                        <div class="input-group-text" ><i class="fa-solid fa-magnifying-glass"></i></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row" id="list_search" v-if="text_search != ''">
            <div class="col-12 p-1" id="inner_search">
                <div class="item_user_article" v-for="(user_article,index) in user_articles" :key="index">
                    <div class="item_user" v-if="user_article.user" @click="goInforAccount(user_article.user.id)">
                        <img :src="(process_url(user_article.user.avatar))">
                        <span> {{ user_article.user.fullname }}</span>
                    </div>
                    <div class="item_article" v-if="user_article.aritcle" @click="goArticle(user_article.aritcle.id)">
                        <i class="fa-solid fa-blog" style="margin-right: 8px;"></i> {{ user_article.aritcle.title }} 
                    </div>
                </div>
                <div class="no_result" v-if="user_articles.length == 0"><i class="fa-solid fa-magnifying-glass"></i> No result</div>
            </div>
        </div>
    </div>
</template>
<script>

import BaseRequest from '../../restful/user/core/BaseRequest';
import config from '../../config.js';

export default {
    name : "DashboardLeft",
    components: {

    },
    data(){
        return{
            text_search:'',
            logo: require('@/assets/logo.png'),
            user_articles:[],
        }
    },
    created(){

    },
    mounted(){

    },
    methods:{
        goMain(){
            this.$router.push({name:"DashboardMain"});
        },
        process_url(path){
            return config.API_URL + path.slice(1);
        },
        goArticle(id){
            // this.$router.push({name:'ArticleDetails',params:{id:id}});
            window.location = window.location.origin + '/article/' + id;
        },
        goInforAccount(id){
            // this.$router.push({name:'InforAccount',params:{id:id}});
            window.location = window.location.origin + '/infor/' + id;
        }
    },
    watch:{
        text_search:function(){
            var inp = {
                text_search:this.text_search 
            };
            BaseRequest.post('search',inp)
            .then( (data) => {
                this.user_articles = data.results;
            })
            .catch( () => {
            })
        }
    }
}
</script>
<style scoped>
#dashboard_left {
    /* border: 1px solid red; */
    height: 100vh;
    background-color: #F2F4F6;
}

.input-group-text {
    border-top-right-radius:20px !important;
    border-bottom-right-radius:20px !important;
    background-color: white;
    border-left: none;
    padding-left: 5px !important;
    color: silver;
}
#text_search {
    border-top-left-radius:20px;
    border-bottom-left-radius:20px;
    border-right: none;
    outline: none !important;
    transition: all 0s ease;
    padding-right: 0px !important;
}
#text_search:focus {
    outline: none !important;
    border-color: #4c90f5 !important;
}
.input-group:focus-within .input-group-text {
  border-color: #4c90f5;
}
.main_right {
    align-items: center;
}
.logo_blog {
    width: 12%;
    cursor: pointer;
}
.logo_blog img{
    width: 100%;
    object-fit: cover;
}
.form_search {
    padding-left:10px;
    width: 88%;
}

#list_search {
    margin-left: 10px;
    margin-right: 5px;
    padding: 5px 10px;
    background-color: white;
    border:1px solid silver;
    border-radius: 10px;
}
#inner_search {
    max-height: 80vh;
    overflow: hidden;
    overflow-y: scroll;
}

/* item_user */
.item_user {
    display: flex;
    align-items: center;
    border-radius: 10px;
    padding: 5px 10px;
    cursor: pointer;
}
.item_user:hover {
    background-color: #e4e4e4;
}
.item_user img {
    height: 40px;
    width: 40px;
    object-fit: cover;
    border-radius: 20px;
    margin-right: 10px;
}
.item_user span {
    font-weight: bold;
}

/* item_article */
.item_article {
    align-items: center;
    border-radius: 10px;
    padding: 10px 10px;
    padding-top: 5px;
    cursor: pointer;
    font-weight: bold;
    padding-left: 60px;

    /* Sử dụng kỹ thuật clamp() để giới hạn chiều cao */
    /* height: clamp(0px, 30px, auto); */
    max-height: 55px;
    
    /* Ẩn dấu ba chấm ban đầu */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
    -webkit-line-clamp: 2; /* giới hạn số dòng */
    word-wrap: break-word;
    cursor: pointer;
}
.item_article:hover {
    background-color: #e4e4e4;
}

.no_result {
    display: flex;
    align-items: center;
    border-radius: 10px;
    padding: 5px 10px;
    justify-content: center;
    background-color: #e4e4e4;
    font-weight: bold;
}
.no_result i {
    margin-right: 10px;
}
</style>
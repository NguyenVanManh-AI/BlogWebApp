<template>
    <div id="dashboard_right" class="pl-2 pt-2 pr-2">
        <div class="row m-0 pl-3 pr-3 title-account" >
            <div class="col-10 d-flex align-items-center justify-content-end" style="cursor: pointer;"  @click="openModal = !openModal"  v-if="user">
                <h1 class="" style="font-size: 17px;font-weight: bold;">{{ user.fullname }}</h1>
            </div>
            <div style="cursor: pointer;" id="account" class="col-2 mr-0 d-flex align-items-end" @click="openModal = !openModal" v-if="user">
                <img :src="user.avatar" alt="Avatar" v-if="user.avatar != null" />
                <img src='../../assets/avatar.png' alt="Avatar" v-if="user.avatar == null"> 
            </div>
            <div v-if="user==null" id="login">
                <li @click="login"><span><i class="fa-solid fa-arrow-right-to-bracket"></i></span> Login </li>
            </div>
        </div>
        <div class="row m-0 p-2" :class="{ openModal: openModal, closeModal: !openModal }" >
            <div id="modal_account" class="col-12" >
                <li v-if="user" @click="goInforAccount(user.id)"><span><i class="fa-solid fa-user-check"></i></span> {{ user.fullname }} </li>
                <li @click="profile"><span><i class="fa-solid fa-gear"></i></span> Personal page </li>
                <li @click="helpSupport"><span><i class="fa-solid fa-question"></i></span> Help & Support </li>
                <li @click="comments"><span><i class="fa-solid fa-info"></i></span> Comments </li>
                <li @click="logout"><span><i class="fa-solid fa-arrow-right-from-bracket"></i></span> Log out </li>
            </div>
        </div>
    </div>
</template>
<script>

import config from '../../config.js';

export default {
    name : "DashboardRight",
    components: {

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
            openModal:false,
        }
    },
    created(){

    },
    mounted(){
        this.user = JSON.parse(window.localStorage.getItem('user'));
        if(this.user){
            if(this.user.avatar) this.user.avatar = config.API_URL + this.user.avatar ;
        }
    },
    methods:{
        login(){
            this.$router.push({name:'UserLogin'});
        },
        logout(){
            window.localStorage.clear();
            window.location = window.location.href;
        },
        profile(){
            this.$router.push({name:'UserProfile'});
        },
        goInforAccount(id){
            this.$router.push({name:'InforAccount',params:{id:id}});
        },
        helpSupport:function(){
            this.$router.push({name:'HelpSupport'});
        },
        comments:function(){
            this.$router.push({name:'UserComments'});
        },
    },
}
</script>
<style scoped>
#dashboard_right {
    background-color: #F2F4F6;
    height: 100vh;
}
#account img {
    cursor: pointer;
    max-width: 150% !important;
    width: 40px;
    height: 40px;
    object-fit:cover;
    border-radius: 20px;
}
.openModal {
    display: block;
}
.closeModal {
    display: none;
}
#modal_account {
    box-shadow: rgba(0, 0, 0, 0.15) 0px 15px 25px, rgba(0, 0, 0, 0.05) 0px 5px 10px;
    border-radius: 10px;
    padding: 10px 20px !important;
    background-color: white;
}
.title-account {
    border-radius: 10px;
    /* border-bottom: 1px solid silver; */
    background-color: white;
    border: 1px solid silver;
    height: 52px;
    display: flex;
    justify-content: end;
    align-items: center;
}
.title-account h1:hover {
    color: #0076e5;
}
.title-account div:nth-child(1):hover h1{
    color: #0076e5;
}

#modal_account li {
    width: 100%;
    padding: 6px;
    font-weight: bold;
    border: 1px solid silver;
    margin: 5px 0px;
    border-radius: 10px;
    padding-left: 25px;
    cursor: pointer;
}
#modal_account li:hover {
    background-color: rgb(234, 234, 234);
    color: #0076e5;
}
#modal_account li span {
    background-color: rgb(210, 210, 210);
    border-radius: 20px;
    display: inline-block;
    height: 30px;
    width: 30px;
    padding: 3px;
    text-align: center;
    align-items: center;
    margin-right: 10px;
}

#login {
    margin-left: auto;
}
#login li {
    width: 100%;
    font-weight: bold;
    border: 1px solid silver;
    /* margin: 5px 0px; */
    border-radius: 10px;
    cursor: pointer;
    height: 40px;
    display: flex;
    align-items: center;
    padding: 0px 16px;  
}
#login li:hover {
    background-color: rgb(234, 234, 234);
    color: #0076e5;
}
#login li span {
    background-color: rgb(210, 210, 210);
    border-radius: 20px;
    text-align: center;
    margin-right: 10px;
    width: 30px;
    text-align: center;
    height: 30px;
    display: list-item;
    line-height: 30px;
}


</style>
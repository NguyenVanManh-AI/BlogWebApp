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
        <div class="row pl-2 pr-3 pb-2" id="list_search">
            <div class="col-12">
                <li>
                    <img src="https://scontent.fsgn2-8.fna.fbcdn.net/v/t39.30808-6/338856899_181123218062404_3931839156424930272_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=PAV4XNO4wngAX_nOTx-&_nc_ht=scontent.fsgn2-8.fna&oh=00_AfDCl0lqy6BVKPq6Dr5jjk8M0kU_oXuk7RTg5pitfZbMBA&oe=64310B58"/>
                    <span>Nguyen Van Manh</span>
                </li>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name : "DashboardLeft",
    components: {

    },
    data(){
        return{
            text_search:'',
            logo: require('@/assets/logo.png')
        }
    },
    created(){

    },
    mounted(){

    },
    methods:{
        goMain(){
            this.$router.push({name:"DashboardMain"});
        }
    },
    watch:{
        text_search:function(){
            console.log(this.text_search);
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




</style>
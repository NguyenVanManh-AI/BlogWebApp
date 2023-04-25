<template>
    <div id="dashboard" class="row m-0">
        <div id="left" class="col-3 p-0"><DashboardLeft></DashboardLeft></div>
        <div id="user" class="col-6 p-0"><DashboardUser></DashboardUser></div>
        <div id="right" class="col-3 p-0"><DashboardRight></DashboardRight></div>
    </div>
</template>
<script>

import DashboardLeft from './DashboardLeft.vue'
import DashboardRight from './DashboardRight.vue'
import DashboardUser from './DashboardUser.vue'

export default {
    name : "DashboardMain",
    components: {
        DashboardLeft,
        DashboardRight,
        DashboardUser
    },
    data(){
        return{

        }
    },
    created(){

    },
    mounted(){
        window.document.title='Main - Blog App';
        if (document.body.style.paddingLeft !== "0px") {
            document.body.style.paddingLeft = "0px";
        }
    },
    methods:{
        
    },
}
</script>
<style scoped>
#user {
    background-color: #F2F4F6;
}
</style>
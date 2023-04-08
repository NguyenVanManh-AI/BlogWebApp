<template>
    <div>
        <SidebarMenuAkahon v-if="user"></SidebarMenuAkahon>
        <div id="view-user">
            <div id="view-user-min">
                <div id="content">
                    <router-view></router-view>
                </div>
            </div>
        </div>
    </div>
  </template>
<script>

import SidebarMenuAkahon from './Sidebar-menu-akahon.vue';
import useEventBus from '../../composables/useEventBus'

export default {
    name : "UserMain",
    components: {
        SidebarMenuAkahon
    },
    data(){
        return{
            user:null,
        }
    },
    created(){

    },
    mounted(){
        this.user = window.localStorage.getItem('user');
        const { onEvent } = useEventBus()
        onEvent('eventLogout',()=>{
            this.admin = null;
            this.$router.push({name:"UserLogin"});
            window.location = window.location.href;
        })
    },
    methods:{
        
    },
}
</script>
<style scoped>
#view-user {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: white;
}
#view-user-min {
    box-shadow: rgba(99, 127, 152, 0.48) 6px 2px 16px 0px, rgba(255, 255, 255, 0.8) -6px -2px 16px 0px;
    border-radius: 20px;
    height: 93vh;
    width: 96%;
    padding: 16px;
}
#content {
    width: 100%;
    height: 100%;
    overflow: hidden;
    overflow-y: scroll;
}
</style>
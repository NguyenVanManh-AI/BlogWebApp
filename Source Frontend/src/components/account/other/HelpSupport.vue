<template>
    <div id="helpSupport">
        <ParticleVue32></ParticleVue32>
        <div id="helpSupport_content">
            <h1 style="color: #0085FF;font-size: 24px;text-align: center;font-weight: bold;">Help Support</h1>
            <h1>User manual</h1>
            <li>Add,Edit,View All Article</li>
            <li>Comment Article</li>
            <li>Change Password</li>
            <li>Update Profile</li>
            <h1>About US</h1>
            <h1>Team members include</h1> email , phone , mssv 
            <li>01. Nguyễn Văn Mạnh</li>
            <li>02. Nguyễn Công Cường </li>
            <li>03. Phan Tiến Đạt</li>
        </div>
    </div>
</template>
<script>

import ParticleVue32 from "../../particle/ParticleVue32.vue";
export default {
    name : "HelpSupport",
    components: {
        ParticleVue32,
    },
    data(){
        return{
  
        }
    },
    created(){
  
    },
    mounted(){
  
    },
    methods:{
        
    },
}
</script>
<style scoped>
#helpSupport_content {
    background-color: white;
    width: 100%;
    height: 100%;
    position: relative;
    border-radius: 10px;
    height: 88vh;
    box-shadow: rgb(204, 219, 232) 3px 3px 6px 0px inset, rgb(204, 219, 232) -3px -3px 6px 1px inset;
    padding: 20px;
}
</style>
<template>
  <div>

    <h1 style="font-size:100px">{{error.status}}</h1>
    <h2>{{error.message}}</h2>
    <a href='https://blog-nvm.herokuapp.com'><button class="btn btn-outline-dark">HOME</button></a>
  </div>
</template>

<script>

export default {
    name : "CompError",
    data(){
        return{
            error:{
                message:'',
                status:null
            }
        }
    },
    mounted(){
        this.error = JSON.parse(window.localStorage.getItem('error'));
    },
    methods:{
        
    },
    components:{

    }

}
</script>

<style>

</style>
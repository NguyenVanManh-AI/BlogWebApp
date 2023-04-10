<template>
    <div id="modal_article" v-if="article">
                <div >
                    
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
        </div>
    </div>
</template>
<script>
export default {
    name : "ModalArticle",
    components: {

    },
    data(){
        return{

        }
    },
    props: ['article'],
    created(){

    },
    mounted(){

    },
    methods:{
        
    },
    watch:{

    }
}
</script>
<style scoped>
#modal_article {
    /* background-color: red; */
}

</style>
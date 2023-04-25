<template>
    <div id="add_article">
        <div class="d-flex justify-content-center mt-2 text-center" id="title_article" style="font-weight: bold;color: #0076e5;font-size: 26px;font-style: italic;"><h1><i class="fa-solid fa-feather"></i>  {{ article.title }}</h1></div>
        <div id="content_html"></div>
        <div class="dt1">
            <div>
                <button @click="editArticle" type="submit" class="mt-4 btn-pers" id="login_button" ><i class="fa-solid fa-pen-to-square"></i> Edit</button>
            </div>
        </div>
      <!-- <Notification></Notification> -->
    </div>
</template>
<script>

import BaseRequest from '../../../restful/user/core/BaseRequest';
import useEventBus from '../../../composables/useEventBus'
// import Notification from '../../Notification'
export default {
    name : "ArticleDetail",
    components: {
      // Notification
    },
    data(){
        return{
          article:{
            title:'',
            content:'',
            id_user:null
          },
          id_article:null
        }
    },
    created(){
  
    },
    setup() {
      
    },
    mounted(){
        // {path:'detail/:id',name:'ArticleDetail',component:ArticleDetail},
        this.id_article = this.$route.params.id
        this.article.id_user = JSON.parse(window.localStorage.getItem('user')).id;

        BaseRequest.get('articles/'+this.id_article+'/')
        .then( data => {
        this.article = data ;
          window.document.title=this.article.title;
            var content = window.document.getElementById('content_html');
            content.innerHTML = this.article.content; 
          const { emitEvent } = useEventBus();
          emitEvent('eventSuccess','View Article Success !');
        })
        .catch( () => {
          const { emitEvent } = useEventBus();
          emitEvent('eventError','View Article Fail !');
        })
    },
    methods:{
        editArticle(){
            this.$router.push({name:'ArticleEdit',params:{id:this.id_article}}); 
        },
    },
}
</script>
<style scoped>
#add_article {
  padding: 10px;
  min-height: -webkit-fill-available;
}
#content {
  margin-bottom: 100px;
}


#content_html {
    margin-top: 30px;
    padding: 20px;
    margin-bottom: 20px;
    border: 2px solid silver;
    border-radius: 20px;
}

/* btn add */
.btn-pers {
  bottom: 10%;
  position: absolute;
  right: -1%;
  padding: 1em 2.5em;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 2.5px;
  font-weight: 700;
  color: #0085FF;
  background-color: #fff;
  border: none;
  border-radius: 45px;
  box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease 0s;
  cursor: pointer;
  outline: none;
  transform: translateX(-50%);
  border: 2px solid #0085FF;
}

.btn-pers:hover {
  background-color: #0085FF;
  box-shadow: 0px 15px 20px rgba(46, 138, 229, 0.4);
  color: #fff;
  transform: translate(-50%, -7px);
  border: 2px solid white;
}

.btn-pers:active {
  transform: translate(-50%, -1px);
}


</style>
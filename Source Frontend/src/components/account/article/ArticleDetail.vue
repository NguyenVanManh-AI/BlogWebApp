<template>
    <div id="add_article">
        <div class="d-flex justify-content-center mt-2" style="font-weight: bold;color: #0076e5;font-size: 20px;"><h1><i class="fa-solid fa-feather"></i> {{id_article}}New Article</h1></div>
        <div style="margin-top: 30px;margin-bottom: 10px;color:gray;text-transform: uppercase;"><i class="fa-solid fa-paragraph"></i> Title</div>
        <div>
            {{ article.title }}
        </div>

        <div style="margin-top: 30px;margin-bottom: 10px;color:gray;text-transform: uppercase;"><i class="fa-solid fa-file-pen"></i> Content</div>
        <div id="content">
            {{ article.content }}
        </div>

        <div class="dt1">
            <div>
                <button @click="editArticle" type="submit" class="mt-4 btn-pers" id="login_button" ><i class="fa-solid fa-plus"></i> Edit</button>
            </div>
        </div>
      <Notification></Notification>
    </div>
</template>
<script>

import BaseRequest from '../../../restful/user/core/BaseRequest';
import useEventBus from '../../../composables/useEventBus'
import Notification from '../../Notification'
export default {
    name : "ArticleDetail",
    components: {
      Notification
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
  position: relative;
}
#content {
  margin-bottom: 100px;
}



/* btn add */
.btn-pers {
  bottom: 30px;
  position: absolute;
  left: 50%;
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
}

.btn-pers:hover {
  background-color: #0085FF;
  box-shadow: 0px 15px 20px rgba(46, 138, 229, 0.4);
  color: #fff;
  transform: translate(-50%, -7px);
}

.btn-pers:active {
  transform: translate(-50%, -1px);
}


</style>
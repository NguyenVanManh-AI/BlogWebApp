<template>
  <div id="all_article">
    <div class="d-flex justify-content-center mt-2 mb-3" style="font-weight: bold;color: #0076e5;font-size: 20px;"><h1><i class="fa-solid fa-bars"></i> All Article</h1></div>
    <div id="all">
      <table class="table table-bordered table-hover">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col"><i class="fa-solid fa-paragraph"></i> title</th>
            <th colspan="3" class="text-center"><i class="fa-solid fa-gears"></i> feature</th>
          </tr>
        </thead>
        <tbody v-for="(article,index) in articles" :key="index">
          <tr class="hover_title">
            <th scope="row"><span>{{ (pageN-1)*6+index+1 }}</span></th>
            <td style="cursor: pointer;" class="col-12 align-center" @click="viewArticle(article.article.id)">{{ article.article.title }}</td>
            <td><div class="btn_center"><button @click="viewArticle(article.article.id)"  type="button" class="btn btn-primary"><i class="fa-solid fa-eye"></i></button></div></td>
            <td><div class="btn_center"><button @click="editArticle(article.article.id)" type="button" class="btn btn-primary"><i class="fa-solid fa-pen-to-square"></i></button></div></td>
            <td><div class="btn_center"><button @click="openModel(article.article.id);"  data-toggle="modal" data-target="#exampleModalDelete" type="button" class="btn btn-danger"><i class="fa-solid fa-trash"></i></button></div></td>
          </tr>
        </tbody>
      </table>
      <div id="divpaginate">
        <paginate class="pag" id="nvm"
            :page-count="Math.ceil(this.quantity/6)"
            :page-range="3"
            :margin-pages="2"
            :click-handler="clickCallback"
            :initial-page="this.pageN"
            :prev-text="'Prev'"
            :next-text="'Next'"
            :container-class="'pagination'"
            :page-class="'page-item'">
        </paginate>
    </div>
    </div>

    <!-- Model Delete Admin -->
    <div style="background-color: #3d3d3d99;" class="modal fade" id="exampleModalDelete" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document" >
          <div class="modal-content">
              <div class="modal-header">
                  <h5 class="modal-title" id="exampleModalLabel">Warning</h5>
                  <button style="padding-right: 50px;padding-top: 30px;" type="button" class="close" data-dismiss="modal" aria-label="Close">
                      <span aria-hidden="true" >&times;</span>
                  </button>
              </div>
              <div class="modal-body">
                  <div class="alert alert-warning" role="alert">
                      Are you sure you want to delete this article ? <br>
                      This article will be permanently deleted from the system !
                  </div>
              </div>
              <div class="modal-footer">
                  <button type="button" id="close_btn" class="btn btn-outline-secondary" data-dismiss="modal" @click="closeDelete" >Close</button>
                  <button type="button" class="btn btn-outline-danger" @click="deleteArticle"><i class="fa-solid fa-trash"></i> Delete</button>
              </div>
          </div>
      </div>
    </div>
    <!-- <Notification></Notification> -->
  </div>
</template>
<script>

import BaseRequest from '../../../restful/user/core/BaseRequest';
import useEventBus from '../../../composables/useEventBus'
// import Notification from '../../Notification'
import Paginate from 'vuejs-paginate-next';

export default {
  name : "ArticleAll",
  components: {
    // Notification,
    paginate: Paginate,
  },
  data(){
      return{
        articles:null,
        quantity:null,
        id_user:null,
        pageN:1,
        id_article_delete:null,
      }
  },
  created(){

  },
  mounted(){
    window.document.title='All Articles - Blog App';
    this.id_user = JSON.parse(window.localStorage.getItem('user')).id;

    // BaseRequest.get('articles/?page=1&id_user='+this.id_user)
    BaseRequest.get('users/'+this.id_user+'/articles?page=1')
    .then( data => {
      this.articles = data.results;
      this.quantity = data.count;
      const { emitEvent } = useEventBus();
      emitEvent('eventSuccess','Get All Article Success !');
    })
    .catch( () => {
      const { emitEvent } = useEventBus();
      emitEvent('eventError','Get All Article Fail !');
    })
  },
  methods:{
    clickCallback:function(pageNum){
      this.pageN = pageNum;
      this.getArticles(pageNum);
    },
    getArticles(pageNum){
      // BaseRequest.get('articles/?page='+pageNum+'&id_user='+this.id_user)
      BaseRequest.get('users/'+this.id_user+'/articles?page='+pageNum)
      .then( data => {
        this.articles = data.results;
        this.quantity = data.count;
        const { emitEvent } = useEventBus();
        emitEvent('eventSuccess','Get All Article Success !');
      })
      .catch( () => {
        const { emitEvent } = useEventBus();
        emitEvent('eventError','Get All Article Fail !');
      })
    },
    viewArticle(id){
      this.$router.push({name:'ArticleDetail',params:{id:id}}); 
    },
    editArticle(id){
      this.$router.push({name:'ArticleEdit',params:{id:id}}); 
    },
    openModel(id){
      this.id_article_delete = id;
    },
    deleteArticle(){
      console.log(this.id_article_delete);
      BaseRequest.delete('articles/'+this.id_article_delete+'/')
      .then( () => {
          var close_btn = window.document.getElementById('close_btn');
          close_btn.click();
          const { emitEvent } = useEventBus();
          emitEvent('eventSuccess','Delete Article Success !');
          // tải lại resource mới mà không cần phải reload lại trang 
          this.getArticles(this.pageN);
      })
      .catch( () => {
          const { emitEvent } = useEventBus();
          emitEvent('eventError','Delete Article Fail !');
      })
    }
  },
}
</script>
<style scoped>

#all_article {
  min-height: -webkit-fill-available;
  position: relative;
}
#divpaginate {
  bottom: 30px;
  position: absolute;
  width: 100%;
  display: flex;
  justify-content: center;
}



.btn_center {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  width: 100%;height: 100%;
}
.table th {
  vertical-align: none !important;
}

.hover_title:hover {
  color: #0076e5 !important;
}
</style>
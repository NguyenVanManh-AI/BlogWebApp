<template>
    <div id="add_article">
      <form  @submit.prevent="save()">
        <div class="d-flex justify-content-center mt-2" style="font-weight: bold;color: #0076e5;font-size: 20px;"><h1><i class="fa-solid fa-paper-plane"></i> Update Article</h1></div>
        <div style="margin-top: 30px;margin-bottom: 10px;color:gray;text-transform: uppercase;"><i class="fa-solid fa-paragraph"></i> Title</div>
        <div>
            <input v-model="article.title" required placeholder="Title Article" type="text" class="form-control" >
        </div>

        <div style="margin-top: 30px;margin-bottom: 10px;color:gray;text-transform: uppercase;"><i class="fa-solid fa-file-pen"></i> Content</div>
        <p style="font-size: 12px;padding-left: 6px;color: #515151;margin-top: 2px;">Tip : Press the key combination <span style="font-weight: bold;"><i class="fa-brands fa-windows"></i> + .</span> for more icons . For Mac OS, press <span style="font-weight: bold;">Command + Control + Space</span> .</p>
        <div id="content">
            <quill-editor
                v-model:value="state.content"
                :options="state.editorOption"
                :disabled="state.disabled"
            />
        </div>

        <div class="dt1">
            <div>
                <button type="submit" class="mt-4 btn-pers" id="login_button" ><i class="fa-solid fa-floppy-disk"></i> Save</button>
            </div>
        </div>
      </form>
    <!-- <Notification></Notification> -->
    </div>
</template>
<script>
import BaseRequest from '../../../restful/user/core/BaseRequest';
import useEventBus from '../../../composables/useEventBus'
// import Notification from '../../Notification'
import { reactive } from "vue";
export default {
    name : "ArticleEdit",
    components: {
        // Notification
    },
    data(){
        return{
            article:{
                title:'',
                content:'',
            },
            id_article:null
        }
    },
    created(){
  
    },
    setup() {
      const state = reactive({
        content: "<p></p>",
        _content: "",
        editorOption: {
          placeholder: "Content Article",
          modules: {

          },
        },
        disabled: false,
      });
      return {
        state,
      };
    },
    mounted(){
        this.id_article = this.$route.params.id
        BaseRequest.get('articles/'+this.id_article+'/')
        .then( data => {
            this.article = data ;
            window.document.title=this.article.title;
            this.state.content = this.article.content;
            const { emitEvent } = useEventBus();
            emitEvent('eventSuccess','View Article Success !');
        })
        .catch( () => {
          const { emitEvent } = useEventBus();
          emitEvent('eventError','View Article Fail !');
        })
    },
    methods:{
        save(){
            this.article.content = this.state.content;
            BaseRequest.patch('articles/'+this.id_article+'/',this.article)
            .then( () => {
                const { emitEvent } = useEventBus();
                emitEvent('eventSuccess','Edit Article Success !');
            })
            .catch( () => {
                const { emitEvent } = useEventBus();
                emitEvent('eventError','Edit Article Fail !');
            })
        }
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
}

.btn-pers:active {
  transform: translate(-50%, -1px);
}


</style>
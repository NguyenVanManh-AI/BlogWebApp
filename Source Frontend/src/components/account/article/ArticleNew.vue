<template>
    <div id="add_article">
        <div><h1>New Article</h1></div>
        <div>Title Article</div>
        <div>
            <input type="text">
        </div>
        <div>Content</div>
        <div id="content">
            <quill-editor
                v-model:value="state.content"
                :options="state.editorOption"
                :disabled="state.disabled"
            />
        </div>
    </div>
</template>
<script>

import { reactive } from "vue";
export default {
    name : "ArticleNew",
    components: {
  
    },
    data(){
        return{
  
        }
    },
    created(){
  
    },
    setup() {
      const state = reactive({
        content: "<p></p>",
        _content: "",
        editorOption: {
          placeholder: "Content",
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
  
    },
    methods:{
        
    },
}
</script>
<style scoped>
#add_article {

}

</style>
<template>
    <div id="dashboard_user">
        <div v-for="comment in comments" :key="comment.id">
        <div v-if="!editingComment || editingComment.id !== comment.id">
            <p>{{ comment.content }}</p>
            <button @click="showEditModal(comment)">Edit</button>
            <button @click="deleteComment(comment)">Delete</button>
        </div>
        <div v-else>
            <h3>Edit comment</h3>
            <textarea v-model="editingComment.content"></textarea>
            <button @click="saveComment()">Save</button>
            <button @click="cancelEdit()">Cancel</button>
        </div>
        </div>
    </div>
</template>
<script>
export default {
    name : "DashboardUser",
    components: {

    },
    data(){
        return{
comments: [
        { id: 1, content: "Comment 1" },
        { id: 2, content: "Comment 2" },
        { id: 3, content: "Comment 3" },
      ],
      showModal: false,
      editingComment: null,
        }
    },
    created(){

    },
    mounted(){

    },
    methods:{
showEditModal(comment) {
      this.editingComment = comment;
      this.showModal = true;
    },
    saveComment() {
      // Save edited comment to the backend
      // ...
      this.showModal = false;
      this.editingComment = null;
    },
    cancelEdit() {
      this.showModal = false;
      this.editingComment = null;
    },
    deleteComment(comment) {
      // Delete comment from the backend
      // ...
      this.comments = this.comments.filter((c) => c.id !== comment.id);
    },
    },
}
</script>
<style scoped>
#dashboard_user {
    background-color: green;
}
</style>
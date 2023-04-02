import { createRouter, createWebHistory } from 'vue-router'


import Login from './../components/CompLogin'
import Register from './../components/CompRegister'
import Post from './../components/CompPost'
import PostEdit from './../components/CompPostEdit'
import DetailPost from './../components/DetailPost'
import MyPost from './../components/MyPosts'
import PostNew from './../components/CompPostNew'
import CompError from './../components/CompError'
import NotFound from './../components/NotFound'

const routes = [
    {path: '/login',component: Login,name:'Login'},    
    {path: '/register',component: Register,name:'Register'} ,
    {path: '',component: Post,name:'Post'}, 
    {path: '/my',component: MyPost,name:'MyPost'}, 
    {path: '/posts/:id',component: DetailPost,name:'DetailPost'}, 
    {path: '/post/edit',component: PostEdit,name:'PostEdit'}, 
    {path: '/post/new',component: PostNew,name:'PostNew'}, 
    {path: '/error',component: CompError,name:'CompError'}, 
    {path: '/:NotFound(.*)*',component: NotFound,name:'NotFound'}
    
];

const router = createRouter({
    history: createWebHistory(),
    routes: routes
})

router.beforeEach((to,from,next)=>{
    let excludePages = ['/login','/register'];
    let requiredlogin = !excludePages.includes(to.path);
    let user = localStorage.getItem('user');
    if(requiredlogin && !user){
        if(to.path != "/" && to.path.indexOf('/posts/')){
            next({name:'Login'});
            alert("Bạn chưa đăng nhập !");
        }
    }
    next();
})

export default router

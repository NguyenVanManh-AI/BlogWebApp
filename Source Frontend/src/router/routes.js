import { createRouter, createWebHistory } from 'vue-router'
// import useEventBus from '../composables/useEventBus'

import UserLogin from './../components/account/UserLogin'
import UserRegister from './../components/account/UserRegister'

import ArticleMain from './../components/article/ArticleMain'
import ArticleAll from './../components/article/ArticleAll'
import ArticleDetail from './../components/article/ArticleDetail'
import ArticleEdit from './../components/article/ArticleEdit'
import ArticleNew from './../components/article/ArticleNew'
import UserArticle from './../components/article/UserArticle'

import DashboardMain from './../components/dashboard/DashboardMain'
// import DashboardLeft from './../components/dashboard/DashboardLeft'
// import DashboardRight from './../components/dashboard/DashboardRight'
// import DashboardUser from './../components/dashboard/DashboardUser'

import CompError from './../components/CompError'
import NotFound from './../components/NotFound'

const routes = [
    {path: '/login',component: UserLogin,name:'UserLogin'},    
    {path: '/register',component: UserRegister,name:'UserRegister'} ,

    {
        path:'/article',
        name:'ArticleMain',
        component:ArticleMain,
        children : [
            {path:'all',name:'ArticleAll',component:ArticleAll},
            {path:'my-article',name:'UserArticle',component:UserArticle},
            {path:'detail/:id',name:'ArticleDetail',component:ArticleDetail},
            {path:'edit/:id',name:'ArticleEdit',component:ArticleEdit},
            {path:'add',name:'ArticleNew',component:ArticleNew},
        ]
    },
    {path: '/dashboard',component: DashboardMain,name:'DashboardMain'}, 

    {path: '/error',component: CompError,name:'CompError'}, 
    {path: '/:NotFound(.*)*',component: NotFound,name:'NotFound'}
    
];

const router = createRouter({
    history: createWebHistory(),
    routes: routes
})

router.beforeEach((to, from, next) => {
    const excludePages = ['/login', '/register', '/dashboard'];
    const requiresLogin = !excludePages.includes(to.path);
    const user = localStorage.getItem('user');
    
    if (requiresLogin && !user) {
      if (to.path !== '/' && !to.path.startsWith('/posts/')) {
        next({ name: 'Login' });
        alert('Bạn chưa đăng nhập!');
      } else {
        next(false); 
      }
    } else if (to.path === '/') {
      next({ name: 'DashboardMain' }); 
    } else {
        next(); 
    }
});

export default router

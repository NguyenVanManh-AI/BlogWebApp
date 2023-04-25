import { createRouter, createWebHistory } from 'vue-router'
// import useEventBus from '../composables/useEventBus'

import UserLogin from './../components/account/UserLogin'
import UserRegister from './../components/account/UserRegister'
import UserProfile from './../components/account/UserProfile'
import UserchangePassword from './../components/account/UserchangePassword'
import UserMain from './../components/account/UserMain' 

import ArticleAll from './../components/account/article/ArticleAll'
import ArticleDetail from './../components/account/article/ArticleDetail'
import ArticleEdit from './../components/account/article/ArticleEdit'
import ArticleNew from './../components/account/article/ArticleNew'

// other
import HelpSupport from './../components/account/other/HelpSupport'
import UserComments from './../components/account/other/UserComments'

import DashboardMain from './../components/dashboard/DashboardMain'
import ArticleDetails from './../components/dashboard/ArticleDetails'
import InforAccount from './../components/dashboard/InforAccount'
// import DashboardLeft from './../components/dashboard/DashboardLeft'
// import DashboardRight from './../components/dashboard/DashboardRight'
// import DashboardUser from './../components/dashboard/DashboardUser'

import CompError from './../components/CompError'
import NotFound from './../components/NotFound'

const routes = [
    {path: '/login',component: UserLogin,name:'UserLogin'},    
    {path: '/register',component: UserRegister,name:'UserRegister'} ,

    {
        path:'/account',
        name:'UserMain',
        component:UserMain,
        children : [
            {path:'profile',name:'UserProfile',component:UserProfile},
            {path:'change-password',name:'UserchangePassword',component:UserchangePassword},
            {path:'all',name:'ArticleAll',component:ArticleAll},
            {path:'add',name:'ArticleNew',component:ArticleNew},
            {path:'detail/:id',name:'ArticleDetail',component:ArticleDetail},
            {path:'edit/:id',name:'ArticleEdit',component:ArticleEdit},
            {path:'help-support',name:'HelpSupport',component:HelpSupport},
            {path:'comment',name:'UserComments',component:UserComments},
        ]
    },
    {path: '/main',component: DashboardMain,name:'DashboardMain'}, 
    {path: '/article/:id',component: ArticleDetails,name:'ArticleDetails'}, 
    {path: '/infor/:id',component: InforAccount,name:'InforAccount'}, 

    {path: '/error',component: CompError,name:'CompError'}, 
    {path: '/:NotFound(.*)*',component: NotFound,name:'NotFound'}
    
];

const router = createRouter({
    history: createWebHistory(),
    routes: routes
})

router.beforeEach((to, from, next) => {
  if(to.path.includes('/article')) next();
  if(to.path.includes('/infor')) next();
  const user = localStorage.getItem('user');
  const requiresAuth = !['/main', '/login', '/register'].includes(to.path);
  if (requiresAuth && !user) {
    next('/login');
  } else {
    next();
  }
});

// router.beforeEach((to, from, next) => {

//     if(to.path.includes('/main')) next(); 
//     if(to.path.includes('/article ')) next();
//     if(to.path.includes('/register ')) next();
//     if(to.path.includes('/login ')) next();
    
//     // const excludePages = ['/login', '/register', '/main'];
//     // const requiresLogin = !excludePages.includes(to.path);
//     // const user = localStorage.getItem('user');
    
//     // if (requiresLogin && !user) {
//     //   if(to.path.startsWith('/article/')){
//     //     next();
//     //   }
//     //   if(to.path.startsWith('/infor/')){
//     //     next();
//     //   }
//     //   // else if (to.path !== '/' && !to.path.startsWith('/posts/')) {
//     //   //   next({ name: 'Login' });
//     //   //   alert('Bạn chưa đăng nhập!');
//     //   // } else {
//     //   //   next(false); 
//     //   // }
//     //   // else {
//     //   //   next({ name: 'NotFound' }); 
//     //   // }
//     // } else if (to.path === '/') {
//     //   next({ name: 'DashboardMain' }); 
//     // } else {
//     //     next(); 
//     // }
// });

export default router

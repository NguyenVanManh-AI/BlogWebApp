<template>
  <div>
    <div>
      <router-view></router-view>
      <Notification></Notification>
    </div>
  </div>
</template>

<script>

import Notification from './components/Notification';
// chỉ cần để một lần Notification tại file App.vue là được , những component con khác chỉ việc gửi đi sự kiện là tự đọng có 
// Mặc khác nếu để Notification tại file App thì z-index của nó luôn nằm trên các cái khác mà không cần chỉnh 
// còn nếu chỉnh thì mình vào component Notification để chỉnh thôi cũng được 
export default {
  name: 'App',
  components:{
    Notification,
  },
  mounted() {
    if(window.location.pathname === '/' || window.location.pathname === ''){
      this.$router.push({name:"DashboardMain"});
    }
  //   const shortcutIcon = document.querySelector('link[rel="shortcut icon"]');
  //   if (shortcutIcon) {
  //     shortcutIcon.href = '/logo.png';
  //     document.head.appendChild(shortcutIcon);
  //   } else {
  //     const newShortcutIcon = document.createElement('link');
  //     newShortcutIcon.rel = 'shortcut icon';
  //     newShortcutIcon.href = '/logo.png';
  //     document.head.appendChild(newShortcutIcon);
  //   }
  },
}
</script>

<style>

/* @import url('https://fonts.googleapis.com/css?family=Exo:400,800');
* {
  font-family: 'Exo', sans-serif;
} */
/*toàn bộ ô cuộn*/
/* ::-webkit-scrollbar { 
  width: 13px;
} */

/* ẩn thanh scroll */
::-webkit-scrollbar {
  display: none !important;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  list-style: none;
}

.modal-header button.close {
  padding-right: 50px;
  padding-top: 30px;
}
.modal.fade {
  background-color: #3d3d3d99;
}
a {
  text-decoration: none;
}
/* Track */
::-webkit-scrollbar-track { 
  background: white;  /*màu nền của ô cuộn */
}
/* Handle */
::-webkit-scrollbar-thumb { /*thanh cuộn nằm trong ô cuộn*/
    background: #888;  
    border-radius: 10px;
    border: 3px solid transparent; /*HAY*/
    background-clip: content-box;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover { /*thanh cuộn nằm trong ô cuộn khi hover vào */
    background: #0085FF; 
    /*background: #555; */
    border-radius: 10px;
    border: 3px solid transparent;
    background-clip: content-box;
}


/* Ẩn thanh cuộn cho phần tử */
#dashboard_user::-webkit-scrollbar {
  display: block !important;
  width: 12px !important;
  cursor: pointer !important;
}
#dashboard_user::-webkit-scrollbar-track { 
  background: transparent !important;  
}
/* Hiển thị thanh cuộn khi hover vào */
/* #dashboard_user:hover::-webkit-scrollbar {
  display: block !important;
  width: 12px !important;
  cursor: pointer !important;
} */

/* Thiết lập các thuộc tính cho thanh cuộn */
#dashboard_user::-webkit-scrollbar-thumb:hover {
  background-color: #0085FF;
  border-radius: 10px;
  border: 3px solid transparent;
  background-clip: content-box;
}

#dashboard_user::-webkit-scrollbar-thumb {
  background-color: #888;
  border-radius: 10px;
  border: 3px solid transparent;
  background-clip: content-box;
}

.max {
  /* height: 526px; */
  height: 495px;
}
.min {
  /* height: 490px; */
  height: 459px;
}
#view{
  display: grid;
  width: 100%;
  overflow-y: scroll;
}
#view::-webkit-scrollbar {
    display: none;
}
/* Hide scrollbar for IE, Edge and Firefox */
#view {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}
</style>

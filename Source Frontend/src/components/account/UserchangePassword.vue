<template>
    <div id="profile" >
        <ParticleVue32></ParticleVue32>
        <img v-if="user.url_img != null" :src="url_img">
        <div id="details" class="col-12">
            <form class="col-12 p-0" @submit.prevent="changeforpw" >
                <div class="row" >
                    <div class="col-12">
                        <div style="margin-top: 30px;margin-bottom: 20px;color:gray"><i class="fa-solid fa-repeat"></i> CHANGE PASSWORD</div>
                    </div>
                </div>
                <div class="form-group row" v-if="status">
                  <label  class="col-sm-5 col-form-label"><i class="fa-solid fa-key"></i> Current Password</label>
                  <div class="col-sm-7 show-pw"> 
                    <!-- chú ý là input có thể chỉnh padding được style="padding-right:40px"
                    ứng dụng trong việc cho thêm cái gì đó ví dụ show hide password chẳng hạn -->
                    <input required minlength="6" :type="typeInput" v-model="changepw.current_password" class="form-control"  placeholder="Current Password">
                  </div>
                </div>
                <div class="form-group row" >
                  <label  class="col-sm-5 col-form-label"><i class="fa-solid fa-key"></i> New Password</label>
                  <div class="col-sm-7">
                    <input required minlength="6" :type="typeInput" v-model="changepw.new_password"  class="form-control"  placeholder="New Password">
                  </div>
                </div>
                <div class="form-group row">
                  <label class="col-sm-5 col-form-label"><i class="fa-solid fa-key"></i> Confrim New Password</label>
                  <div class="col-sm-7">
                    <input required minlength="6" :type="typeInput" v-model="changepw.new_password_confirmation"  class="form-control"  placeholder="Confrim New Password">
                  </div>
                </div>
                <div class="form-group row" style="display:flex;align-content:center;align-items:center;line-height: 100%;margin-bottom:0px">
                  <div class="col-5" >
                  </div>
                  <div class="col-7" >
                    <label>Show All</label> <input v-model="checked" @change="showPw" type="checkbox">
                  </div>
                </div>
                <div class="dt1">
                    <div>
                        <button type="submit" class="mt-4 btn-pers" id="login_button" >Change Password</button>
                    </div>
                </div>
            </form>
        </div>
  
        <div id="message">
            <!-- <Notification></Notification> -->
        </div>
  
    </div>
  </template>
  
  
  <script scoped>
  
  import BaseRequest from '../../restful/user/core/BaseRequest';
  import useEventBus from '../../composables/useEventBus';
  // import Notification from '../Notification';
  // import config from '../../config.js';
  
  import ParticleVue32 from "../particle/ParticleVue32.vue";
  
  export default {
    name : "UserchangePassword",
    components: {
      // Notification,
      ParticleVue32,
    },
    data(){
        return{
            changepw:{
                // id:1,
                current_password:'',
                new_password:'',
                new_password_confirmation:'',
            },
            checked:false,
            typeInput:"password",
            user:{
                id:null,
                fullname:'',
                username:'',
                email: '',
                phone: '',
                google_id:null,
                date_of_birth:null,
                url_img:null,
                gender:null,
                address:'',
                status:null,
                access_token:'',
                refreshToken:'',
                created_at:null,
                updated_at:null,
                email_verified_at:null,
            },
            url_img:'',
            status:true,
        }
    },
    setup(){
      document.title = "Blog App - Change Password";
    },
    created(){
        // document.title = "Meta Shop - Admin Profile";
        document.title = "Blog App - Change Password";
    },// ta sẽ có created sẽ chạy sau setup() , setup chạy trước 
    computed(){
  
    },
    mounted(){
      window.document.title='Change Password';
    },
    methods:{
        showPw:function(){
          if(this.checked == false) this.typeInput = "password";
          else this.typeInput = "text";
        },
        changeforpw(){
          // console.log(this.changepw);
          if(this.changepw.new_password != this.changepw.new_password_confirmation){
              const { emitEvent } = useEventBus();
              emitEvent('eventError','New password does not match !');
              return 0;
          }
          else {
            var changepw2 = {
              password : this.changepw.new_password,
              oldpassword : this.changepw.current_password
            }
            console.log(changepw2);
            BaseRequest.patch('users/3/changepassword',changepw2)
            .then( () =>{
                this.changepw.current_password='';
                this.changepw.new_password='';
                this.changepw.new_password_confirmation='';
                this.checked = false;
                const { emitEvent } = useEventBus();
                emitEvent('eventSuccess','Change For Password Success !');
            }) 
            .catch(()=>{
                const { emitEvent } = useEventBus();
                emitEvent('eventError','Change For Password Fail !');
            })
          }
        },
    }
  }
  </script>
  <style scoped>
  *{
    transition: all 1s ease;
  }
  #profile{
    position: relative;
    /* background-color: #F2F4F6; */
    padding: 40px 140px;
    padding-bottom: 30px;
    /* height: 800px; */
    min-width: 100%;
  }
  
  /* details */
  #details{
    width: 100%;
    background-color: #000;
    box-shadow: rgb(204, 219, 232) 3px 3px 6px 0px inset, rgb(204, 219, 232) -3px -3px 6px 1px inset;
    padding: 10px 40px;
    padding-bottom: 20px;
    border-radius: 10px;
    position: relative;
    background-color: white;
    background-color: rgba(255, 255, 255, 0.545);
    font-weight: bold;
  }
  #profile > img {
    position: absolute;
    right: 0px;
    top: 0px;
    opacity: 0.9;
    min-width: 100%;
    max-height: 100%;
    object-fit: cover;
    filter: blur(8px);
    -webkit-filter: blur(8px);
  }
  #details input{
    background-color: rgba(255, 255, 255, 0.605); 
    color: #0085FF;
    font-weight: bold;
    font-style: italic;
  }
  #details label {
    color: #0085FF;
    font-style: italic;
  }
  
  /* btn login */
  .btn-pers {
  position: relative;
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
  
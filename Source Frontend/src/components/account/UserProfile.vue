<template>
    <div id="profile" >
        <ParticleVue32></ParticleVue32>
        <img v-if="user.url_img != null" :src="url_img">
        <!-- bind style này hoặc động tốt chỉ là tìm cách khác để style thêm opacity -->
        <!-- <div id="details" :style="[ user.url_img != null ? {'background-image': 'url(' + url_img + ')'} : { 'background-color': 'white' }]"> -->
        <div id="details" class="col-12">
            <form class="col-12 p-0" @submit.prevent="saveInfor">
                <div class="row" >
                    <div class="col-9">
                        <div style="color:gray"><i class="fa-solid fa-pen-to-square"></i> Edit Profile</div>
                        <div style="margin-top: 30px;margin-bottom: 20px;color:gray"><i class="fa-solid fa-user"></i> USER INFORMATION</div>
                        <label><i class="fa-solid fa-user-check"></i> Full Name</label><input v-model="user.fullname" placeholder="Full Name" type="text" class="form-control" >
                    </div>
                    <div class="col-3 mt-10" >
                        <div >
                            <FilePicker></FilePicker>
                        </div>
                        <!-- <label><i class="fa-solid fa-image"></i> Avatar</label><input @change="handleOnchange" type="file" class="form-control" > -->
                    </div>
                </div>
                <div class="row">
                    <div class="col-6"><label><i class="fa-solid fa-cake-candles"></i> Date of birth</label><input v-model="user.date_of_birth" type="date" format="YYYY MM DD" class="form-control" ></div>
                    <div class="col-6">
                        <label><i class="fa-solid fa-venus-mars"></i> Gender</label>
                        <div style="border:1px solid #ced4da;padding:4px;border-radius:0.25rem;display:flex;height: 38px;background-color: rgba(255, 255, 255, 0.605);">
                            <div class="form-check form-check-inline">
                                <input v-model="user.gender" class="form-check-input" type="radio" name="inlineRadioOptions" id="male" value="1">
                                <label style="color: #0085FF;" class="form-check-label" for="inlineRadio1">Men</label>
                            </div>
                            <div class="form-check form-check-inline">
                                <input v-model="user.gender" class="form-check-input" type="radio" name="inlineRadioOptions" id="female" value="0">
                                <label style="color: #0085FF;" class="form-check-label" for="inlineRadio2">Women</label>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="title-big" style="margin-top: 30px;margin-bottom: 20px;color:gray"><i class="fa-solid fa-mobile-screen-button"></i> CONTACT INFORMATION</div>
                <div class="row">
                    <div class="col-12"><label><i class="fa-solid fa-envelope"></i> Email</label><input v-model="user.email" placeholder="Email" type="email" class="form-control" ></div>
                </div>
                <div class="dt1">
                    <div>
                        <button type="submit" class="mt-4 btn-pers" id="login_button" >Save</button>
                    </div>
                </div>
            </form>
        </div>

        <div id="message">
            <Notification></Notification>
        </div>

    </div>
</template>


<script scoped>

import BaseRequest from '../../restful/user/core/BaseRequest';
import useEventBus from '../../composables/useEventBus';
import Notification from './../Notification';
import config from '../../config.js';

import ParticleVue32 from "../particle/ParticleVue32.vue";
import FilePicker from './FilePicker.vue';

export default {
    name : "UserProfile",
    components: {
      Notification,
      ParticleVue32,
      FilePicker
    },
    created(){
        document.title = "Meta Shop - Profile"
    },
    data(){
        return{
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
            err:{
                fullname:[],
                email:[],
                username:[],
                address:[],
                date_of_birth:[],
                gender:[],
                phone:[]
            },
            url_img:''
        }
    },
    setup(){
      return {

      }
    },
    computed(){

    },
    mounted(){

        this.user = JSON.parse(window.localStorage.getItem('user'));
        if(this.user != null && this.user.url_img != null) this.url_img = config.API_URL + this.user.url_img;

    },
    methods:{
        saveInfor:function(){
            var iuser = JSON.stringify(this.user);
            var idCustomer = this.user.id;
            BaseRequest.patch('api/customer/update-profile',this.user)
            .then( () =>{
                window.localStorage.setItem('user',iuser);

                // gửi sự kiện để upload file 
                const { emitEvent } = useEventBus();
                emitEvent('eventUserUpfile',idCustomer);
                setTimeout(()=>{emitEvent('eventUserResetUpfile');}, 2000);

                emitEvent('eventUserSuccess','Edit Information Success !');

                window.localStorage.setItem('user',JSON.stringify(this.user));

                this.err = null;

                setTimeout(()=>{
                    window.location=window.location.href;
                }, 1500);

            }) 
            .catch(error=>{
                console.log(error);
                this.err = error.response.data;
                var error2 = this.err;

                if(error2.fullname) this.inError(error2.fullname);
                if(error2.email) this.inError(error2.email);
                if(error2.username) this.inError(error2.username);
                if(error2.address) this.inError(error2.address);
                if(error2.date_of_birth) this.inError(error2.date_of_birth);
                if(error2.gender) this.inError(error2.gender);
                if(error2.phone) this.inError(error2.phone);
                // this.err = error.reponse.status;
            })
        },
        inError:function(er){
            const { emitEvent } = useEventBus();
            for(var i=0;i<er.length;i++) emitEvent('eventUserError',er[i]);
        },
    }
}
</script>

<style scoped>
* {
    transition: all 1s ease;
}
#profile{
    position: relative;
    background-color: #F2F4F6;
    padding: 0px 100px;
    padding-bottom: 30px;
    /* height: 800px; */
    min-width: 100%;
}

/* details */
#details{
    width: 100%;
    background-color: #000;
    /* box-shadow: 0px 10px 10px -10px gray; */
    box-shadow: rgb(204, 219, 232) 3px 3px 6px 0px inset, rgb(204, 219, 232) -3px -3px 6px 1px inset;
    /* box-shadow: rgba(50, 50, 93, 0.25) 0px 30px 60px -12px, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px; */
    padding: 30px 40px;
    border-radius: 10px;
    position: relative;
    background-color: white;
    background-color: rgba(255, 255, 255, 0.545);
    /* chọn white sau đó kéo thanh dọc xuống là có màu này */
    font-weight: bold;
    /* background-color: #F84B2F;  */
    /* Fallback color */
    /* background-color: #f84a2f49; */
    /* Black w/opacity/see-through */
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
    /* background-color: transparent; */
    font-weight: bold;
    /* border: black; */
}
#details label {
    color: #F84B2F;
}

/* #details label{
    font-weight: bold;
    font-size: 16px;
    background-color: rgba(255, 255, 255, 0.359);
    color: black;
    padding-left: 3px;
    padding-right: 3px;
    border-radius:3px ;
} */
/* .dt1 input {
    color: #0085FF;
}
.dt1 {
    display: flex;
    margin-bottom: 20px;
}
.dt1 > div {
    margin-right: 30px;
}
#sm {
    display: flex;
    justify-content: flex-start
} */

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

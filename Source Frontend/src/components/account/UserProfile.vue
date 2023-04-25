<template>
    <div id="profile" >
        <ParticleVue32></ParticleVue32>
        <img v-if="user.avatar != null" :src="url_img">
        <!-- bind style này hoặc động tốt chỉ là tìm cách khác để style thêm opacity -->
        <!-- <div id="details" :style="[ user.url_img != null ? {'background-image': 'url(' + url_img + ')'} : { 'background-color': 'white' }]"> -->
        <div id="details" class="col-12">
            <form class="col-12 p-0" @submit.prevent="saveInfor">
                <div class="row" >
                    <div class="col-9">
                        <div style="color:gray"><i class="fa-solid fa-pen-to-square"></i> Edit Profile</div>
                        <div style="margin-top: 30px;margin-bottom: 20px;color:gray"><i class="fa-solid fa-user"></i> USER INFORMATION</div>
                        <label><i class="fa-solid fa-user-check"></i> Full Name</label><input v-model="user.fullname" required placeholder="Full Name" type="text" class="form-control" >
                    </div>
                    <div class="col-3 mt-10" >
                        <div >
                            <FilePicker></FilePicker>
                        </div>
                        <!-- <label><i class="fa-solid fa-image"></i> Avatar</label><input @change="handleOnchange" type="file" class="form-control" > -->
                    </div>
                </div>
                <div class="row">
                    <div class="col-6"><label><i class="fa-solid fa-cake-candles"></i> Date of birth</label><input required v-model="user.date_of_birth" type="date" format="YYYY MM DD" class="form-control" ></div>
                    <div class="col-6">
                        <label><i class="fa-solid fa-venus-mars"></i> Gender</label>
                        <div style="border:1px solid #ced4da;padding:4px;border-radius:0.25rem;display:flex;height: 38px;background-color: rgba(255, 255, 255, 0.605);">
                            <div class="form-check form-check-inline">
                                <input required v-model="user.gender" class="form-check-input" type="radio" name="inlineRadioOptions" id="male" value="true">
                                <label style="color: #0085FF;" class="form-check-label" for="inlineRadio1">Men</label>
                            </div>
                            <div class="form-check form-check-inline">
                                <input required v-model="user.gender" class="form-check-input" type="radio" name="inlineRadioOptions" id="female" value="false">
                                <label style="color: #0085FF;" class="form-check-label" for="inlineRadio2">Women</label>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="title-big" style="margin-top: 30px;margin-bottom: 20px;color:gray"><i class="fa-solid fa-mobile-screen-button"></i> CONTACT INFORMATION</div>
                <div class="row">
                    <div class="col-12"><label><i class="fa-solid fa-envelope"></i> Email</label><input required v-model="user.email" placeholder="Email" type="email" class="form-control" ></div>
                </div>
                <div class="dt1">
                    <div>
                        <button type="submit" class="mt-4 btn-pers" id="login_button" ><i class="fa-solid fa-floppy-disk"></i> Save</button>
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

// import BaseRequest from '../../restful/user/core/BaseRequest';
import useEventBus from '../../composables/useEventBus';
// import Notification from './../Notification';
import config from '../../config.js';

import ParticleVue32 from "../particle/ParticleVue32.vue";
import FilePicker from './FilePicker.vue';

export default {
    name : "UserProfile",
    components: {
    //   Notification,
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
                email:null,
                date_of_birth:null,
                gender:null,
                fullname:null,
                avatar:null,
                access_token:null,
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
        if(this.user != null && this.user.avatar != null) this.url_img = config.API_URL + this.user.avatar;
        window.document.title=this.user.fullname + ' - Profile';
    },
    methods:{
        saveInfor:function(){

            const { emitEvent } = useEventBus();
            emitEvent('eventUserUpfile',this.user);
            setTimeout(()=>{emitEvent('eventUserResetUpfile');}, 2000);

        },
    }
}
</script>

<style scoped>
/* * {
    transition: all 1s ease;
} */
#profile{
    position: relative;
    background-color: #F2F4F6;
    padding: 0px 100px;
    padding-bottom: 20px;
    padding-top: 20px;
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
    max-height: 120%;
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

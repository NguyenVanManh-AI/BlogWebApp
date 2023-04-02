const axios = require('axios');
import config from '../config.js'
import router from './../router/routes' 

let dataUser = window.localStorage.getItem('user');
let user = null;
if(dataUser){
	user = JSON.parse(dataUser);
}

export default {
	_getHeaders(){
		let headers = {};
		if(user !== null){
			headers.Authorization = 'Bearer ' + user.accessToken;
		}
		return headers;
	},

	get(url){
		return new Promise( (resolve, reject) =>{ 
			axios.get(
				config.API_URL + '/' + url  , 
				{
					headers : this._getHeaders()
				}
			)
			.then( response =>{
				resolve(response.data);
			})
			.catch( error => {
				// if(error.response.status == 404){
				// 	window.location.href = '/401';
				// }
				// if(error.response.status == 404){
				// 	window.location.href = '/404';
				// }
				// if(error.response.status == 503){
				// 	window.location.href = '/503';
				// }
				let errors = {
					message : error.message,
					status : error.response.status
				}
				window.localStorage.setItem('error',JSON.stringify(errors));
				router.push({name:'CompError'});
				reject(error);
			})
		});
	},
	post(url,data){
		return new Promise( (resolve, reject) =>{
			axios.post(
				config.API_URL + '/' + url, 
				data,
				{
					headers : this._getHeaders()
				}
			)
			.then( response =>{
				resolve(response.data);
			})
			.catch( error => {
				let errors = {
					message : error.message,
					status : error.response.status
				}
				window.localStorage.setItem('error',JSON.stringify(errors));
				router.push({name:'CompError'});
				reject(error);
			})
		})
	},
	put(url,data){
		return new Promise( (resolve, reject) =>{
			axios.put(
				config.API_URL + '/' + url, 
				data,
				{
					headers : this._getHeaders()
				}
			)
			.then( response =>{
				resolve(response.data);
			})
			.catch( error => {
				let errors = {
					message : error.message,
					status : error.response.status
				}
				window.localStorage.setItem('error',JSON.stringify(errors));
				router.push({name:'CompError'});
				reject(error);
			})
		})
	},
	delete(url){
		return new Promise( (resolve, reject) =>{
			axios.delete(
				config.API_URL + '/' + url, 
				{
					headers : this._getHeaders()
				}
			)
			.then( response =>{
				resolve(response.data);
			})
			.catch( error => {
				let errors = {
					message : error.message,
					status : error.response.status
				}
				window.localStorage.setItem('error',JSON.stringify(errors));
				router.push({name:'CompError'});
				reject(error);
			})
		})
	}
}


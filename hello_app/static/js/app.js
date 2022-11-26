let form= document.getElementById("empform");
let empid=document.getElementById("empid");
let name=document.getElementById("name");
let address=document.getElementById("address");
let dob=document.getElementById("dob");
let mobile =document.getElementById("phone");

document.addEventListener("DOMContentLoaded",function(){
	form.addEventListener("submit",function(e){
		let idValue=empid.value;
		let nameValue=name.value;
		let addressValue=address.value;
		let dobValue=dob.value;
		let mobileValue=mobile.value;
		let x = validateForm(idValue,nameValue,addressValue,dobValue,mobileValue);
		if(x==false){ 
		e.preventDefault();
		}
	})

	function validateForm(id,name,address,dob,mobile){	
		val = true
		console.log(id+name+address+dob+mobile);
		if(mobile.length!=10){
			errorField("Contact Number should contain exactly 10 numbers")
			console.log("phone number error is there")
			val = false
		}
		
		if (name.length<5){
	        errorField("Employee Name is too short.\n Please enter Employee's full name.")
			console.log("Name error")
			val = false
		}

	    if (address.length < 10){
	        errorField("Employee's Address is too short.\n Please enter Employee's full address.")
			console.log("phone number error is there")
			val = false
		}
			return val;
	}

	function errorField(message){
		let div=document.createElement("div")
		div.classList.add("alert","alert-danger")
		div.innerHTML=`${message}`
		let cardBody=document.querySelector(".card-body")
		cardBody.insertBefore(div,form)

		setTimeout(function(){
			document.querySelector(".alert").remove()
		})
	}
})

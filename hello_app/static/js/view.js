let form= document.getElementById("empform");
let empid=document.getElementById("empid");

document.addEventListener("DOMContentLoaded",function(){
	form.addEventListener("submit",function(e){
		let idValue=empid.value;
		let x = validateForm(idValue);
		if(x==false){ 
		e.preventDefault();
		}
	})

	function validateForm(id){	
		val = true
		

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

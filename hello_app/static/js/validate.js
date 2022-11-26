function clearErrors(){

    errors = document.getElementsByClassName('formerror');
    for(let item of errors)
    {
        item.innerHTML = "";
    }


}
function seterror(id, error){
    //sets error inside tag of id 
    element = document.getElementById(id);
    element.getElementsByClassName('formerror').innerHTML = error;

}

function validateForm(){
    var returnval = false;
    clearErrors();

    //perform validation and if validation fails, set the value of returnval to false
    var name = document.forms['myForm']["name"].value;
    if (name.length<5){
        seterror("sname", "*Length of name is too short");
        returnval = false;
    }

    if (name.length == 0){
        seterror("sname", "*Length of name cannot be zero!");
        returnval = false;
    }


    var phone = document.forms['myForm']["phone"].value;
    if (phone.length != 10){
        seterror("sphone", "*Phone number should be of 10 digits!");
        returnval = false;
    }

    var address = document.forms['myForm']["address"].value;
    if (address.length < 10){
        seterror("saddress", "*Address too short!!!");
        returnval = false;
    }

    return returnval;
}


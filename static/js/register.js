$(document).ready(function(){
    $("#register").show();
    $("#otp").hide();
    $('select').material_select('destroy');
    $('select').material_select();
});


function FormValidate(){
    var name = $("#name").val();
    var username = $("#username").val();
    var mobile = $("#mobile").val();
    var gender = $("#gender").val()
    var password = $("#pass").val();

    var regexpname = /^[a-zA-Z ]+$/;
    var regexpmob = /^[0-9]{10}$/;              

    if(!regexpname.test(name)){
            Materialize.toast('Enter correct name', 4000);
    }
    if(!regexpmob.test(mobile)){
            Materialize.toast('Enter correct mobile number', 4000);
    }
    if(username==""){
            Materialize.toast('Enter a valid username', 4000);
    }
    if(gender=="Select gender"){
            Materialize.toast('Select a gender', 4000);
    }
    if(password==""){
            Materialize.toast('Enter a password', 4000);       
    }
    else{
        
        sendData = {
            'name': name,
            'username':username,
            'gender': gender,
            'mobile': mobile,
            'password' : password
        };

        localStorage.setItem("mobile", mobile);
        localStorage.setItem("name", name);
        localStorage.setItem("username", username);
        localStorage.setItem("gender", gender);
        localStorage.setItem("password", password);
        $.ajax({
            type: 'POST',
            url: '/home/register/',
            data: sendData,
            success: function(data){
                    $("#register").hide();
                    $("#otp").show();
            },
            error: function(){
                Materialize.toast('Sorry an error occured please try again later', 4000);
            }
        });

    }
}

function otpValidate(){
    var mobile = localStorage.getItem("mobile");
    var name = localStorage.getItem("name", name);
    var username = localStorage.getItem("username", username);
    var gender = localStorage.getItem("gender", gender);
    var password =localStorage.getItem("password", password);
    var otp = $("#otpValue").val();
    
    var regexpmob = /^[0-9]{10}$/;        
    var regexpotp = /^[0-9]{4}$/;

    if(!regexpmob.test(mobile)){
            Materialize.toast('Enter correct mobile number', 4000);
    }
    if(!regexpotp.test(otp)){
            Materialize.toast('Enter correct OTP', 4000);
    }
    else{
            sendData = {
                    "otp" : otp,
                    'name': name,
                    'username':username,
                    'gender': gender,
            'mobile': mobile,
            'password' : password
            }

            $.ajax({
            type: 'POST',
            url: '/otp/verify',
            data: sendData,
            success: function(data){

                    if(data.success == true){
                            Materialize.toast(data.message, 4000);
                            $("#register").show();
                            $("#otp").hide();
                    }
                    else{
                            Materialize.toast(data.message, 4000);
                    }
                    
                    
            },
            error: function(){
                Materialize.toast('Sorry an error occured please try again later', 4000);
            }
        });


    }
}
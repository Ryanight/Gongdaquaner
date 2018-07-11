$(document).ready(function(){
    $("#btn-login").click(function(){
        var useremail = $("#exampleInputEmail1").val();
        var userpassword = $("#exampleInputPassword1").val();
        alert("Email: " + useremail);
        // var data = {
        //     'email' : useremail,
        //     'password' : userpassword
        // }
        // data to send to server.
        $.ajax({url:"/js_call", data_temp: {'email':useremail, 'password':userpassword}, success:function(data){
                alert(data);
            }});
    });

    $(".after").click(function(){
        $("#btn-goMain").after("<a id=\"btn-goMain\" href=\"../main.html\" class=\"btn btn-success btn-block btn-block\">登录</a>");
    });

    // $("#btn-goMain").append(localStorage.getItem("a"));
    // $(".after").click( function(){
    //     localStorage.a="login2";
    //     $("#btn-goMain").after("<a id=\"btn-goMain\" href=\"main.html\" class=\"btn btn-success btn-block btn-block\">登录</a>");
    //     localStorage.a=$("#btn-goMain").html();
    // })
})


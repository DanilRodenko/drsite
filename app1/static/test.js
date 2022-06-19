
$(document).ready(function(){
    $('#id45').click(function(e) {
    alert("Тількі для зареєстрованих користувачів")
    })

//    Регистрация
    $("#sub_reg").click(function(e) {
        login=$("#check_login").val()

        if (login.length <=3) {
            alert("Login must be more than 3 symbols")
            e.preventDefault()
            }
    })
    $("#sub_reg").click(function(e) {
        email=$("#check_mail").val()
        if (email != email.match(/[\w\d\.\_]+@[\w]+.[\w]+/)) {
        alert("Incorrect mail")
        e.preventDefault()
}
    })
    $("#sub_reg").click(function(e) {
        password=$("#check_password").val()
        if (password.length <=3) {
            alert("Password must be more than 3 symbols")
            e.preventDefault()
        }
    })

    $("#test").click(function(e){
    $.post(
    'ajax_path',
    {},
    function(response) {
    alert(response.number)}
    )
    })

    $("#check_login").blur(function(e){
        $.post(
    'check_login',
    { "login" : $("#check_login").val()},
    function(response) {
    if (response.status == 'error') {
        alert('Login already taken')
    }})
    })

    $("#check_mail").blur(function(e){
        $.post(
    'check_mail',
    { "email" : $("#check_mail").val()},
    function(response) {
    if (response.status == 'error') {
        alert('Mail is already taken')
    }})
    })



    $("#sub_reg_ajax").click(function(e) {
    $.post(
    'register_2',
    {'login' : $("#check_login").val(),
    'first_name' : $("#first_name").val(),
    'email' : $("#check_mail").val(),
    'password' : $("#check_password").val()
    },
    function(response) {
    if (response.status == 'ok'){
    alert('Registration success')}
    })
    })
})


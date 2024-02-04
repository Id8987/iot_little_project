let btn1  = document.getElementById("btn1")
let btn2 = document.getElementById("btn2")

btn1.addEventListener('click', ()=>{
    btn1.disabled = true;
    btn2.disabled = false
    document.getElementsByClassName('header')[0].classList.add('light')
})
btn2.addEventListener('click', ()=>{
    btn2.disabled = true;
    btn1.disabled = false
    document.getElementsByClassName('header')[0].classList.remove('light')
})
// document.getElementById('submitBtn').addEventListener('click', function (e){
//     e.preventDefault()
// })
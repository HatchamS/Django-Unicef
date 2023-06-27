let checkCookie = document.cookie.indexOf("CookieContractSee=yes");
let cookieContrac=document.querySelector(".wrapper")
if (checkCookie != -1){
    cookieContrac.classList.remove("hide")
}

const cookieBox = document.querySelector(".popup-screen")
acceptBtn = document.getElementById("accept");
declinBtn=document.getElementById("refuse");

acceptBtn.addEventListener("click", SeeContract);
declinBtn.addEventListener("click", SeeContract);

function SeeContract(){
  
  document.cookie = "CookieContractSee=yes; max-age="+60*60*24*30+";SameSite=Lax";
  if(document.cookie){
    cookieContrac.classList.remove("hide");
  }else{ 
    alert("Cookie can't be set! Please unblock this site from the cookie setting of your browser.");
  }
}

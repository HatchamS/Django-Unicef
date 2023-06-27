function changeTextSwitch() {
  
    var checkBox = document.getElementById("switchButton");
    var text = document.getElementById("contentSwitch");
    var secretSection = document.getElementById("localisation");
    const EndSecretSection = document.getElementById("mapSecretSection");
  
    
    if (checkBox.checked == true){
      text.innerText = "Oui";
      text.style.left = "16%";
      text.style.color="white";
      secretSection.classList.replace("secret","commonParagraphe");
      EndSecretSection.scrollIntoView()
    } else {
      text.innerText = "?";
      text.style.left = "60%";
      text.style.color="black"
      secretSection.classList.replace("commonParagraphe","secret")
    }
}


    
            

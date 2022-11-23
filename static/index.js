const btnSwitch = document.querySelector('#switch');

const enlace = document.querySelector('#enlace');
const baseUrl = "https://bootswatch.com/5/darkly/bootstrap.css";
const Urlvacia = "";
btnSwitch.addEventListener('click', () => {
    btnSwitch.classList.toggle('active');
    if(btnSwitch.classList.contains('active')){
        var elemento = document.getElementById("enlace");
        elemento.href = baseUrl;
    }
    else{
        var elemento = document.getElementById("enlace");
        elemento.href = Urlvacia;
    }
   
    //document.body.classList.toggle('dark');
    //guardamos en local 
    if(btnSwitch.classList.contains('active')){
        localStorage.setItem('dark-mode', 'true');
    } else{
        localStorage.setItem('dark-mode', 'false');
    }

});

//comprobacion

if(localStorage.getItem('dark-mode') === 'true'){
    var elemento = document.getElementById("enlace");
    btnSwitch.classList.add('active');
    elemento.href = baseUrl;
} else{
    var elemento = document.getElementById("enlace");
    btnSwitch.classList.remove('active');
    elemento.href = Urlvacia;
}


//comprobacion

if(localStorage.getItem('dark-mode') === 'true'){
    document.body.classList.add('dark');
    navegacion.classList.toggle('navbar-dark border-bottom');
    btnSwitch.classList.add('active');
} else{
    document.body.classList.remove('dark');
    navegacion.classList.toggle('navbar-dark border-bottom');
    btnSwitch.classList.remove('active');
}
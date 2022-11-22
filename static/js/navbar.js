/* SHOW MENU */
const navMenu = document.getElementById('nav-menu'),
navToggle = document.getElementById('nav-toggle'),
navClose = document.getElementById('nav-close')


/* MENU SHOW */
if(navToggle) {
    navToggle.addEventListener("click", () => {
        navMenu.classList.add("show_menu")
    })
}

  
/* MENU HIDDEN */
if(navToggle) {
    navClose.addEventListener("click", () => {		
        navMenu.classList.remove("show_menu")
    }) 
}

  
/* REMOVE MENU MOBILE */
const navLink = document.querySelectorAll('.nav_link')

function linkAction() {
    const navMenu = document.getElementById('nav-menu')
    //when we click on each nav_link, we remove the show-menu close
    navMenu.classList.remove('show_menu')
}

navLink.forEach(n => n.addEventListener('click', linkAction))


/* Change background Header */
function scrollNavbar() {
    const navbar = document.getElementById("navbar")

    //wheen the scroll is greater than 40 viewport height, add the scroll haeder to the geader tag
    if(this.scrollY >= 50) navbar.classList.add("scroll_nav"); else navbar.classList.remove("scroll_nav")
}

window.addEventListener('scroll', scrollNavbar)
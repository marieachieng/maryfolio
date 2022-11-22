/* typing animation */
var typed = new Typed(".typing", {
    strings:["Web Designer", "Web Developer",],
    typeSpeed:100,
    BackSpeed:60,
    loop:true
});

/* About Tabs */
const tabs = document.querySelectorAll('[data-target]'), tabContents = document.querySelectorAll('[data-content]')

tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        const target = document.querySelector(tab.dataset.target)

        tabContents.forEach(tabContent => {
            tabContent.classList.remove('about_active')
        })

        target.classList.add('about_active')

        tabs.forEach(tab => {
            tab.classList.remove('about_active')
        })

        tab.classList.add('about_active')
    })
})


/*--- Load More --*/
const loadmore = document.getElementById('loadmore')

let currentItems = 9;
loadmore.addEventListener('click', (e) => {
    const elementList = [...document.querySelectorAll('.portfolio .project_card')];
    for(let i=currentItems; i<currentItems + 9; i++){
        if(elementList[i]){
            elementList[i].style.display = 'block';
        }
    }
    currentItems += 9;
    if(currentItems >= elementList.length){
        e.target.style.display = 'none';
    }
    if(currentItems < elementList.length){
        e.target.style.display = 'none'
    }
})

/* Go Back to previous page */
function Previous() {
    window.history.go(-1);
}  
  
  
/* Scroll Progress */
var scrollProgress = document.getElementById("progress")

let calcScrollValue = () => {
let pos = document.body.scrollTop || document.documentElement.scrollTop;

let calcHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
let percentValue = Math.round((pos * 100) / calcHeight);

if (pos > 100) {
    scrollProgress.style.display = "grid";
} else {
    scrollProgress.style.display = "none";
}

scrollProgress.style.background = `conic-gradient(#80ff00 ${percentValue}%, #d7d7d7 ${percentValue}%)`;
};

scrollProgress.addEventListener('click', () => {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
});

window.onscroll = calcScrollValue;
window.onload = calcScrollValue;
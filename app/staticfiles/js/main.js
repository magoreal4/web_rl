document.addEventListener('DOMContentLoaded', () => {
    const btn = document.querySelector('.hamburger')
    const menu = document.querySelector('.mobile-menu')
    
    btn.addEventListener('click', () => {
      // menu.classList.toggle('hidden')
      menu.classList.toggle('scale-y-100')
    })
    
    // bg-gray-700 text-gray-100
    const modeBtn = document.querySelector('.mode-button')
    const nav = document.querySelector('.nav')
    
    modeBtn.addEventListener('click', () => {
      nav.classList.toggle('bg-gray-700')
      nav.classList.toggle('text-gray-600')
      nav.classList.toggle('text-gray-100')
    })
  



  


    
  
  });
  
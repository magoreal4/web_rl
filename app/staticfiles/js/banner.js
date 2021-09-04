/*
 * based on this dribbble shot by Andrew Baygulov: https://dribbble.com/shots/6427548-Kaiser-Slideshow
 */


  
  $( document ).ready(function() {
    i=2;
    varTime = 8400;
    nSlide = $("#banner > .slide").length;
    $("#banner > .slide:first-child").addClass("active");
    $("#banner > .slide:first-child h2").addClass('word');

    // Animacipn parrafo
    let quotes = $("#banner .slide p");
    let quoteIndex = -1;
    function showNextQuote() {
      ++quoteIndex;
      quotes.eq(quoteIndex % quotes.length)
        .fadeIn(2000)
        .delay(4400)
        .fadeOut(2000);
    }
    showNextQuote();
    

      

      setInterval(() => {
        // Animación de las imagenes
        $("#banner > .slide:nth-child(" + i + ")").addClass("active");
        (i == 1) ? $("#banner > .slide:nth-child(" + (nSlide-1) + ")").removeClass("active"):null;
        (i == 2) ? $("#banner > .slide:nth-child(" + (nSlide) + ")").removeClass("active"):null;
        (i > 2) ? $("#banner > .slide:nth-child(" + (i-2) + ")").removeClass("active"):null;
        
        
        // Animacion Titulo
        $("#banner > .slide:nth-child(" + (i-1) + ") h2").removeClass('word');
        (i == 1) ? $("#banner > .slide:nth-child(" + (nSlide) + ") h2").removeClass('word'):null;
        $("#banner > .slide:nth-child(" + i + ") h2").addClass('word');

        // Animación parrafo
        showNextQuote();
       
         
    
    


        
        (i == nSlide) ? i=0:null;
        i++; 
      }, varTime);

      AOS.init({
        duration: 1200,
        easing: 'ease-in-out-back'
      });
      
});


/* When the user scrolls down, hide the navbar. When the user scrolls up, show the navbar */
window.onload = function () {
    var prevScrollPos = window.pageYOffset;
  
    if (/Mobi|Android/i.test(navigator.userAgent)) {
      // Allow navbar to move with page   
      document.getElementById("navbar").style.position = "relative";
      // Reduce big upper margin in main logo banner
      try {
        document.getElementsByClassName("mobi-header-nav-offset")[0].style["margin-top"] = "-48px";
      }
      catch(err) {}
    } else {
      window.onscroll = function () {
        var currentScrollPos = window.pageYOffset;
        console.log(prevScrollPos, currentScrollPos, document.referrer);
        if (prevScrollPos > currentScrollPos || // main - scrolling down
          prevScrollPos === 0 || // top of page
          prevScrollPos === currentScrollPos || // no movement between mouse down
          currentScrollPos - prevScrollPos > 1200 || // a big page jump, i.e. route by id
          currentScrollPos <= 0) { // scroll below 0px (i.e. go too high)
          document.getElementById("navbar").style.top = "0";
        } else {
          document.getElementById("navbar").style.top = "-60px";
        }
        prevScrollPos = currentScrollPos;
      }
    }
  }
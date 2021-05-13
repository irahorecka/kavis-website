/* When the user scrolls down, hide the navbar. When the user scrolls up, show the navbar */
window.onload = function () {
    var prevScrollPos = window.pageYOffset;

    window.onscroll = function () {
        var currentScrollPos = window.pageYOffset;
        if (prevScrollPos > currentScrollPos && prevScrollPos - currentScrollPos > 6 || // main - scrolling up AND must be at rate > 6px per read
          prevScrollPos === 0 || // top of page
          prevScrollPos === currentScrollPos || // no movement between mouse down
          currentScrollPos - prevScrollPos > 1200 || // a big page jump, i.e. route by id
          currentScrollPos <= 0) { // scroll below 0px (i.e. go too high)
          document.getElementById("navbar").style.top = "0";
        } else if (prevScrollPos - currentScrollPos < -3) {  // must be at rate > 3px per read
          document.getElementById("navbar").style.top = "-60px";
        }
        prevScrollPos = currentScrollPos;
    }
}
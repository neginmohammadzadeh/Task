
function initialize() {
  var init = { 'speed': 0, 'direction': 'normal' }
  var xhttp = new XMLHttpRequest();
  xhttp.onerror = function () {
    document.body.style.cursor = 'default'
  };
  xhttp.open("GET", apiInit, false);
  xhttp.send();

  if (xhttp.status == 200) {
    init = JSON.parse(xhttp.responseText)
  }
  else {
    alert(xhttp.statusText)
  }
  return init;
}

window.onload = function () {
  const speedUpButton = document.getElementById('speedUp');
  const reverseDirectionButton = document.getElementById('reverseDirection');
  const userInputContainer = document.getElementById('userInputContainer');


  // const userInput = '<script>alert("XSS Attack!");</script> script';
  // // Sanitize user input using DOMPurify
  // const sanitizedInput = DOMPurify.sanitize(userInput);
  // userInputContainer.innerHTML = sanitizedInput;

  var fan_init = initialize();
  // Run the application by the initial values
  setSpeed(fan_init.speed);
  setDirection(fan_init.direction);

  //Event listener of reverse button
  speedUpButton.addEventListener('click', () => {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {

      if (this.readyState == 4 && this.status == 200) {
        fan_init.speed = JSON.parse(this.responseText).speed
        setSpeed(fan_init.speed)
      }
      else if (this.readyState == 4) {
        alert('error')
      }
    };
    xhttp.onerror = function () {
      alert(xhttp.status + '-' + xhttp.statusText)
    };
    xhttp.open("GET", apiSpeedUp, true);
    xhttp.setRequestHeader("speed", fan_init.speed);
    xhttp.send();

  });
  //Event listener of reverse button
  reverseDirectionButton.addEventListener('click', () => {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
        fan_init.direction = JSON.parse(this.responseText).direction
        setDirection(fan_init.direction);
      }
      else if (this.readyState == 4) {
        alert('error')
      }
    };
    xhttp.onerror = function () {
      alert(this.statusText)
    };
    xhttp.open("GET", apiReverse, true);
    xhttp.setRequestHeader("dir", fan_init.direction);
    xhttp.send();

  });
}

//  Change UI for increase speed
function setSpeed(s) {
  const fanBlades = document.getElementById('fan-blades');
  if (s != 0) {
    speed_reverse = 1 / s;
  }
  else {
    speed_reverse = 0
  }
  fanBlades.style.animationDuration = (speed_reverse) + 's';
}
//  Change UI for reverse direction
function setDirection(d) {
  const fanBlades = document.getElementById('fan-blades');
  fanBlades.style.animationDirection = d;

}
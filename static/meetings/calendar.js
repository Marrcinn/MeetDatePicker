function changeState(buttonID) {
    // Get the button element
    var button = document.getElementById(buttonID);
  
    // Get the current state from the button's data attribute
    var currentState = button.getAttribute('data-state');
  
    // Update the state based on the current state value
    if (currentState === 'one') {
      // Change state to "two"
      button.setAttribute('data-state', 'two');
      button.style.backgroundColor = "red"; // Change the color to red
      console.log('State changed to "two"');
    } else if (currentState === 'two') {
      // Change state to "one"
      button.setAttribute('data-state', 'one');
      button.style.backgroundColor = "#BBD8B3"; // Change the color to green

      console.log('State changed to "one"');
    }
  }
 
  
  
// Declare variables
var buttonColors = ["red", "blue", "green", "yellow"];
var gamePattern = [];
var userClickedPattern = [];
var level = 0;

// Create a way to start game with inital key
$(document).keypress(function(){
    nextSequence();
});

// Capture user clicks and save to user clicked array
$("div[type=button]").click(function() {
    var userChosenColor = this.id;
    userClickedPattern.push(userChosenColor);
    // Call play sound
    playSound(userChosenColor);
    // Call animate button press
    animatePress(userChosenColor);
    console.log(userClickedPattern)
})
// Select random color and add to game pattern array
function nextSequence() {
    var randomNumber = Math.floor(Math.random() * 4);
    var randomColor = buttonColors[randomNumber];
    gamePattern.push(randomColor);
    // Animate  buttons
    $("#" + randomColor).fadeOut(100).fadeIn(100);
    // Play audio
    playSound(randomColor);
    $("h1").text("Level " + level)
    level++;
    
    console.log(gamePattern);
 
}
// Sound when user clicks button
function playSound(name) {
    var audio = new Audio("sounds/" + name + ".mp3")
    audio.play();
}
// Declare button press
function animatePress(currentColor) {
    $("#" + currentColor).addClass("pressed");
    setTimeout(function() {
        $("#" + currentColor).removeClass("pressed");
    }, 100)
    
}

nextSequence();
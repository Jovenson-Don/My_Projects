// Declare variables
var buttonColors = ["red", "blue", "green", "yellow"];
var gamePattern = [];
var userClickedPattern = [];
var level = 0;
var started = false;

// Start game on keypress
$(document).keypress(function() {
    if (!started) {
        nextSequence();
        $("h1").text("Level " + level);
        started = true;
    }
});

// Capture user clicks and save to userClickedPattern array
$("div[type=button]").click(function() {
    var userChosenColor = this.id;
    userClickedPattern.push(userChosenColor);
    
    // Call play sound
    playSound(userChosenColor);
    
    // Call animate button press
    animatePress(userChosenColor);
    
    // Check user's answer
    checkAnswer(userClickedPattern.length - 1);
});

// Select random color and add to gamePattern array
function nextSequence() {
    userClickedPattern = [];
    level++;
    $("h1").text("Level " + level);
    
    var randomNumber = Math.floor(Math.random() * 4);
    var randomColor = buttonColors[randomNumber];
    gamePattern.push(randomColor);
    
    // Animate button
    $("#" + randomColor).fadeOut(100).fadeIn(100);
    
    // Play audio
    playSound(randomColor);
}

// Sound when user clicks button
function playSound(name) {
    var audio = new Audio("sounds/" + name + ".mp3");
    audio.play();
}

// Animate button press
function animatePress(currentColor) {
    $("#" + currentColor).addClass("pressed");
    setTimeout(function() {
        $("#" + currentColor).removeClass("pressed");
    }, 100);
}

// Check user input against game pattern
function checkAnswer(currentLevel) {
    if (gamePattern[currentLevel] === userClickedPattern[currentLevel]) {
        if (userClickedPattern.length === gamePattern.length) {
            setTimeout(function () {
                nextSequence();
            }, 1000);
        }
    } else {
        // Play wrong audio and reset game
        var audio = new Audio("sounds/wrong.mp3");
        audio.play();

        $("body").addClass("game-over");
        setTimeout(function() {
            $("body").removeClass("game-over");
        }, 200);

        $("h1").text("Press A Key to Start");

        startOver();
    }

    // Start game over
    function startOver() {
        level = 0;
        gamePattern = [];
        started = false;
    }
}

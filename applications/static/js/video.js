window.onload = function () {
    if (document.getElementById('myVideo')) {
        setInterval(init, 100);
    }
    
};

function loadQuiz() {
    var player = document.getElementById('myVideo');

    if (player.currentTime >= 20 && player.currentTime < 20.1) {
        player.pause();

        if (player.webkitDisplayingFullscreen) {
            document.webkitCancelFullScreen();
        }
        var quizArea = document.getElementById('quizArea');
        quizArea.style.display = 'block';
    }
    if (player.currentTime >= 25 && player.currentTime < 25.1) {
        var quizArea = document.getElementById('quizArea');
        quizArea.style.display = 'none';
    }
}

function stateQuiz() {
    var player1 = document.getElementById('myVideo');

    if (player1.currentTime >=20 && player1.currentTime <= 25) {
        var quizArea1 = document.getElementById('quizArea');
        if (quizArea1.style.display === 'none')
            quizArea1.style.display = 'block';
    } else {
        var quizArea1 = document.getElementById('quizArea');
        if (quizArea1.style.display === 'block')
            quizArea1.style.display = 'none';
    }
}

function init() {
    loadQuiz();
    stateQuiz();
}
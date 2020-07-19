window.onload = function () {
    if (document.getElementById('myVideo')) {
        setInterval(init, 100);
    }
    
};

function loadQuiz() {
    var player = document.getElementById('myVideo');
    var origin = document.querySelector('.left_middle_content');

    // video pause
    if (player.currentTime >= 3 && player.currentTime < 3.1) {
        player.pause();

        if (player.webkitDisplayingFullscreen) {
            document.webkitCancelFullScreen();
        }
        origin.style.display = 'none';
        var quizArea = document.querySelector('.quiz1');
        quizArea.style.display = 'block';
    }
    if (player.currentTime >= 13 && player.currentTime < 13.1) {
        player.pause();

        if (player.webkitDisplayingFullscreen) {
            document.webkitCancelFullScreen();
        }
        origin.style.display = 'none';
        var quizArea = document.querySelector('.quiz2');
        quizArea.style.display = 'block';
    }
    if (player.currentTime >= 23 && player.currentTime < 23.1) {
        player.pause();

        if (player.webkitDisplayingFullscreen) {
            document.webkitCancelFullScreen();
        }
        origin.style.display = 'none';
        var quizArea = document.querySelector('.quiz3');
        quizArea.style.display = 'block';
    }

    // delete quiz
    if (player.currentTime >= 8 && player.currentTime < 8.1) {
        var quizArea = document.querySelector('.quiz1');
        quizArea.style.display = 'none';
        origin.style.display = 'block';
    }
    if (player.currentTime >= 18 && player.currentTime < 18.1) {
        var quizArea = document.querySelector('.quiz2');
        quizArea.style.display = 'none';
        origin.style.display = 'block';
    }
    if (player.currentTime >= 28 && player.currentTime < 28.1) {
        var quizArea = document.querySelector('.quiz3');
        quizArea.style.display = 'none';
        origin.style.display = 'block';
    }
}

function stateQuiz() {
    var player1 = document.getElementById('myVideo');
    var origin = document.querySelector('.left_middle_content');

    if (player1.currentTime >=3 && player1.currentTime <= 8) {
        var quizArea = document.querySelector('.quiz1');
        if (quizArea.style.display === 'none') {
            quizArea.style.display = 'block';
            origin.style.display = 'none';
        }
    } else if (player1.currentTime >= 13 && player1.currentTime <= 18) {
        var quizArea = document.querySelector('.quiz2');
        if (quizArea.style.display === 'none') {
            quizArea.style.display = 'block';
            origin.style.display = 'none';
        }
    } else if (player1.currentTime >= 23 && player1.currentTime <= 28) {
        var quizArea = document.querySelector('.quiz3');
        if (quizArea.style.display === 'none') {
            quizArea.style.display = 'block';
            origin.style.display = 'none';
        }
    } else {
        var quizArea1 = document.querySelector('.quiz1');
        var quizArea2 = document.querySelector('.quiz2');
        var quizArea3 = document.querySelector('.quiz3');
        
        if (quizArea1.style.display === 'block')
            quizArea1.style.display = 'none';
        if (quizArea2.style.display === 'block')
            quizArea2.style.display = 'none';
        if (quizArea3.style.display === 'block')
            quizArea3.style.display = 'none';

        origin.style.display = 'block';
    }
}

function init() {
    loadQuiz();
    stateQuiz();
}
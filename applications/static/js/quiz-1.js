window.onload = function () {
    if (document.getElementById('myVideo')) {
        setInterval(init, 100);
    }
    
};

function loadQuiz() {
    var player = document.getElementById('myVideo');
    var origin = document.querySelector('.left_middle_content');

    // video pause
    if (player.currentTime >= 1076 && player.currentTime < 1076.1) {
        player.pause();

        if (player.webkitDisplayingFullscreen) {
            document.webkitCancelFullScreen();
        }
        origin.style.display = 'none';
        var quizArea = document.querySelector('.quiz1');
        quizArea.style.display = 'block';
    }
    if (player.currentTime >= 272 && player.currentTime < 272.1) {
        player.pause();

        if (player.webkitDisplayingFullscreen) {
            document.webkitCancelFullScreen();
        }
        origin.style.display = 'none';
        var quizArea = document.querySelector('.quiz2');
        quizArea.style.display = 'block';
    }
    if (player.currentTime >= 858 && player.currentTime < 858.1) {
        player.pause();

        if (player.webkitDisplayingFullscreen) {
            document.webkitCancelFullScreen();
        }
        origin.style.display = 'none';
        var quizArea = document.querySelector('.quiz3');
        quizArea.style.display = 'block';
    }

    // delete quiz
    if (player.currentTime >= 1086 && player.currentTime < 1086.1) {
        var quizArea = document.querySelector('.quiz1');
        quizArea.style.display = 'none';
        origin.style.display = 'block';
    }
    if (player.currentTime >= 282 && player.currentTime < 282.1) {
        var quizArea = document.querySelector('.quiz2');
        quizArea.style.display = 'none';
        origin.style.display = 'block';
    }
    if (player.currentTime >= 868 && player.currentTime < 868.1) {
        var quizArea = document.querySelector('.quiz3');
        quizArea.style.display = 'none';
        origin.style.display = 'block';
    }
}

function stateQuiz() {
    var player1 = document.getElementById('myVideo');
    var origin = document.querySelector('.left_middle_content');

    if (player1.currentTime >=1076 && player1.currentTime <= 1086) {
        var quizArea = document.querySelector('.quiz1');
        if (quizArea.style.display === 'none') {
            quizArea.style.display = 'block';
            origin.style.display = 'none';
        }
    } else if (player1.currentTime >= 272 && player1.currentTime <= 282) {
        var quizArea = document.querySelector('.quiz2');
        if (quizArea.style.display === 'none') {
            quizArea.style.display = 'block';
            origin.style.display = 'none';
        }
    } else if (player1.currentTime >= 858 && player1.currentTime <= 868) {
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
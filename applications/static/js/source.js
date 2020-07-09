function moveTime(timestamp) {
    if (timestamp === 'quiz1'){
        var time = 20;
    } else if (timestamp === 'quiz2') {
        var time = 41;
    }
    var myVideo = document.getElementById("myVideo");
    myVideo.currentTime = time;
    myVideo.play();
}

function scriptToggle() {
    var scBtn = document.getElementById('scriptBtn')
    var sc = document.getElementById('scriptValue').style;

    if (sc.display === "none") {
        sc.display = "block";
        scBtn.innerText = "스크립트 닫기";
    } else {
        sc.display = "none";
        scBtn.innerText = "스크립트 열기";
    }
}

function questionToggle(quesName) {
    if (quesName === 'quiz1') {
        var q = document.getElementById('quizDiv1').style;
        var a = document.getElementById('ansDiv1').style;
    } else if (quesName === 'quiz2') {
        var q = document.getElementById('quizDiv2').style;
        var a = document.getElementById('ansDiv2').style;
    }

    if (q.display === 'block') {
        q.display = 'none';
        a.display = 'block';
    } else {
        q.display = 'block';
        a.display = 'none';
    }
}
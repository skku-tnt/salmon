function questionToggle(quesName) {
    if (quesName === 'quiz1') {
        var a = document.getElementById('ans1');
        a.innerText = '정답 : 종교개혁';
    } else if (quesName === 'quiz2') {
        var a = document.getElementBㅉyId('ans2');
        a.innerText = '정답 : 로마 카톨릭교';
    } else if (quesName === 'quiz3') {
        var a = document.getElementById('ans3');
        a.innerText = '정답 : 츠 빙 글리';
    }
}
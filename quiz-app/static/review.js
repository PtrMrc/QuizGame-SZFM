const reviewList = document.getElementById("review-list");
const answers = JSON.parse(localStorage.getItem("playerAnswers")) || [];

answers.forEach((q, i) => {
    const li = document.createElement("li");
    li.innerHTML = `
        <strong>${i+1}. ${q.question}</strong><br>
        ${q.answers.map((a, idx) => {
            if(idx === q.correct) return `<span style="color:green">${a} ✅</span>`;
            if(idx === q.selected && idx !== q.correct) return `<span style="color:red">${a} ❌</span>`;
            return a;
        }).join('<br>')}
        <hr>
    `;
    reviewList.appendChild(li);
});

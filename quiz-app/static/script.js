// Kezdő oldal

function startGame() {
  const name = document.getElementById('playerName').value;
  if (!name) {
    alert('Kérlek, add meg a neved!');
    playerName = name;
    return;
  }
  localStorage.setItem("playerName", name);
  window.location.href = "/quiz";
}

//Kérdés-válasz oldal

let questions = [];
let correctAnswers = 0;
let currentQuestion = 0;
let score = 0;
let timer;
let timeLeft = 20;
let totalQuestions = 0;

async function loadQuestions() {
  const response = await fetch("questions.json");
  allquestions = await response.json();

  // Kérdések összekeverése
  allquestions.sort(() => Math.random() - 0.5);

  // Maximum 10 kérdés kiválasztása
  questions = allquestions.slice(0, 10);

  totalQuestions = questions.length;
  loadQuestion();
}

function loadQuestion() {
  timeLeft = 20;
  document.getElementById("timer").textContent = `Idő: ${timeLeft}s`;
  document.getElementById("score").textContent = `Pontok: ${score}`;
  document.getElementById("question").textContent = questions[currentQuestion].question;

  const optionButtons = document.querySelectorAll(".option-btn");
  questions[currentQuestion].answers.forEach((answer, i) => {
    optionButtons[i].textContent = answer;
  });

  startTimer();
}

function startTimer() {
  clearInterval(timer);
  timeLeft = 20;
  document.getElementById("time-bar").style.width = "100%";

  timer = setInterval(() => {
    timeLeft--;
    document.getElementById("timer").textContent = `Idő: ${timeLeft}s`;
    document.getElementById("time-bar").style.width = (timeLeft / 20 * 100) + "%";

    if (timeLeft <= 0) {
      clearInterval(timer);
      nextQuestion();
    }
  }, 1000);
}

function selectAnswer(index) {
  if (index === questions[currentQuestion].correct) {
    const basePoints = 50;
    const speedBonus = timeLeft * 3; // 3 bónusz pont minden megmaradt másodpercért
    score += basePoints + speedBonus;
    correctAnswers++;
  }
  nextQuestion();
}

function nextQuestion() {
  currentQuestion++;
  if (currentQuestion < questions.length) {
    loadQuestion();
  } else {
    endGame();
  }
}



function endGame() {
  localStorage.setItem("lastScore", score);
  localStorage.setItem("lastCorrect", correctAnswers);
  localStorage.setItem("lastTotal", totalQuestions);
  const playerName = localStorage.getItem("playerName") || "Ismeretlen";
  localStorage.setItem("playerName", playerName);
  window.location.href = "/end";
}

//Kvíz vége oldal


// --- Kvíz vége oldal betöltésekor:
if (document.body.contains(document.querySelector(".end-container"))) {
  const finalScore = localStorage.getItem("lastScore") || 0;
  const correct = localStorage.getItem("lastCorrect") || 0;
  const total = localStorage.getItem("lastTotal") || 0;
  const playerName = localStorage.getItem("playerName") || "Ismeretlen";

  document.getElementById("final-score").textContent = `Elért pontszám: ${finalScore}`;
  document.getElementById("correct-answers").textContent = `Helyes válaszok: ${correct}/${total}`;

  // --- Ranglista localStorage-ban ---
  let leaderboard = JSON.parse(localStorage.getItem("leaderboard")) || [];
  leaderboard.push({ name: playerName, score: finalScore });
  leaderboard.sort((a, b) => b.score - a.score);
  leaderboard = leaderboard.slice(0, 15); // csak top 5

  localStorage.setItem("leaderboard", JSON.stringify(leaderboard));

  const list = document.getElementById("leaderboard");

  leaderboard.forEach((player, index) => {
  const li = document.createElement("li");

  // érmek hozzáadása
  let medal = "";
  if (index === 0) medal = "👑 ";   // első hely
  else if (index === 1) medal = "🥈 "; // második hely
  else if (index === 2) medal = "🥉 "; // harmadik hely

  li.textContent = `${medal}${player.name} - ${player.score} pont`;

  // Ha ez az utoljára hozzáadott játékos, akkor "NEW" jelzés a jobb oldalon
  const lastAddedName = playerName; // a mostani játékos
  if (player.name === lastAddedName && player.score == finalScore) {
    const newBadge = document.createElement("span");
    newBadge.textContent = " NEW";
    newBadge.style.color = "#FF5722";
    newBadge.style.fontWeight = "bold";
    li.appendChild(newBadge);
  }

  list.appendChild(li);
});
}

// --- Restart gomb ---
function restartGame() {
  window.location.href = "/";
}


//Első kérdés betöltése
if (document.body.contains(document.querySelector(".quiz-container"))) {
  loadQuestions();
}


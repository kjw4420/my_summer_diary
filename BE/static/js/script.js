var modal = document.getElementById("signup-modal");
var signupButton = document.getElementById("signup-button");
var closeButton = document.getElementsByClassName("close")[0];

function goToIndexPage() {
  var vacationStartPeriod = document.getElementById("vacation-startperiod").value;
  var vacationFinishPeriod = document.getElementById("vacation-finishperiod").value;
  var url = "./index.html?start=" + encodeURIComponent(vacationStartPeriod) + "&finish=" + encodeURIComponent(vacationFinishPeriod);
  window.location.href = url;
}

signupButton.onclick = function() {
  modal.style.display = "block";
}

closeButton.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

function changeColor() {
  var loginButton = document.getElementById('loginbutton');
  loginButton.style.backgroundColor = 'red';
  loginButton.style.color = 'white';
}

// 회원 가입 폼 검증
var signupForm = document.getElementById("signup-form");

signupForm.onsubmit = function(event) {
var passwordInput = document.getElementById("signup-password");
var confirmPasswordInput = document.getElementById("signup-confirm-password");

if (passwordInput.value !== confirmPasswordInput.value) {
 alert("비밀번호가 일치하지 않습니다.");
 event.preventDefault(); // 폼 제출 방지
}
}
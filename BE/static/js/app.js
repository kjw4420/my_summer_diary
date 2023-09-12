const canvas = document.getElementById("jsCanvas");
const ctx = canvas.getContext("2d");
const colors = document.getElementsByClassName("jsColor");
const range = document.getElementById("jsRange");
const eraseBtn = document.getElementById("jsErase");
const saveBtn = document.getElementById("jsSave");

const INITIAL_COLOR = "#000000";
const CANVAS_WIDTH = 420;
const CANVAS_HEIGHT = 300;
ctx.strokeStyle = INITIAL_COLOR;

canvas.width = CANVAS_WIDTH;
canvas.height = CANVAS_HEIGHT;

ctx.fillStyle = "transparent";
ctx.fillRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);

ctx.strokeStyle = INITIAL_COLOR;
ctx.fillStyle = INITIAL_COLOR;
ctx.lineWidth = 2.5;

let painting = false;
let erasing = false;

function stopPainting() {
  painting = false;
}

function startPainting() {
  painting = true;
}

function getMousePos(event) {
  const rect = canvas.getBoundingClientRect();
  const scaleX = canvas.width / rect.width;
  const scaleY = canvas.height / rect.height;
  return {
    x: (event.clientX - rect.left) * scaleX,
    y: (event.clientY - rect.top) * scaleY,
  };
}

function onMouseMove(event) {
  const { x, y } = getMousePos(event);
  if (!painting) {
    ctx.beginPath();
    ctx.moveTo(x, y);
  } else {
    if (erasing) {
      ctx.globalCompositeOperation = "destination-out";
      ctx.clearRect(0, 0, canvas.width, canvas.height); // 그림 전체를 지우는 부분
      ctx.fillRect(0, 0, canvas.width, canvas.height);
    } else {
      ctx.globalCompositeOperation = "source-over";
      ctx.lineTo(x, y);
      ctx.stroke();
    }
  }
}

function handleColorClick(event) {
  const color = event.target.style.backgroundColor;
  ctx.strokeStyle = color;
}

function handleRangeChange(event) {
  const size = event.target.value;
  ctx.lineWidth = size;
}

function handleEraseClick() {
  erasing = !erasing;
  if (erasing) {
    eraseBtn.innerText = "그림 그리기";
  } else {
    eraseBtn.innerText = "그림 지우기";
  }
}

//이거 수정
function handleSaveClick() {
  var image = canvas.toDataURL("image/png"); //문자열 반환

  var blobBin = atob(image.split(",")[1]); // base64 데이터 디코딩
  var array = [];
  for (var i = 0; i < blobBin.length; i++) {
    array.push(blobBin.charCodeAt(i));
  }
  var file = new Blob([new Uint8Array(array)], { type: "image/png" }); // Blob 생성
  var dataForm = document.getElementById("form");
  var formData = new FormData(dataForm);
  formData.append("drawing", file); // file data 추가

  fetch("insert/", {
    method: "POST",
    body: formData,
  });
}

if (canvas) {
  canvas.addEventListener("mousemove", onMouseMove);
  canvas.addEventListener("mousedown", startPainting);
  canvas.addEventListener("mouseup", stopPainting);
  canvas.addEventListener("mouseleave", stopPainting);
}

Array.from(colors).forEach((color) =>
  color.addEventListener("click", handleColorClick)
);

if (range) {
  range.addEventListener("input", handleRangeChange);
}

if (eraseBtn) {
  eraseBtn.addEventListener("click", handleEraseClick);
}

//여기
if (saveBtn) {
  saveBtn.addEventListener("click", handleSaveClick);
}

document.getElementById("texts").style.fontSize = "20px";

// JavaScript 코드
var weatherImages = document.querySelectorAll(".weather-image");

weatherImages.forEach(function (image) {
  image.addEventListener("click", function () {
    weatherImages.forEach(function (img) {
      img.classList.remove("clicked");
    });
    this.classList.add("clicked");
  });
});

//저장 버튼 눌리면 창닫기

const submitBtn = document.querySelector(".submit");

submitBtn.addEventListener("click", function () {
  window.close();
});

//작성 취소
const cancelBtn = document.querySelector(".cancel");
const titleInput = document.getElementById("title");
const contentTextarea = document.getElementById("texts");

cancelBtn.addEventListener("click", function () {
  titleInput.value = "";
  contentTextarea.value = "";
});

const uploadBtn = document.querySelector(".btn-upload");
const fileInput = document.getElementById("file");

uploadBtn.addEventListener("click", function () {
  fileInput.click();
});

fileInput.addEventListener("change", function () {
  const selectedFile = fileInput.files[0];
  if (selectedFile && selectedFile.type.startsWith("image/")) {
    // 선택한 파일이 사진 파일인 경우에 대한 처리 로직을 여기에 작성합니다.
  } else {
    // 선택한 파일이 사진 파일이 아닌 경우에 대한 처리 로직을 여기에 작성합니다.
    alert("사진 파일만 업로드할 수 있습니다.");
    fileInput.value = ""; // 선택한 파일 초기화
  }
});

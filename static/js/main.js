// 전체 컨텐츠 저장
if (document.getElementById("content")) {
  var contents = document.getElementById("content").innerHTML;
}

function refresh() {
  if (document.getElementById("content")) {
    var count = document.getElementById("content").childElementCount;
    for (var i = count; i < 6; i++) {
      var divs = document.createElement("div");
      divs.className = "content-blank";
      document.getElementById("content").appendChild(divs);
    }
  }
}

$(document).ready(function () {
  refresh();
});

// 파일 업로드
function loadFile(input) {
  var container = document.getElementById("content-img");
  var file = input.files[0]; //선택된 파일 가져오기;

  // 파일 선택 취소하면 다시 업로드 버튼 생성
  if (!document.getElementById("imgfile").value) {
    container.innerHTML = "";
    var iconImg = document.createElement("img");
    var divImg = document.createElement("div");
    iconImg.setAttribute("src", "/static/images/upload.png");
    divImg.setAttribute("class", "fs-5 text-primary");
    divImg.innerText += "여기를 눌러 업로드";
    container.appendChild(iconImg);
    container.appendChild(divImg);
  }

  //새로운 이미지 div 추가
  var newImage = document.createElement("img");
  newImage.className += "img-fluid content-img";

  //이미지 source 가져오기
  newImage.src = URL.createObjectURL(file);

  newImage.style.width = "50%";
  newImage.style.height = "50%";

  if (container.hasChildNodes()) {
    container.innerHTML = "";
    // 기존에 있던 이미지 삭제
  }
  container.appendChild(newImage);
}

// 파일 업데이트
function updateFile(input) {
  var file = input.files[0]; //선택된 파일 가져오기

  // 파일 선택 안했으면 리턴
  if (!document.getElementById("imgfile").value) {
    return;
  }
  //새로운 이미지 div 추가
  var newImage = document.createElement("img");
  newImage.setAttribute("class", "img");
  newImage.className += "img-fluid content-img";

  //이미지 source 가져오기
  newImage.src = URL.createObjectURL(file);

  var container = document.getElementById("content-img");
  if (container.hasChildNodes()) {
    container.removeChild(container.childNodes[0]);
  }
  container.appendChild(newImage);
}

function changeTag(value) {
  var container = document.getElementById("content");
  container.innerHTML = contents;
  if (value == "메모") {
    let tmp = document.querySelectorAll(".일기");
    for (var i = 0; i < tmp.length; i++) {
      tmp[i].remove();
    }
  } else if (value == "일기") {
    let tmp = document.querySelectorAll(".메모");
    for (var i = 0; i < tmp.length; i++) {
      tmp[i].remove();
    }
  }

  refresh();
}

// 폼 유효성검사

// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
  "use strict";

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll(".needs-validation");

  // Loop over them and prevent submission
  Array.from(forms).forEach((form) => {
    form.addEventListener(
      "submit",
      (event) => {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }

        form.classList.add("was-validated");
      },
      false
    );
  });
})();

// 모달 나가면 새로고침
$("#PostModal").on("hidden.bs.modal", function () {
  location.reload();
});

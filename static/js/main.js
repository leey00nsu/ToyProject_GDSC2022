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
  alert(value);

  // $.ajax({
  //   url: "/",
  //   type: "GET",
  //   data: {
  //     input_val: input_val.value,
  //   },
  //   datatype: "json", // 서버에서 반환되는 데이터 json 형식
  //   success: function (data) {
  //     // AJAX 통신이 성공하면 해당 과일의 영어 단어가 출려되도록
  //     console.log(data["eng"]); // 콘솔에서 확인
  //     var element = document.getElementById("div_id");
  //     document.all("div_id").innerHTML = data["eng"];
  //   },
  // });
}

// 폼 유효성검사
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

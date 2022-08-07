function loadFile(input) {
  var file = input.files[0]; //선택된 파일 가져오기

  //새로운 이미지 div 추가
  var newImage = document.createElement("img");
  newImage.setAttribute("class", "img");

  //이미지 source 가져오기
  newImage.src = URL.createObjectURL(file);

  newImage.style.width = "50%";
  newImage.style.height = "50%";
  // newImage.style.visibility = "hidden";   //버튼을 누르기 전까지는 이미지를 숨긴다
  newImage.style.objectFit = "contain";

  //이미지를 image-show div에 추가
  var container = document.getElementById("image-show");
  if (container.hasChildNodes()) {
    container.removeChild(container.childNodes[0]);
  }
  container.appendChild(newImage);
}

function updateFile(input) {
  var file = input.files[0]; //선택된 파일 가져오기

  //새로운 이미지 div 추가
  var newImage = document.createElement("img");
  newImage.setAttribute("class", "img");
  newImage.className += "img-fluid content-img";

  //이미지 source 가져오기
  newImage.src = URL.createObjectURL(file);

  //이미지를 image-show div에 추가
  var container = document.getElementById("content-img");
  if (container.hasChildNodes()) {
    container.removeChild(container.childNodes[0]);
  }
  container.appendChild(newImage);
}

function changeTag(value) {
  alert(value);

  $.ajax({
    url: "/",
    type: "GET",
    data: {
      input_val: input_val.value,
    },
    datatype: "json", // 서버에서 반환되는 데이터 json 형식
    success: function (data) {
      // AJAX 통신이 성공하면 해당 과일의 영어 단어가 출려되도록
      console.log(data["eng"]); // 콘솔에서 확인
      var element = document.getElementById("div_id");
      document.all("div_id").innerHTML = data["eng"];
    },
  });
}

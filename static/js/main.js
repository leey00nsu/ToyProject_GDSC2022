function loadFile(input) {
  console.log("in");
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

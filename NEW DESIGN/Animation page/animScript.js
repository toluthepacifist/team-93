const arrowAnimBtn = document.querySelectorAll("#arrowBtn");

function arrow() {
  let arrowImg = document.querySelector(".arrowImg");

  for (let i = 0; i < arrowAnimBtn.length; i++) {
    arrowAnimBtn[i].addEventListener("click", (e) => {
      if (arrowAnimBtn[i].value === "1") {
        arrowImg.className = "animated fadeIn";
        setTimeout(() => {
          arrowImg.className = "arrowImg";
        }, 2000);

        console.log("is is 1");
      } else if (arrowAnimBtn[i].value === "2") {
        arrowImg.className = "animated fadeOut";
        setTimeout(() => {
          arrowImg.className = "arrowImg";
        }, 2000);

        console.log("is is 2");
      } else if (arrowAnimBtn[i].value === "3") {
        arrowImg.className = "animated fadeInBorder";
        setTimeout(() => {
          arrowImg.className = "arrowImg";
        }, 2000);

        console.log("it is 3");
      } else if (arrowAnimBtn[i].value === "4") {
        arrowImg.className = "animated fadeInLeft";
        setTimeout(() => {
          arrowImg.className = "arrowImg";
        }, 2000);

        console.log("it is 4");
      } else if (arrowAnimBtn[i].value === "5") {
        arrowImg.className = "animated fadeInRight";
        setTimeout(() => {
          arrowImg.className = "arrowImg";
        }, 2000);

        console.log("it is 5");
      } else if (arrowAnimBtn[i].value === "6") {
        arrowImg.className = "animated fadeInUp";
        setTimeout(() => {
          arrowImg.className = "arrowImg";
        }, 2000);

        console.log("it is 6");
      }
    });
  }
}
arrow();

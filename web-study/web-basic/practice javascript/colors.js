let Links = {
  setColor: function (color) {
    // const alist = document.querySelectorAll("a");
    // let i = 0;
    // while (i < alist.length) {
    //   alist[i].style.color = color;
    //   i = i + 1;
    // }
    $("a").css("color", color);
  },
};

let Body = {
  setBackgroundColor: function (color) {
    //document.querySelector("body").style.backgroundColor = color;
    $("body").css("backgroundColor", color);
  },
  setColor: function (color) {
    //document.querySelector("body").style.color = color;
    $("body").css("color", color);
  },
};

function nightDayHandler(self) {
  if (self.value === "night") {
    Body.setBackgroundColor("black");
    Body.setColor("white");
    self.value = "day";

    Links.setColor("powderblue");
  } else {
    Body.setBackgroundColor("white");
    Body.setColor("black");
    self.value = "night";

    Links.setColor("blue");
  }
}

let Link = {
  setColor: function (color) {
    alist = document.querySelectorAll("a");
    let i = 0;
    while (i < alist.length) {
      alist[i].style.color = color;
      i += 1;
    }
  },
};

let Body = {
  setBackgroundColor: function (color) {
    document.querySelector("body").style.backgroundColor = color;
  },
  setColor: function (color) {
    document.querySelector("body").style.color = color;
  },
};

function nightDayHandler(self) {
  body = document.querySelector("body");
  a = document.querySelectorAll("a");
  if (self.value === "night") {
    self.value = "day";
    Body.setBackgroundColor("black");
    Body.setColor("yellow");
    Link.setColor("purple");
  } else {
    self.value = "night";
    body.style.backgroundColor = "white";
    body.style.color = "black";
    Link.setColor("blue");
  }
}

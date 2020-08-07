const express = require("express");
const app = express();

const PORT = 4000;

const handleListening = () => {
  console.log(`Listening on: http://localhost:${PORT}`);
};

const handleHome = (req, res) => {
  console.log("Hi from Home");
  res.send("Hi");
};

app.get("/", handleHome);

app.listen(PORT, handleListening);

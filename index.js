import express from "express";
const app = express();

const PORT = 4000;

const handleListening = () => {
  console.log(`Listening on: http://localhost:${PORT}`);
};

const handleHome = (req, res) => {
  console.log("Hi from Home");
  res.send("Hi");
};

const between = (req, res, next) => {
  console.log("between");
  next();
};

app.use(between);

app.get("/", handleHome);

app.listen(PORT, handleListening);

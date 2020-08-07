import express from "express";
import morgan from "morgan";
import helmet from "helmet";
import cookieParser from "cookie-parser";
import bodyParser from "body-parser";

const app = express();

const PORT = 4000;

const handleListening = () => {
  console.log(`Listening on: http://localhost:${PORT}`);
};

const handleHome = (req, res) => {
  console.log("Hi from Home");
  res.send("Home");
};
const handleProfile = (req, res) => {
  console.log("Hi from Profile");
  res.send("Profile");
};

app.use(cookieParser());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(helmet());
app.use(morgan("tiny"));

app.get("/", handleHome);
app.get("/profile", handleProfile);
app.listen(PORT, handleListening);

import app from "./app";
import "./db";

const PORT = 5000;

const handleListening = () => {
  console.log(`Listening on: http://localhost${PORT}`);
};

app.listen(PORT, handleListening);

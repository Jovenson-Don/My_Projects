import express from "express";
import bodyParser from "body-parser";
import { name } from "ejs";

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.render("index.ejs");
});

app.post("/submit", (req, res) => {
  const firstName = req.body["fName"].length;
  const lastName = req.body["lName"].length;
  const nameLength = firstName + lastName
  res.render("index.ejs", {results: nameLength});
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

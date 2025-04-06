import express from "express";
const app = express();
const port = 3000;

app.get("/", (req, res) => {
  res.send("<h1>Hello world!</h1>");
});

app.get("/about", function(req, res) {
  res.send("<h2>About Me</h2>,");
});

app.get("/contact", (req, res) => {
  res.send("<h1>Contact Me</h1><p>7742402535</p>")
})

app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});

import express from "express";
import bodyParser from "body-parser";


const app = express();
const port = "3000";

app.use(bodyParser.urlencoded({ extended: true }));


app.get("/", (req, res) => {
    res.render("index.ejs");
});

app.get("/create", (req, res) => {
    res.render("create.ejs")
})

app.get("/viewblogs", (req, res) => {
    res.render("create.ejs")
})


app.listen(port, () => {
    console.log(`Listen on port: ${port}`)
});

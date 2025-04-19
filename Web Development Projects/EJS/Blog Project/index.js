import express from "express";
import bodyParser from "body-parser";


const app = express();
const port = "3000";
const allBlogs = []

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"))


app.get("/", (req, res) => {
    res.render("index.ejs");
});

app.get("/create", (req, res) => {
    res.render("create.ejs");
});

app.get("/viewblogs", (req, res) => {
    res.render("viewblogs.ejs", {blogs: allBlogs});
});
app.get("/view", (req, res) => {
    res.render("view.ejs");
    console.log(req.body);
});

app.post("/createdblog", (req, res) => {
    const results = req.body;
    allBlogs.push(results);
    console.log(req.body);
    res.render("createdblog.ejs", {data: results});
});


app.listen(port, () => {
    console.log(`Listen on port: http://127.0.0.1:${port}`)
});

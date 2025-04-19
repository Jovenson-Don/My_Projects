import express from "express";
import bodyParser from "body-parser";


const app = express();
const port = "3000";
const allBlogs = []
let blogID = 0

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"))


app.get("/", (req, res) => {
    res.render("index.ejs", {blogs: allBlogs});
});

app.get("/create", (req, res) => {
    res.render("create.ejs");
});

app.get("/all-blogs", (req, res) => {
    res.render("all-blogs.ejs", {blogs: allBlogs});
});

app.get("/edit-blog/:id", (req, res) => {
    blogID = req.params.id;
    res.render("edit-blog.ejs", {post: allBlogs[blogID]});
});
app.post("/submit", (req,res) => {
    allBlogs.push(req.body);
    res.redirect("/all-blogs");
});

app.post("/updated", (req, res) => {
    allBlogs[blogID] = req.body;
    res.redirect("/all-blogs");
    
});

app.get("/delete/:id", (req, res) => {
    blogID = req.params.id;
    allBlogs.pop(blogID);
    res.redirect("/all-blogs");
});

app.listen(port, () => {
    console.log(`Listen on port: http://127.0.0.1:${port}`)
});

import axios from "axios";
import express from "express";
import pg from "pg";
import bodyParser from "body-parser";

const app = express();
const port = 3000;
const db = new pg.Client({
    user: "postgres",
    database: "books",
    password: "Gameover21",
    host: "localhost",
    port: 5432
});

app.use(bodyParser.urlencoded({ extended: true}));
app.use(express.static("public"));

db.connect();

app.get("/", async (req, res) => {
    
    res.render("index.ejs");
});
app.post("/", async (req, res) => {
    console.log(req.body.isbn);
    const isbn = req.body.isbn;
    const response = await axios.get(`https://covers.openlibrary.org/b/isbn/${isbn}-L.jpg`);
    console.log(response.data);
    res.render("index.ejs", {data: response.data})
})

app.listen(port, () => {
    console.log(`We lit at https://127.0.0.1:${port}`)
});
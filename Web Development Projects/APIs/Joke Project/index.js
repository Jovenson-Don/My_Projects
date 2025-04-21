import express from "express";
import bodyParser from "body-parser";
import axios from "axios";

const app = express();
const port = 3000;
const API_URL = "https://v2.jokeapi.dev/joke/Any?type=single";

app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));


app.get("/", async (req, res) => {
    try {
        const response = await axios.get(API_URL);
        const data = response.data;
        res.render("index.ejs", { joke: data}) 
    } catch (error) {
        console.error(error.message)
    }
});

app.listen(port, () => {
    console.log(`We lit at http://127.0.0.1:${port}`)
});
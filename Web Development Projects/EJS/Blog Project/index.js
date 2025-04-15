import express from "express";
import bodyParser from "bodyParser"

const app = express();
const port = "3000";


app.get("/", (req, res) => {
    res.send("hello");
});
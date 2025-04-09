import express from "express";

const app = express();
const port = 3000;

const d = new Date();
let day = d.getDay();

let type = "a weekday";
let adv ="time to workkkk....";

if (day < 0 || day > 5) {
    type = "the weekend!";
    adv ="time to have fun!!!"; 
};

app.get("/", (req, res) => {
    res.render("index.ejs", {
        dayType: type,
        advice: adv,
    });
});
app.listen(port, () => {
    console.log(`We lit at port ${port}`);
});
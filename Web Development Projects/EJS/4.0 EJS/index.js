import express from "express";

const app = express();
const port = 3000;

const d = new Date("April 12, 2025 01:15:00");
let day = d.getDay();

let type = "a weekday";
let adv ="time to workkkk....";

if (d < 0 || d > 5) {
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
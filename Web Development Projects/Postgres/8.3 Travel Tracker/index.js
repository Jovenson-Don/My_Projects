import express, { response } from "express";
import bodyParser from "body-parser";
import pg from "pg";

const app = express();
const port = 3000;
const db = new pg.Client({
  user: "postgres",
  host: "localhost",
  database: "world",
  password: "Gameover21",
  port: 5432
});

db.connect();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));

app.get("/", async (req, res) => {
  //Write your code here.
  try {
    const result = await db.query(
      "SELECT country_code FROM visited_countries"
    );
    const countryCodes = result.rows.map(item => item.country_code);
    res.render("index.ejs", { countries: countryCodes, total: result.rows.length});
    db.end();
  } catch (error) {
    console.error("Error:", error)
    res.render("index.ejs", {error: error})
  }
});

app.post("/add", async (req, res) => {
  try {
    const result = await db.query(
      "SELECT country_code FROM countries WHERE country_name = $1", 
      [req.body.country]);

      const countryCode = result.rows[0].country_code;

      try {
        await db.query("INSERT INTO visited_countries (country_code) VALUES ($1)", 
          [countryCode]);
          res.redirect("/");
        
      } catch (error) {
        console.error(error.message)
        res.render("index.ejs")
      }
  } catch (error) {
    console.error(error.message)
    res.render("index.ejs")
  }
  
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});

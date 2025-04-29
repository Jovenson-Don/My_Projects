import express from "express";
import bodyParser from "body-parser";
import pg from "pg";

const app = express();
const port = 3000;
const db = new pg.Client({
  user: "postgres",
  database: "permalist",
  host: "localhost",
  password: "Gameover21",
  port: 5432
});

db.connect();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));

app.get("/", async (req, res) => {
  try {
    const result = await db.query("SELECT * FROM items ORDER BY id");
    let items = result.rows;
    console.log(items)
    res.render("index.ejs", {
      listTitle: "Today",
      listItems: items,
    });
  } catch (error) {
    console.log(error);
    res.redirect("/");
  }
});

app.post("/add", async (req, res) => {
  const item = req.body.newItem;
  try {
    await db.query(
      "INSERT INTO items (title) VALUES ($1)",
    [item]);
    res.redirect("/");
  } catch (error) {
    console.log(error);
    res.redirect("/");
  }
  
});

app.post("/edit", async (req, res) => {
  const id = req.body.updatedItemId;
  const title = req.body.updatedItemTitle;
  try {
  await db.query(
    "UPDATE items SET title = $1 WHERE id = $2",
  [title, id]);
  res.redirect("/");
  } catch(error) {
    console.log(error);
    res.redirect("/");
  }
});

app.post("/delete", async (req, res) => {
  const deletedID = req.body.deleteItemId;
  await db.query(
    "DELETE FROM items WHERE id = $1",
  [deletedID]);
  res.redirect("/");
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

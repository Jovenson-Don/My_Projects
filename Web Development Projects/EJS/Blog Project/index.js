import express from "express";
import bodyParser from "body-parser";
import session from "express-session";
import env from "dotenv";
import pg from "pg";
import bcrypt from "bcrypt";
import passport from "passport";
import { Strategy } from "passport-local";
import methodOverride from "method-override";

const app = express();
const port = "3000";
const saltRounds = 10;

env.config();

const db = new pg.Client({
  user: process.env.PG_USER,
  password: process.env.PG_PASSWORD,
  database: process.env.PG_DATABASE,
  port: process.env.PG_PORT,
  host: process.env.PG_HOST,
});

db.connect();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));
app.use(methodOverride("_method"));

app.use(
  session({
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: true,
  })
);

app.use(passport.initialize());
app.use(passport.session());

app.get("/", async (req, res) => {
  if (req.isAuthenticated()) {
    const id = req.user.id;
    try {
      const result = await db.query(
        "SELECT * FROM blog WHERE user_id = $1 ORDER BY time DESC",
        [id]
      );
      res.render("index.ejs", { blogs: result.rows });
    } catch (error) {
      console.log(error);
    }
  } else {
    res.redirect("/login");
  }
});

app.get("/login", (req, res) => {
  res.render("login.ejs");
});

app.get("/logout", (req, res) => {
  req.logout((err) => {
    if (err) {
      return next(err);
    } else {
      res.redirect("/login");
    }
  });
});

app.get("/register", (req, res) => {
  res.render("register.ejs");
});

app.get("/create", (req, res) => {
  res.render("create.ejs", { userInfo: req.user });
});

app.get("/all-blogs", async (req, res) => {
  const id = req.user.id;
  try {
    const result = await db.query(
      "SELECT * FROM blog WHERE user_id = $1 ORDER BY time DESC",
      [id]
    );
    res.render("all-blogs.ejs", { blogs: result.rows });
  } catch (error) {
    console.log(error);
  }
});

app.get("/edit-blog/:id", async (req, res) => {
  const id = req.params.id;
  try {
    const result = await db.query(
      "SELECT * FROM blog where id = $1",
      [id]
    );
    const post = result.rows[0];
    res.render("edit-blog.ejs", { post: post });
  } catch (error) {
    console.log(error);
  }
});

app.post("/registering", async (req, res) => {
  const userInfo = req.body;
  try {
    const result = await db.query("SELECT * FROM users WHERE email = $1", [
      userInfo.email,
    ]);

    if (result.rows.length > 0) {
      res.send("Email found. Please login");
    } else {
      bcrypt.hash(userInfo.password, saltRounds, async (error, hash) => {
        if (error) {
          console.log(error);
        } else {
          const newUser = await db.query(
            "INSERT INTO users (fname, lname, email, password) VALUES ($1, $2, $3, $4) RETURNING *",
            [userInfo.fname, userInfo.lname, userInfo.email, hash]
          );
          const user = newUser.rows[0];
          req.login(user, (error) => {
            res.redirect("/");
          });
        }
      });
    }
  } catch (error) {
    console.log(error);
  }
});

app.post("/submit", async (req, res) => {
  const blog = req.body.blog;
  const subject = req.body.subject;
  const fullName = req.body.full_name;
  const id = req.user.id;
  try {
    await db.query(
      "INSERT INTO blog (blog, user_id, subject, full_name, time) VALUES ($1, $2, $3, $4, $5)",
      [
        blog,
        id,
        subject,
        fullName,
        new Date().toLocaleString("en-US", { timeZone: "America/New_York" }),
      ]
    );
  } catch (error) {
    console.log(error);
  }
  res.redirect("/all-blogs");
});

app.post("/updated/", async (req, res) => {
  const subject = req.body.subject;
  const blog = req.body.blog;
  const id = req.body.id;
  console.log(id);
  try {
    await db.query(
      "UPDATE blog SET blog = $1, subject = $2, time = $3 WHERE id = $4",
      [
        blog,
        subject,
        new Date().toLocaleString("en-US", {
          timeZone: "America/New_York",
        }),
        id,
      ]
    );
    res.redirect("/all-blogs");
  } catch (error) {
    console.log(error);
  }
});

app.post(
  "/login",
  passport.authenticate("local", {
    successRedirect: "/",
    failureRedirect: "/login",
  })
);

app.delete("/delete/:id", async (req, res) => {
  const id = req.params.id;
  try {
    await db.query("DELETE FROM blog WHERE id = $1", [id]);
    res.redirect("/");
  } catch (error) {
    console.log(error);
  }
});

passport.use(
  new Strategy({ usernameField: "email" }, async function verify(
    email,
    password,
    cb
  ) {
    try {
      const result = await db.query(
        "SELECT * FROM users WHERE email = $1",
        [email]
      );

      if (result.rows.length > 0) {
        const user = result.rows[0];
        bcrypt.compare(password, user.password, (error, valid) => {
          if (error) {
            console.log(error);
            return cb(error);
          } else {
            if (valid) {
              return cb(null, user);
            } else {
              return cb(null, false);
            }
          }
        });
      } else {
        console.log("no user found");
        return cb(null, false);
      }
    } catch (error) {
      console.log(error);
      return cb(error);
    }
  })
);

passport.serializeUser((user, cb) => {
  cb(null, user);
});

passport.deserializeUser((user, cb) => {
  cb(null, user);
});

app.listen(port, () => {
  console.log(`Listen on port: http://127.0.0.1:${port}`);
});

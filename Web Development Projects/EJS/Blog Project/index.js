import express from "express";
import bodyParser from "body-parser";
import session from "express-session";
import env from "dotenv";
import pg from "pg";
import bcrypt from "bcrypt";
import passport from "passport";
import { Strategy } from "passport-local";

const app = express();
const port = "3000";
const allBlogs = [];
const saltRounds = 10;
let blogID = 0;

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

app.use(
  session({
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: true,
  })
);

app.use(passport.initialize());
app.use(passport.session());

app.get("/", (req, res) => {
  if (req.isAuthenticated()) {
    res.render("index.ejs");
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
  console.log(req.user.fname)
  res.render("create.ejs", {userInfo: req.user});
});

app.get("/all-blogs", (req, res) => {
  console.log(req.user);
  res.render("all-blogs.ejs", { blogs: allBlogs });
});

app.get("/edit-blog/:id", (req, res) => {
  console.log(req.body);
  blogID = req.params.id;
  res.render("edit-blog.ejs", { post: allBlogs[blogID] });
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
          await db.query(
            "INSERT INTO users (first_name, last_name, email, password) VALUES ($1, $2, $3, $4)",
            [userInfo.first_name, userInfo.last_name, userInfo.email, hash]
          );
          res.redirect("/login");
        }
      });
    }
  } catch (error) {
    console.log(error);
  }
});

app.post("/submit", (req, res) => {
  console.log(req.body);
  const blogData = {
    id: allBlogs.length + 1,
    subject: req.body.subject,
    full_name: req.body.full_name,
    blog: req.body.blog,
    posted: new Date().toLocaleString("en-US", {
      timeZone: "America/New_York",
    }),
  };
  allBlogs.push(blogData);
  res.redirect("/all-blogs");
});

app.post("/updated/", (req, res) => {
  const blogData = {
    id: req.body.id,
    subject: req.body.subject,
    full_name: req.body.full_name,
    blog: req.body.blog,
    posted: new Date().toLocaleString("en-US", {
      timeZone: "America/New_York",
    }),
  };
  allBlogs[blogID] = blogData;
  res.redirect("/all-blogs");
});

app.post(
  "/login",
  passport.authenticate("local", {
    successRedirect: "/",
    failureRedirect: "/login",
  })
);

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
        bcrypt.compare(password, user.password, (err, valid) => {
          if (err) {
            console.log(err);
            return cb(err);
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
    } catch (err) {
      console.log(err);
      return cb(err);
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

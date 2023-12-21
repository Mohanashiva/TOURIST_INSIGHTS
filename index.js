const express = require("express");
const app = express();
const fs = require('fs');
const { Pool } = require('pg');

const touristPlacesData = require('./data/tourist_places.json');
const { User, Location, Data, Resource } = require("./models");
const bodyParser = require("body-parser");
const path = require("path");
const passport = require("passport");
const connectEnsureLogin = require("connect-ensure-login");
const session = require("express-session");
const LocalStrategy = require("passport-local");
const flash = require("connect-flash")
const bcrypt = require("bcrypt");
const { name } = require("ejs");
const saltRounds = 10;

// Set up view engine and static files
app.set("view engine", "ejs");
app.use(express.static(__dirname + '/public'));
app.set("views", path.join(__dirname, "/views"));
app.use(flash());

// Configure session
app.use(
  session({
    secret: "my-secret-super-key-12091209",
    cookie: {
      maxAge: 24 * 60 * 60 * 1000,
    },
    resave: false,
    saveUninitialized: false,
  })
);
app.use(function (request, response, next) {
  response.locals.messages = request.flash();
  next();
});

// Initialize Passport
app.use(passport.initialize());
app.use(passport.session());

// Define Passport local strategy for authentication
passport.use(new LocalStrategy({
  usernameField: 'email',
  passwordField: 'password',
}, (username, password, done) => {
  User.findOne({ where: { email: username } })
    .then(async (user) => {
      const result = await bcrypt.compare(password, user.password)
      if (result) {
        return done(null, user);
      } else {

        return done(null, false, { message: "Invalid Password" });
      }
    }).catch(() => {
      return done(null, false, { message: "Unrecognized Email_ID" });
    })
}));

// Serialize and deserialize user objects
passport.serializeUser((user, done) => {
  done(null, user.id);
});

passport.deserializeUser((id, done) => {
  User.findByPk(id)
    .then((user) => {
      done(null, user);
    })
    .catch((error) => {
      done(error);
    });
});

// Configure body parser for JSON parsing and URL-encoded parsing
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));



// Define routes for different pages
app.get("/", (req, res) => {
  res.render("index", {
    title: "Home",
  });
});

app.get("/signup", (req, res) => {
  res.render("signup", {
    title: "Signup",
  });
});

app.get("/aboutPage", (req, res) => {
  res.render("aboutPage", {
    title: "aboutPage",
  });
});

app.get("/parkahan", (req, res) => {
  res.render("index", {
    title: "index",
  });
});

app.get("/signin", (req, res) => {
  res.render("signin", {
    title: "Signin",
  });
});

// Handle user registration
app.post("/user", async (request, response) => {
  const hashedPwd = await bcrypt.hash(request.body.password, saltRounds)
  console.log(hashedPwd);
  try {
    const newUser = await User.create({
      firstName: request.body.firstName,
      lastName: request.body.lastName,
      email: request.body.email,
      password: hashedPwd
    });
    request.login(newUser, (err) => {
      if (err) {
        console.error(err);
        response.status(500).json({ error: "Internal Server Error" });
      }
      response.redirect("/home");
    }
    )
  }
  catch (error) {
    request.flash("error", "Email already exists");
    return response.redirect('/signup');
  }
}

);

// Add a route for the home page and check if the user is authenticated
app.get("/home", (req, res) => {
  if (req.isAuthenticated()) {
    // User is authenticated, render the home page
    res.render("home", {
      title: "Home Page",
      user: req.user,
      firstName: req.user.firstName, // Pass the firstName to the template
    });
  } else {
    // User is not authenticated, redirect to the sign-in page
    res.redirect("/signin");
  }
});



// Handle user login
app.post("/session", passport.authenticate('local',
  {
    failureRedirect: "/signin",
    failureFlash: true,
  }
),
  (request, response) => {
    console.log(request.user);
    response.redirect("/home");
  });

//tourist questions page 
// Route to ask tourist-related questions and collect user preferences
app.get("/home/touristP/touristQ", (req, res) => {
  res.render("touristQ", {
    title: "Tourist Questions",
  });
});

// Route to process user answers from the tourist questions form
app.post("/process-answers", async (req, res) => {
  // Extract user answers from the request body
  const { region, type } = req.body;

  // Load your JSON datasets (assuming they're arrays of objects)
  const dataset = await Data.findAll();
  const dataset2 = await Location.findAll();

  // Filter the datasets based on user preferences
  const recommendations = dataset.filter(item => {
    return item.region == region && item.type == type;
  });
  
  const recommendations2 = dataset2.filter(item => {
    return item.region == region && item.type == 'hotel';
  });

  // Combine the recommendations into a single array
  // const combinedRecommendations = [...recommendations, ...recommendations2];

  console.log(recommendations);
  console.log(recommendations2);
  const data = { recommendations, recommendations2 }

  // Pass combined recommendations data to the "/TRecommendations" route
  res.redirect(`/TRecommendations?data=${encodeURIComponent(JSON.stringify(data))}`);
});




app.post("/process-resource", async (req, res) => {
  // Extract user answers from the request body
  const { state, type } = req.body;

  // Load your JSON dataset (assuming it's an array of objects)
  const dataset = await Location.findAll()
  console.log(req.body);
  // console.log("dataset")
  console.log(state, type)
  console.log(dataset);
  // Filter the dataset based on user preferences
  const recommendations = dataset.filter(item => {
    // console.log(item.state.toLowerCase());
    return item.state == state && item.type == type;
  });
  

  console.log(recommendations)

  // console.log("recommendations")
  // console.log(recommendations)
  // Pass recommendations data to the "/TRecommendations" route
  res.redirect(`/home/touristP/RRecommendations?data=${encodeURIComponent(JSON.stringify(recommendations))}`);
});

app.get("/home/touristP/RRecommendations", async (req, res) => {
  // Retrieve recommendations data from the query parameter
  const recommendations = JSON.parse(req.query.data || '[]');
  const hotel = await Location.findAll()

  // const hotelRec = hotel.filter(item => {
  //   return item.type != "hotel";
  // });

  // Render the TRecommendations EJS template
  res.render("RRecommendations", {
    title: "Recommendations",
    recommendations: recommendations,
    // portal: hotelRec
  });
});



// Route to display recommendations based on user preferences
app.post("/TRecommendations", async (req, res) => {
  const { region, type } = req.body;

  // Load your JSON datasets (assuming they're arrays of objects)
  const dataset = await Data.findAll();
  const dataset2 = await Location.findAll();

  // Filter the datasets based on user preferences
  const recommendations = dataset.filter(item => {
    return item.region == region && item.type == type;
  });
  
  const recommendations2 = dataset2.filter(item => {
    return item.region == region && item.type == 'hotel';
  });

  // Combine the recommendations into a single array
  // const combinedRecommendations = [...recommendations, ...recommendations2];


  res.render("TRecommendations", {
    title: "Recommendations", 
    recommendations: recommendations,
    portal: recommendations2,
  });
});



// renders stakeholder page
app.get("/home/stakeholderQ", connectEnsureLogin.ensureLoggedIn(), (req, res) => {
  res.render("stakeholderQ", {
    title: "stakeholderQ page",
    user: req.user,
    userId: req.user.id,
  });
});

function ensureAuthenticated(req, res, next) {
  if (req.isAuthenticated()) {
    // User is authenticated, proceed to the next middleware
    return next();
  } else {
    // User is not authenticated, redirect to the sign-in page
    res.redirect("/signin");
  }
}

// post method for stakeholder
app.post("/hotels", ensureAuthenticated, async (request, response) => {
  try {
    console.log("Received a POST request to /hotels");
    console.log("Request body:", request.body);


    const mapsLink = request.body.link;
    if (request.body.type=='hotel') { const coordinatesMatch = mapsLink.match(/@(-?\d+\.\d+),(-?\d+\.\d+)/);
    request.body.latitude = coordinatesMatch[1];
    request.body.longitude = coordinatesMatch[2];
    }
    
    // Passport.js should have authenticated the user before reaching this route.
    // Therefore, you should have access to the user object, including the userId.
    const userId = request.user.id;

    // Create a new hotel (location) record with the associated userId
    const hotel = await Location.create({
      name: request.body.name,
      link: request.body.link,
      latitude: request.body.latitude,
      longitude: request.body.longitude,
      state: request.body.state,
      type: request.body.type,
      region: request.body.region,
      userId: userId // Set the userId to the extracted value
    });

    console.log("Hotel created:", hotel);

    // Render the "Submitted" page with the submitted hotel data
    response.render("submitted", {
      hotelName: hotel.name,
      hotelLink: hotel.link,
    });
  } catch (error) {
    console.error(error);
    response.status(500).json({ error: "Internal Server Error" });
  }
});

app.post("/posthotels", async (request, response) => {
  try {
    console.log("Received a POST request to /hotels");
    console.log("Request body:", request.body);
    
    const hotel = await Location.bulkCreate(request.body);


    console.log("Hotel created:", hotel);

    // Render the "Submitted" page with the submitted hotel data
    response.send( { data:hotel });
  } catch (error) {
    console.error(error);
    response.status(500).json({ error: "Internal Server Error" });
  }
});







app.get("/submitted", ensureAuthenticated, (req, res) => {
  // Assuming you have access to the user's submitted hotel data
  // Retrieve the hotel name and link from wherever you stored it
  const hotelName = hotel.name; // Replace with the actual hotel name
  const hotelLink = hotel.link; // Replace with the actual hotel link

  // Render the "Submitted" page with the hotel data
  res.render("submitted", {
    hotelName: hotelName,
    hotelLink: hotelLink,
  });
});



app.get("/getUsers", async (request, response) => {

  console.log("login.body")
  try {
    const hotel = await User.findAll()
    console.log(hotel)
    response.send(hotel)
  } catch (error) { }
})

app.get("/random", (req, res) => {
  // User is authenticated, render the home page  
  res.render("random", {
    title: "random",
    user: req.user,
    firstName: req.user.firstName, // Pass the firstName to the template
  });
});

// Handle user logout
app.get("/signout", (request, response, next) => {
  request.logout((err) => {
    if (err) {
      return next(err);
    }
    response.redirect("/");
  });
});

app.get("/data", async (request, response) => {

  console.log("login.body")
  try {
    const hotel = await Data.findAll()
    console.log(hotel)
    response.send(hotel)
  } catch (error) { }
})




app.post("/data", async (request, response) => {
  try {
    const data = await Data.bulkCreate(request.body);


    console.log(data);


    response.status(200).json(data);
  } catch (error) {
    console.error(error);
    response.status(500).json({ error: 'Internal Server Error' });
  }
});

//view all hotels 
app.get('/hotels', ensureAuthenticated, async (req, res) => {
  try {
    // Retrieve the logged-in user's ID from the user object
    const loggedInUserId = req.user.id;
    
    // Fetch hotels associated with the logged-in user
    const hotels = await Location.findAll({
      where: {
        userId: loggedInUserId,
      },
    });

    // Render the 'viewHotels' page with the user's hotels
    res.render('viewHotels', { hotels });
  } catch (error) {
    console.error('Error fetching hotel data:', error);
    console.log('User object:', req.user);
    
    // Handle any errors that occur during fetching
    res.status(500).send('Internal Server Error');
  }
});




app.get('/gethotels', async (req, res) => {
  try {
    // Retrieve the logged-in user's ID from the user object

    // Fetch hotels associated with the logged-in user
    const hotels = await Location.findAll();

    // Render the 'viewHotels' page with the user's hotels
    res.send({ hotels });
  } catch (error) {
    console.error('Error fetching hotel data:', error);
    console.log('User object:', req.user);
    
    // Handle any errors that occur during fetching
    res.status(500).send('Internal Server Error');
  }
});

app.delete("/hotel/:id", async function (request, response) {
  console.log("We have to delete a Todo with ID: ", request.params.id);
  const { id } = request.params;

  try {
    const result = await pool.query('DELETE FROM "\Locations\" WHERE id = $1', [id]);
    response.status(200).json({ message: 'Record deleted successfully' });
    console.log(result);
  } catch (error) {
    console.error('Error deleting record:', error);
    response.status(500).json({ error: 'Internal Server Error' });
  }

});

//render tourist  prespectives
app.get("/home/touristP", (req, res) => {
  res.render("touristP", {
    title: "touristP",
  });
});


const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'database_development',
  password: 'password',
  port: 5432,
});


app.get("/home/touristP/resourceQ", (req, res) => {
  res.render("resourceQ", {
    title: "resource questions",
  });
});

//resource post
app.post("/resource", async (request, response) => {
  try {

    const data = await Resource.bulkCreate(request.body);
    console.log(data);

    response.status(200).json(data);
  } catch (error) {
    console.error(error);
    response.status(500).json({ error: 'Internal Server Error' });
  }
});


app.get("/resource", async (request, response) => {

  console.log("resource.get")
  try {
    const resource = await Resource.findAll()
    console.log(resource)
    response.send(resource)
  } catch (error) { }
})

app.delete("/resource/:id", async function (request, response) {
  console.log("We have to delete a resource with ID: ", request.params.id);
  const { id } = request.params;

  try {
    const result = await pool.query('DELETE FROM "\Resources\" WHERE id = $1', [id]);
    response.status(200).json({ message: 'Record deleted successfully' });
    console.log(result);
  } catch (error) {
    console.error('Error deleting record:', error);
    response.status(500).json({ error: 'Internal Server Error' });
  }

});

// Start the server
app.listen(4000, () => {
  console.log("Server is running on port 5000");
});
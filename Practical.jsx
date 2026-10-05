

// pr 6
/*Q1- create database (npm install mongodb, use college, db.student.find())
const { MongoClient } = require("mongodb");

const url = "mongodb://localhost:27017";
const client = new MongoClient(url);

async function run() {
  await client.connect();
  console.log("Connected to MongoDB");

  const db = client.db("college");
  await db.createCollection("students");
  console.log("Database and collection created");

  const students = db.collection("students");

  await students.insertOne({ name: "Kunal", age: 20, marks: 85 });

  await students.insertMany([
    { name: "Aman", age: 21, marks: 78 },
    { name: "Riya", age: 19, marks: 92 },
  ]);
  console.log("Data inserted");

  const result = await students.find().toArray();
  console.log(result);

  await client.close();
}

run();
*/






//Q2 - /component/AddItem.jsx
/*
import { useState } from "react";

function AddItem() {
  const [input, setInput] = useState("");
  const [items, setItems] = useState([]);

  const add = () => {
    if (input === "") return;
    setItems([...items, input]);
    setInput("");
  };

  return (
    <div>
      <input value={input} onChange={(e) => setInput(e.target.value)} />
      <button onClick={add}>Add</button>

      <ul>
        {items.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
}

export default AddItem;

//app.js
import AddItem from "./Components/AddItem";

function App() {
  return <AddItem />;
}

export default App;
*/






//Pr 7 - useState 
/*Q1
import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h1>Count: {count}</h1>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <button onClick={() => setCount(count - 1)}>Decrement</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  );
}

export default Counter;

//app.js
import Counter from "./Components/Counter";

function App() {
  return <Counter />;
}

export default App;
*/












/*Q2- increment decrement
import { useReducer } from "react";

function reducer(state, action) {
  switch (action.type) {
    case "increment":
      return { count: state.count + 1 };
    case "decrement":
      return { count: state.count - 1 };
    case "reset":
      return { count: 0 };
    default:
      return state;
  }
}

function CounterReducer() {
  const [state, dispatch] = useReducer(reducer, { count: 0 });

  return (
    <div>
      <h1>Count: {state.count}</h1>
      <button onClick={() => dispatch({ type: "increment" })}>Increment</button>
      <button onClick={() => dispatch({ type: "decrement" })}>Decrement</button>
      <button onClick={() => dispatch({ type: "reset" })}>Reset</button>
    </div>
  );
}

export default CounterReducer;

import CounterReducer from "./Components/CounterReducer";

function App() {
  return <CounterReducer />;
}

export default App;
*/





//Q3- login and logour 
/*
import { useReducer } from "react";

function reducer(state, action) {
  switch (action.type) {
    case "login":
      return { isLoggedIn: true };
    case "logout":
      return { isLoggedIn: false };
    default:
      return state;
  }
}

function Login() {
  const [state, dispatch] = useReducer(reducer, { isLoggedIn: false });

  return (
    <div>
      <h1>Status: {state.isLoggedIn ? "User Logged In" : "User Logged Out"}</h1>
      <button onClick={() => dispatch({ type: "login" })}>Login</button>
      <button onClick={() => dispatch({ type: "logout" })}>Logout</button>
    </div>
  );
}

export default Login;

//app.js
import Login from "./Components/Login";

function App() {
  return <Login />;
}

export default App;
*/



//pr 8
/*Q1 - API data and render
import { useState, useEffect } from "react";

function UserList() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((res) => res.json())
      .then((data) => setUsers(data));
  }, []);

  return (
    <div>
      <h1>User List</h1>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            {user.name} - {user.email}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default UserList;

import UserList from "./Components/UserList";

//app.js
function App() {
  return <UserList />;
}

export default App;
*/


/* Q2- parent and salary component
function Employee(props) {
  return (
    <div>
      <h2>Employee Data</h2>
      <p>ID: {props.id}</p>
      <p>Name: {props.name}</p>
      <p>Department: {props.department}</p>
    </div>
  );
}

function Salary(props) {
  return (
    <div>
      <h2>Salary Data</h2>
      <p>Salary: {props.salary}</p>
    </div>
  );
}

function EmployeeComponent() {
  const emp = {
    id: 101,
    name: "Kunal",
    department: "IT",
    salary: 60000,
  };

  return (
    <div>
      <h1>Parent Component</h1>
      <Employee id={emp.id} name={emp.name} department={emp.department} />
      <Salary salary={emp.salary} />
    </div>
  );
}

export default EmployeeComponent;

//app.js
import EmployeeComponent from "./Components/EmployeeComponent";

function App() {
  return <EmployeeComponent />;
}

export default App;
*/



/* Q3 - create 5 components
import { createContext, useContext } from "react";

const EmpContext = createContext();

function Component5() {
  const emp = useContext(EmpContext);
  return (
    <div>
      <h3>Component 5 (uses context)</h3>
      <p>Salary: {emp.salary}</p>
    </div>
  );
}

function Component4() {
  return (
    <div>
      <h3>Component 4 (no data)</h3>
      <Component5 />
    </div>
  );
}

function Component3() {
  const emp = useContext(EmpContext);
  return (
    <div>
      <h3>Component 3 (uses context)</h3>
      <p>ID: {emp.id}</p>
      <p>Name: {emp.name}</p>
      <p>Department: {emp.department}</p>
      <Component4 />
    </div>
  );
}

function Component2() {
  return (
    <div>
      <h3>Component 2 (no data)</h3>
      <Component3 />
    </div>
  );
}

function Component1() {
  const emp = {
    id: 101,
    name: "Kunal",
    department: "IT",
    salary: 60000,
  };

  return (
    <EmpContext.Provider value={emp}>
      <h2>Component 1 (creates context)</h2>
      <Component2 />
    </EmpContext.Provider>
  );
}

export default Component1;

//app.js
import Component1 from "./Components/Components";

function App() {
  return <Component1 />;
}

export default App;
*/


//pr9
/* Q1 - lifecycle method
import React, { Component } from "react";

class Lifecycle extends Component {
  state = { color: "red" };

  componentDidMount() {
    setTimeout(() => {
      this.setState({ color: "yellow" });
    }, 5000);
  }

  render() {
    return <h1>My favourite color is {this.state.color}</h1>;
  }
}

export default Lifecycle;

//app.js
import Lifecycle from "./Components/Lifecycle";

function App() {
  return <Lifecycle />;
}

export default App;
*/





//Q2- unmounting in react
/*
import React, { Component } from "react";

class Child extends Component {
  componentWillUnmount() {
    alert("Component is unmounted");
  }

  render() {
    return <h1>Child Component is visible</h1>;
  }
}

class Unmount extends Component {
  state = { show: true };

  render() {
    return (
      <div>
        {this.state.show && <Child />}
        <button onClick={() => this.setState({ show: false })}>
          Delete Component
        </button>
      </div>
    );
  }
}

export default Unmount;

//app.js
import Unmount from "./Components/Unmount";

function App() {
  return <Unmount />;
}

export default App;
*/

/*
/*Q1] Create three pages: Home, About, and Contact using React Router. Configure routes to navigate between the three pages. 
//Code:  Home.js
function Home() { 
return ( 
<div> 
<h1>Home Page</h1> 
<p>Welcome to our website!</p> 
</div> ); 
}
export default Home; 

//Code: Contact.js
function Contact() { 
return ( 
<div> 
<h1>Contact Page</h1> 
<p>Contact us on example@gmail.com</p> 
</div> 
); 
}
export default Contact; 

//Code: About.js
function About() { 
return ( 
<div> 
<h1>About Page</h1> 
<p>This is the about page</p> 
</div> 
); 
}
export default About; 

//Code:App.js
import { BrowserRouter, Routes, Route, Link } from "react-router-dom"; 
import Home from "./Home"; 
import About from "./About"; 
import Contact from "./Contact"; 
function App() { 
return ( 
<BrowserRouter> 
<nav> 
<Link to="/">Home</Link> |{" "} 
<Link to="/about">About</Link> |{" "} 
<Link to="/contact">Contact</Link> 
</nav> 
<Routes> 
<Route path="/" element={<Home />} /> 
<Route path="/about" element={<About />} /> 
<Route path="/contact" element={<Contact />} /> 
</Routes> 
</BrowserRouter> 
);} 
export default App; 

//folder:react->reactapp->src(save all react file here,app.js also)->open cmd->npm start

//Q2] Create a navigation bar using Link or NavLink for Home, Products, About, and Contact. 

//Code:Navbar.js 
import { NavLink } from "react-router-dom"; 
function Navbar() { 
return ( 
<nav> 
<NavLink 
to="/" 
className={({ isActive }) => (isActive ? "active" : "")}> 
Home 
</NavLink> 
<NavLink 
to="/products" 
className={({ isActive }) => (isActive ? "active" : "")}> 
Products 
</NavLink> 
<NavLink 
to="/about" 
className={({ isActive }) => (isActive ? "active" : "")}> About 
</NavLink> 
<NavLink 
to="/contact" 
className={({ isActive }) => (isActive ? "active" : "")}> Contact </NavLink> 
</nav>)}; 
export default Navbar; 

//code:App.js
import { BrowserRouter, Routes, Route } from "react-router-dom"; 
import Navbar from "./Navbar"; 
import Home from "./Home"; 
import About from "./About"; 
import Contact from "./Contact"; 
function Products() { 
return ( 
<div> 
<h1>Products Page</h1> 
<p>Welcome to our products page!</p> 
</div>
)}; 
function App() { 
return ( 
<BrowserRouter> 
<Navbar /> 
<Routes> 
<Route path="/" element={<Home />} /> 
<Route path="/products" element={<Products />} /> 
<Route path="/about" element={<About />} /> 
<Route path="/contact" element={<Contact />} /> 
</Routes> 
</BrowserRouter>);} 
export default App; 

//code:Index.css
nav { display: flex; 
gap: 20px; 
padding: 20px; 
background-color: #222;
} 
nav a { 
color: white; 
text-decoration: none; 
} 
nav a.active { 
color: yellow; 
font-weight: bold; 
border-bottom: 2px solid yellow; 
} 

//Q3] Create a NotFound component that displays “404 - Page Not Found”. Display it whenever the user enters an invalid URL. 

//Code: NotFound.js 
function NotFound() { 
return ( 
<div> 
<h1>404 - Page Not Found</h1> 
<p>Sorry, the page you are looking for does not exist.</p> 
</div> ); 
} 
export default NotFound; 

//Code:App.js 
import { BrowserRouter, Routes, Route } from "react-router-dom"; 
import Navbar from "./Navbar"; 
import Home from "./Home"; 
import About from "./About"; 
import Contact from "./Contact"; 
import NotFound from "./NotFound"; 
function Products() { 
return ( 
<div> 
<h1>
Products Page
</h1> 
<p>Welcome to our products page!</p> 
</div>)}; 
function App() { 
return ( 
<BrowserRouter> 
<Navbar /> 
<Routes> 
<Route path="/" element={<Home />} /> 
<Route path="/products" element={<Products />} /> 
<Route path="/about" element={<About />} /> 
<Route path="/contact" element={<Contact />} /> 
<Route path="*" element={<NotFound />} /> 
</Routes> 
</BrowserRouter>);} 

//Q4] Create a nested route of your choice with two child routes. Use the <Outlet /> component to render the child routes. 

//Code: Products.js 
import { Outlet, NavLink } from "react-router-dom"; 
function Products() {   
return (     
<div>       
<h1>Products</h1>       
<NavLink to="electronics">Electronics</NavLink>{" | "}       
<NavLink to="clothing">Clothing</NavLink>       
<Outlet />     
</div>   
);} 
export default Products; 

//Electronics.js 
function Electronics() {   
return (     
<div>       
<h2>Electronics</h2>       
<p>Mobile phones, laptops and other electronic items.</p>     
</div>   
);} 
export default Electronics; 

//Clothing.js 
function Clothing() {   
return (     
<div>       
<h2>Clothing</h2>       
<p>Shirts, jeans, jackets and other clothing items.</p>     
</div>   
);} 
export default Clothing; 
*/

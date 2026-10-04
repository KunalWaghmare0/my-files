// src/components/Parent.jsx
/*import React, { Component } from "react";
import Child from "./Child";

class Parent extends Component {
  state = { age: 50 };

  render() {
    return (
      <div>
        <h1>This is Parent Class {this.props.address}</h1>
        <Child p_name="Parent Name" p_age={this.state.age} />
      </div>
    );
  }
}

export default Parent;
*/




















/* src/components/Child.jsx:
import React, { Component } from "react";

class Child extends Component {
 render() {
    return (
      <p>{this.props.p_name} - {this.props.p_age}</p>
    );
  }
}

export default Child;
*/


/* src/App.jsx
import Parent from "./Components/Parent";

function App() {
  return <Parent address="Mumbai" />;
}

export default App;
*/











/* Q2 parent.jsx only one code
function Child(props) {
  return (
    <div>
      <p>Name: {props.name}</p>
      <p>Age: {props.age}</p>
    </div>
  );
}

function Parent() {
  return (
    <div>
      <Child name="Kunal" age={21} />
    </div>
  );
}

export default Parent;
*/




/* Q3
import React, { Component } from "react";

class Parent extends Component {
  state = {
    message: "Hello World!"
  };

  updateMessage = () => {
    this.setState({
      message: "Message Updated!"
    });
  };

  render() {
    return (
      <div>
        <h2>{this.state.message}</h2>

        <button onClick={this.updateMessage}>
          Update Message
        </button>
      </div>
    );
  }
}

export default Parent;
*/






/*Q4
import React, { Component } from "react";

class Counter extends Component {
  state = { count: 0 };

  render() {
    return (
      <div>
        <h1>Count: {this.state.count}</h1>
        <button onClick={() => this.setState({ count: this.state.count + 1 })}>
          Increment
        </button>
        <button onClick={() => this.setState({ count: this.state.count - 1 })}>
          Decrement
        </button>
        <button onClick={() => this.setState({ count: 0 })}>
          Reset
        </button>
      </div>
    );
  }
}

export default Counter;
*/

/*
import Counter from "./Parent";

function App() {
  return <Counter />;
}

export default App;
*/



//pr 3
/*
//1. Reading contents of file in synchronous way. 
//CODE: Read.js 
const fs=require("fs") 
const a=fs.readFileSync('./sample.txt',"utf-8") 
console.log(a) 




//2.Reading Content of File In Asynchronous way. 
//CODE: Async.js 
const fs = require("fs"); 
fs.readFile("./sample.txt", "utf-8", (error, data) => { 
if (error) { 
throw new Error("Error reading file!"); 
} 
console.log(data); 
}); 












//3. Read a file content in Async() function. 
const fs = require("fs/promises"); 
async function readFileContent() {
try { 
const data = await fs.readFile("./example.txt", "utf-8"); 
console.log(data); 
} catch (error) { 
console.error("Error reading file!"); 
} 
} 
readFileContent();  














//4.Writing a file 
//a. Create a  file example.txt 
//b. Add some content to it and read the file 
//c. Append data to file 
//d. Rename the file 
//e. Read the file again after appending 
//f. Delete the file 
const fs=require('fs/promises') 
const writeFunct=async()=>{ 
try{ 
const d=await fs.readFile('example.txt','utf-8');
console.log(d) 
await fs.writeFile('example.txt','writing in a file',"utf-8") 
await fs.appendFile('example.txt','\n data append via node.js',"utf-8") 
await fs.rename('example.txt','NewWrite.txt') 
const data=await fs.readFile('NewWrite.txt',"utf-8") 
console.log(data) 
}catch(err){
throw err
} } 
writeFunct() 
*/





//Pr 4
/*
Q1.Create a node.js module that allows users to input text via command line .Once the user enters text,the program should save the input into a file named text.txt.  Additionally,the program should emit a custom event indicating that the text is ready for processing. 

CODE: 
const fs=require('fs');//fs=filesystem module 
const readline=require('readline'); 
const EventEmitter=require('events'); 
const eventEmitter= new EventEmitter(); 
const rl=readline.createInterface( 
{ 
input:process.stdin, 
output:process.stdout 
} 
); 
function handleInput(input){ 
eventEmitter.emit('textReady',input); 
} 
eventEmitter.on('textReady',(text)=> 
{ 
console.log(`Custom event Fired :Text is ready - ${text}`); fs.writeFile('text.txt',text,(err)=>{ 
if (err) throw err; 
console.log("Text has been saved to text.txt"); 
rl.close(); 
}); 
}); 
rl.question('Enter some text:',(text)=> 
{handleInput(text); 
});






//Q2. Create emitEmitter() instance to call factorial of a number.   
CODE: 
const readline = require('readline'); 
const EventEmitter = require('events'); 
const eventEmitter = new EventEmitter(); 
const rl = readline.createInterface( 
{     
input: process.stdin,     
output: process.stdout 
} 
); 
function handleInput(input) 
{     
eventEmitter.emit('findFactorial', input); 
} 
eventEmitter.on('findFactorial', (num) => 
{     
let fact = 1;      
for (let i = 1; i <= num; i++)
{         
fact = fact * i;     
}     
console.log(`Factorial of ${num} is ${fact}`);     
rl.close(); 
}); 
rl.question('Enter a number: ', (number) => {     
handleInput(Number(number)); 
}); 
*/




/*
//pr-5
Q1 Create a simple Node.js Program that creates an HTTP server and handles it.
CODE: 
const http = require('http'); 
const hostname = '127.0.0.1'; 
const port = 4000; 
const server = http.createServer((req, res) => {     
res.writeHead(200, { 'Content-Type': 'text/plain' });     
if (req.url === '/hello') {         
res.end('Hello World!\n');     
}      
else if (req.url === '/about') {         
res.end('This is the about page.\n');     
}      
else {         
res.end('Node.js Server!!\n');     
} 
}); 
server.listen(port ,hostname,()=> {     
console.log("Server running at http://${hostname}:{$port}/"); 
}); 








Q2. Create a Node.js program using Express that serves a list of users from a JSON file. 
a. Display details of all users 
b. Display details based on its parameters such as id 
Users.json 
[
{"id":101,"name":"Alice","age":18}, 
{"id":102,"name":"Isha","age":20}, 
{"id":103,"name":"Ojasa","age":18}, 
{"id":104,"name":"Ritu","age":21}, 
{"id":105,"name":"Ananya","age":20}, 
{"id":106,"name":"John","age":19} 
]

Users.js 
const fs = require('fs'); 
const express = require('express'); 
const port = 8000; 
const app = express(); 
let users = JSON.parse(fs.readFileSync('./users.json')); app.get('/api/v1/users', (req, res) => { 
res.json(users); 
}); 
app.get('/api/v1/users/:id', (req, res) => { 
let id = req.params.id * 1; 
const find_user = users.find(e1 => e1.id === id) res.status(200).json(find_user) 
if(!find_user){ 
return res.status(404).json({ 
"status":"FAILED", 
"message":"could not find user" 
}) 
} 
res.status(200).json(find_user); 
}) 
app.listen(port,()=>{ 
console.log('Server Running') 
}); 
note: install express module
npm install express
get:http://localhost:8000/api/v1/Users/101
get:http://localhost:8000/api/v1/Users
C:\>node pr5q1.js
server running at http://${hostname}:{$port}/
install an extension thunder client for http module
get:127.0.0.1:4000
get:127.0.0.1:4000/hello
get:127.0.0.1:4000/about*/

*/



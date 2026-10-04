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




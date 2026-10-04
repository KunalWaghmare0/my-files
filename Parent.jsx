import React, { Component } from "react";
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


















/*
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





/*
import Parent from "./Components/Parent";

function App() {
  return <Parent address="Mumbai" />;
}

export default App;
*/
import React, {Component} from 'react';
import {PropTypes} from 'prop-types';
import Checkbox from '@material-ui/core/Checkbox';

class Filter extends Component {
    constructor(props){
    super(props);
    this.state = {name:true,age:false};
    this.handleChange=this.handleChange.bind(this);
  }
handleChange = name => event => {
    if (name == "name"){
        this.setState({ [name]: event.target.checked,age: false});
    }

    if (name == "age"){
        this.setState({ [name]: event.target.checked,name: false});
    }
    this.props.changeFilter(name,event.target.checked);

};

    render() {
        return (
        <div className="checkboxes">
            <Checkbox name ="name" checked={this.state.name}
          onChange={this.handleChange("name")}
          value="name"/>
            <label>Name</label>

            <Checkbox name="age" checked={this.state.age}
          onChange={this.handleChange("age")}
          value="age"/>
            <label>Age</label>
        </div>
        );
    }
}

export default Filter;
import React, {Component} from 'react';
import Filter from './components/Filter';
import RecordTable from './components/RecordTable';

class App extends Component {

constructor(props){
    super(props);
    this.state = {name:true,age:false};
    this.filterData = this.filterData.bind(this);
  }
filterData(filterName,val){
	if (filterName=="name"){
		this.setState({name:val,age:false});

	}
	if (filterName=="age"){
		this.setState({age:val,name:false});

	}

}
  render() {
    return (
      <div className="container-fluid">
        <center><h1>Birthday Records</h1></center>
        <Filter changeFilter={this.filterData}></Filter>
        <RecordTable age={this.state.age} name={this.state.name}></RecordTable>
      </div>
    );
  }
}

export default App;

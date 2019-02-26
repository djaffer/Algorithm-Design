import React, {Component} from 'react';
import {PropTypes} from 'prop-types';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

class RecordTable extends Component {

    constructor(props) {
        super(props);
        this.people = [
            {
                name: "Veronica Mize",
                dob: "11/29/2011"
            }, {
                name: "Cecilia Olsson",
                dob: "09/16/1992"
            }, {
                name: "Peter Parker",
                dob: "01/16/1992"
            }, {
                name: "Jimmy Shergil",
                dob: "12/12/2001"
            }, {
                name: "Alexander Alfred",
                dob: "02/09/1891"
            }, {
                name: "Janice Shroyer",
                dob: "12/01/1982"
            }, {
                name: "Ralph White",
                dob: "11/30/2011"
            }, {
                name: "Deborah T. Decker",
                dob: "10/31/1999"
            }
        ];
    }
    renderData(){
        if (this.props.name){
            this.people.sort(function(a, b){

                if (a.name<b.name){
                    return -1;
                }else if(a.name==b.nage){
                    return 0;
                } else{
                    return 1;
                }

                });
        }
        if (this.props.age){
            this.people.sort(function(a, b){

                return new Date(a.dob) - new Date(b.dob);

                });
            

        }
        
        return this.people.map((person,index)=>{
            return (<TableRow key={index}>
                    <TableCell>{person.name}</TableCell>
                    <TableCell>{person.dob}</TableCell>
                    </TableRow>
                    )
        });
        
    }
    render() {
        return (
            <Paper className="width">
                <Table>
                    <TableHead>
                        <TableRow>
                            <TableCell className="table-header">Name</TableCell>
                            <TableCell className="table-header">Date of Birth</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                                {this.renderData()}
                    </TableBody>
                </Table>
            </Paper>
        );
    }
}

export default RecordTable;

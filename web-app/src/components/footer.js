import React, {Component} from 'react';
// import  

class Footer extends Component {

    changed(){
        console.log('changed')
    }

    render() {
        return (
        <div>
        <h2 onClick={this.props.myalert}>
            {this.props.trademark}
        </h2>
        <input onChange = {this.change} type='text'/>
        </div>
        )
    }
}
export  default Footer;
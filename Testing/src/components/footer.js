import React, {Component} from 'react';
import  {CtxConsumer} from '../index';

class Footer extends Component {
    
    state = {
        name:'asdsa',
        age: 34,
        isLogin: true
    }

    componentDidMount() {
        this.setState({name:'Myane'})
    }
    changed = evt => {
        // console.log('changed')
        // console.log(this.state.name)
        console.log('changed',evt.target.value)
        this.setState({name:evt.target.value})
    }

    render() {
        // const animals = ['cat','dog'];
        return (
            <CtxConsumer>
                {(context) => (
                <div>
                {context.animals.map(animal => {
                    return (
                        <div key={animal}>
                            <h1>{animal}</h1>
                            <h1>{animal}</h1>
                        </div>
                    );
                })} 
                </div>

                )}

            </CtxConsumer>
        )
        // return (
        //     <div>
        
        //     {this.state.isLogin ? (    
        //     <React.Fragment>
        //     <h2 onClick={this.props.myalert}>
        //         {this.props.trademark}
        //     </h2>
        //     <input value = {this.state.name}
        //     onChange = {this.changed} type='text'/>
        //     </React.Fragment>
        // ):(    
        //     <React.Fragment>
        //     <h2>You cant see this content</h2>
        //     <h2>You must Login</h2>
        //     </React.Fragment>
        // )}
        //     </div>
        // )
    }
}
export  default Footer;
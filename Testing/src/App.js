// import logo from './logo.svg';
import './App.css';
import Header from './components/header';
import Footer from './components/footer';
import Numbers from './components/numbers';
import styled from 'styled-components';

function createAlert() {
  alert('Hello. You clicked');

}

function ShowMessage(props){

  if(props.toShow) {
    return <h2>My message</h2>

  } else {
    return <h2>Forbidden</h2>
  }
}

const pStyle = {
  fontSize: '2em',
  color: 'red',
}

// this does not work
const Paragraph = styled.p`

font-size: 5em;
color:green;
`;

function App() {
  return (
    <div className="App">
      <Numbers></Numbers>
      <Header info='This is MY message'/>
      <Header info='This is header'/>
      <p style = {pStyle}>main content</p>
      <Paragraph>New styled</Paragraph>
      <Footer trademark='page by Henry'
        myalert = {createAlert}/>
        <ShowMessage toShow={false}/>
    </div>
  );
}

function OurText() {
  return <p>This is our text</p>
}

export default App;

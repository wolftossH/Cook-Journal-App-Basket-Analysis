// import logo from './logo.svg';
import './App.css';
import Header from './components/header';
import Footer from './components/footer';

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

function App() {
  return (
    <div className="App">
      <Header info='This is MY message'/>
      <Header info='This is header'/>
      <p>main content</p>
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

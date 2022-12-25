import logo from './logo.svg';
import './App.css';
import Header from './components/header';
import Footer from './components/footer';


function createAlert() {
  alert('Hello. You clicked');

}

function App() {
  return (
    <div className="App">
      <Header info='This is MY message'/>
      <Header info='This is header'/>
      <p>main content</p>
      <Footer trademark='page by Henry'
        myalert = {createAlert}/>
    </div>
  );
}

function OurText() {
  return <p>This is our text</p>
}

export default App;

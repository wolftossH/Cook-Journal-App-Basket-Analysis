import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {Route, Routes, BrowserRouter} from 'react-router-dom';
import Header from './components/header';

const context = React.createContext();
export const CtxConsumer = context.Consumer;
// const ctxProvider = context.Provider;

const animals = ['elephant', 'lion']

const routing = ReactDOM.createRoot(document.getElementById('root'));
routing.render(
  <BrowserRouter>
  <context.Provider value={{animals:animals}}>
  <div>
    <Routes>    
      <Route path="/" element={<App/>}/>
      <Route path="/movies" element={<Header/>}/>
    </Routes>
    </div>
  </context.Provider>

  </BrowserRouter>
);

// const routing = (
//   <BrowserRouter>
//     <div>
//       <Route exact path="/" element={<App/>}/>
//       <Route path="/movies" element={<Header/>}/>
//     </div>
//   </BrowserRouter>
// )

// ReactDOM.render(
//   routing,
//   document.getElementById('root')
// );


// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>
// );

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

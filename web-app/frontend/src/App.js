import {useEffect, useState} from 'react';
import axios from 'axios';
import {format} from 'date-fns';

import './App.css';

const baseUrl = 'http://localhost:5000'

const handleChange = e => {
  setDescription(e.target.value);
}

function App() {

  const[description, setDescription] = useState('');

  return (
    <div className="App">
      <header className="App-header">
        <form>
          <label htmlFor='description'>Description</label>
          <input
            onChange={handleChange}
            type='text'
            name='description'
            id = 'description'
            value = {description}
          />
        </form>
      </header>
    </div>
  );
}

export default App;

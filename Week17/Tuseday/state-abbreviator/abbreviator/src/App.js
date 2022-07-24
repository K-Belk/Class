import './App.css';
import React, {useState} from 'react'
import states from './statedata';
import StateAbberv from './components/stateAbberv';

function App() {

  const stateData = states
  
  const [abv, setAbv] = useState('AL')

  const handleChange = (event) => {
    setAbv(event.target.value)
  }

  return (
    <div className="App">
      <header className="App-header">
        <label>
          All States
          <select value={abv} onChange={handleChange}>
            {stateData.map((stateData) => (
              <option key={stateData['alpha-2']} value={stateData['alpha-2']}>{ stateData.name }</option> ))}
          </select>
        </label>
              <StateAbberv state={abv} />
      </header>
    </div>
  );
}

export default App;

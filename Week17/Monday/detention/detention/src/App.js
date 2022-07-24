
import './App.css';
import Statement from './components/statement';

function App() {

  const multiStatement = () => {
    const statementArr = [];
    for (let i=0; i < 100; i++) {
      statementArr.push(<Statement key= />)
  }
  return statementArr
  }

  return (
    <div className="App">
      { multiStatement()}
    </div>
  );
};

export default App;

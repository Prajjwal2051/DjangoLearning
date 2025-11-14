import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import TrainerList from './components/TrainerList';
import TrainerDetail from './components/TrainerDetail';
import './App.css';

function App() {
  return (
    <Router>
      <div className="app">
        <Header />
        <main className="container">
          <Routes>
            <Route path="/" element={<TrainerList />} />
            <Route path="/trainers" element={<TrainerList />} />
            <Route path="/trainers/:id" element={<TrainerDetail />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
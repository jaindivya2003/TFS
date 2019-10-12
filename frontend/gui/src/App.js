import React from 'react';
import logo from './logo.svg';
import './App.css';
import 'antd/dist/antd.css'; // or 'antd/dist/antd.less'

import CustomLayout from './containers/Layout'

function App() {
  return (
    <div className="App">
    <CustomLayout>
    </CustomLayout>
    </div>
  );
}

export default App;

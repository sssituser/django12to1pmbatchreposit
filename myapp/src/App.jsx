import {Routes,Route,Link} from 'react-router-dom'
import React from "react";
import EmployeeList from './components/EmployeeList';
import AddEmployee from './components/AddEmployee';
import EditEmployee from './components/EditEmployee';
import FindEmployee from './components/FindEmployee';
export default function App(){
  return(
    <React.Fragment>
      
      <Routes>
        <Route path='/' element={<EmployeeList/>} />
        <Route path='/add' element={<AddEmployee/>} />
        <Route path='/edit/:id' element={<EditEmployee/>} />
        <Route path='/find/:id' element={<FindEmployee/>} />
      </Routes>
    </React.Fragment>
  )
}

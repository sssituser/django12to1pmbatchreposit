import React, { useState } from 'react'
import {Link} from 'react-router-dom'
import axios from 'axios'
import { useNavigate } from 'react-router-dom';
function AddEmployee() {
  
  let navigate=useNavigate();

  let[employee,setEmployee]=useState({
    ename:"",
    esal:"",
    email:"",
    eimage:""
  });
  function updateInput(event){
    setEmployee({
      ...employee,
      [event.target.name]:event.target.value
    })
  }
  function save(event){
    event.preventDefault()
      axios.post("http://localhost:9000/employees",employee)
      .then(()=>{
        alert("Record added successfully.")
        navigate('/')
      })
      .catch((error)=>{
        alert(error)
      })
  }
  return (
   <React.Fragment>
    <div className="container">
     <p className="h1 text-center text-secondary">AddEmployee</p>
   
     <div className="row mt-5">
      <div className="col-md-5">
        <div className="card">
          <div className="card-header bg-primary text-white text-center">
            <p className="h2">Regiser Here</p>
          </div>
          <div className="card-body">
            <form action="" onSubmit={save}>
              <div className="form-group">
                <input type="text" name='ename' onChange={updateInput} value={employee.ename} placeholder='Employee Name' className='form-control'/>
              </div>
              <div className="form-group">
                <input type="text" name='esal' onChange={updateInput} value={employee.esal} placeholder='Employee Salary' className='form-control'/>
              </div>

               <div className="form-group">
                <input type="text" name='email' onChange={updateInput} value={employee.email} placeholder='Employee Email ID' className='form-control'/>
              </div>
              <div className="form-group">
                <input type="text" name='eimage' onChange={updateInput} value={employee.eimage} placeholder='Employee Image URL' className='form-control'/>
              </div>
              <button className='btn btn-primary btn-sm'>AddEmployee</button>
              <Link to='/' className='btn btn-sm btn-success float-right'>Back</Link>
            </form>
          </div>

        </div>
      </div>
     </div>
   </div>
   </React.Fragment>
  )
}

export default AddEmployee
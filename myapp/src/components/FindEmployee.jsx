import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import { Link } from 'react-router-dom';
function FindEmployee() {
  let {id} = useParams()
  let[employee,setEmployee]=useState({});
  useEffect(()=>{
    axios.get(`http://localhost:9000/employees/${id}`)
    .then((res)=>{
      setEmployee(res.data)
    })
    .catch((error)=>{
      alert(error)
    })

  },[]);
  return (
   <React.Fragment>
      <p className="h1 text-center text-secondary">Find Employee:{id} </p>
      <div className="container">
        <div className="row">
          <div className="col">
            <div className="card">
              <div className="card-header bg-primary text-white text-center">
                  <p className="h1">Employee Detials</p>
              </div>
              <div className="card-body">
                <div className="row">
                  <div className="col-md-4">
                    <img src={employee.eimage} className='img-fluid img-thumbnail' style={{height:300,width:400}} alt="" />
                  </div>
                  <div className="col-md-8 mt-2">
                        <ul className='list-group'>
                            <li className='list-group-item'>
                              <h4>Employee ID : {employee.id}</h4>
                            </li>
                            <li className='list-group-item'>
                              <h4>Employee Name : {employee.ename}</h4>
                            </li>
                            <li className='list-group-item'>
                              <h4>Employee Salary : {employee.esal}</h4>
                            </li>
                            <li className='list-group-item'>
                              <h4>Employee Email : {employee.email}</h4>
                            </li>
                        </ul>
                  </div>
                </div>
              </div>
              <div className="card-footer">
                <Link to='/' className='btn btn-primary btn-lg'>Back</Link>
              </div>
            </div>
          </div>
        </div>
      </div>

   </React.Fragment>
  )
}

export default FindEmployee
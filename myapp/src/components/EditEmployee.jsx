import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { Link } from 'react-router-dom';
function EditEmployee() {
  let {id} = useParams()
  let navigate=useNavigate();
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
  function updateInput(event){
    setEmployee({
      ...employee,
      [event.target.name]:event.target.value
    })
  }
  function save(event){
    event.preventDefault()
    axios.put(`http://localhost:9000/employees/${employee.id}`,employee)
    .then(()=>{
      alert("Employee Updated...")
      navigate('/')
    })
    .catch((error)=>{
      alert(error)
    })
  }
  return (
   <React.Fragment>
      <p className="h1 text-center text-secondary">Edit Employee:{id} </p>
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
                       <form action="" onSubmit={save}>

                        <div className="card">
                            <div className="card-body">
                              <div className="form-group">
                                <input type="text" name="ename" onChange={updateInput} value={employee.ename} className='form-control' placeholder='Employee Name' />
                              </div>
                              <div className="form-group">
                                <input type="text" name="esal" onChange={updateInput} value={employee.esal} className='form-control' placeholder='Employee salary' />
                              </div>
                              <div className="form-group">
                                <input type="email" name="email" onChange={updateInput} value={employee.email} className='form-control' placeholder='Employee Email' />
                              </div>
                              <div className="form-group">
                                <input type="text" name="eimage" onChange={updateInput} value={employee.eimage} className='form-control' placeholder='Employee Image URL' />
                              </div>
                              <button className='btn btn-sm btn-outline-amber'>Save</button>
                                <Link to='/' className='btn btn-outline-primary btn-sm float-right'>Back</Link>
                            </div>
                        </div>
                       </form>
                  </div>
                </div>
              </div>
              
            </div>
          </div>
        </div>
      </div>

   </React.Fragment>
  )
}

export default EditEmployee
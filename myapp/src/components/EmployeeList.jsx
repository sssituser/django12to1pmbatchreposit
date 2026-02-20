import React, { useEffect, useState } from 'react'
import {Link} from 'react-router-dom'
import axios from 'axios'
function EmployeeList() {

  let[employees,setEmployees]=useState([]);
    
  useEffect(()=>{
    axios.get("http://localhost:9000/employees")
    .then((res)=>{
      setEmployees(res.data)
    })
    .catch((error)=>{
      alert(error)
    })
  });


  return (
   <React.Fragment>
      <div className="container">
        <p className="h1 text-secondary text-center">EmployeeList</p>
        <section>
          <p className="lead">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Saepe quidem, voluptatibus eos, nostrum vel quo molestias neque debitis, dolorem inventore dolore. Dolores, vitae officia officiis dolorem repudiandae facilis quia, omnis culpa possimus animi minima? Voluptatum reprehenderit, commodi dicta quia similique eaque nam ea maxime tempore deserunt fugit, repudiandae necessitatibus earum vero, veritatis at recusandae voluptatem quidem sed voluptas unde! Vitae! </p>
          <Link to='/add' className='btn btn-outline-primary btn-md'>ADD</Link>
        </section>
        <section>
            {
              employees.length>0 ?
               <table className='table table-bordered table-striped table-hover animated jackInTheBox'>
                  <thead className='bg-primary text-white text-center'>
                    <tr>
                      <th>Employee ID</th>
                      <th>Employee Name</th>
                      <th>Employee Salary</th>
                      <th>Employee Email</th>
                      <th>Employee Image</th>
                      <th>Actions</th>
                    </tr>
                  </thead>
                  <tbody className='bg-info'>
                      {
                        employees.map((emp)=>{
                          return(
                            <tr>
                              <td>{emp.id}</td>
                              <td>{emp.ename}</td>
                              <td>{emp.esal}</td>
                              <td>{emp.email}</td>
                              <td>
                                <img src={emp.eimage} className='img-fluid' style={{width:150,height:100}}/>
                              </td>
                              <td>
                                <Link to={`/find/${emp.id}`} className='mr-3'>Find</Link>
                                <Link to={`/edit/${emp.id}`} className='mr-3'>Edit</Link>
                                <Link>Delete</Link>
                              </td>
                            </tr>
                          )
                        })
                      }
                  </tbody>
               </table>
              :
              <p className="h2 text-danger text-center">Records Not Found</p>
            }
        </section>
      </div>
   </React.Fragment>
  )
}

export default EmployeeList
import React, { useEffect,useState } from 'react'

const url="https://jsonplaceholder.typicode.com/user";
const FetchComponent = () => {
    const [user,setuser]=useState([]);

    const getData= async function(){
       const  user=await fetch(url).then(ris=>ris.json())
       setuser(user)

    }

    useEffect(()=>{
        getData();
    },[])

  return (
 <div className='container'>
    <div className='row'>
        <select>
            <option key={users.id} value={}></option>
        </select>
    </div>

 </div>
  )
}

export default FetchComponent
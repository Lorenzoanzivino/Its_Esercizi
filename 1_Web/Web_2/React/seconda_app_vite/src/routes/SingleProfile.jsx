import React from 'react';
import { useParams } from 'react-router-dom';

const SingleProfile = () => {
    const params = useParams();
    console.log(params)
    return (
        <div className="text-center"><br/>SingleProfile con id : {params.id} </div>
    )
}
export default SingleProfile;
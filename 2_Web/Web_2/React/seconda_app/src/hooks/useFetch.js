import React, { useEffect, useState } from 'react'
import axios from 'axios'


const useFetch = () => {
    
    const [data, setData] = useState([])
    const [isLoading, setIsLoading] = useState([])

    useEffect(() => {
        (async () => {
            setIsLoading(true);
            try{
                const {data} = axios.get(url)
                setData(data)
            }catch(err){
                console.log(err)
            }
            setIsLoading(false);
        })()
    }, [url])

    return {data, isLoading}
}

export default useFetch
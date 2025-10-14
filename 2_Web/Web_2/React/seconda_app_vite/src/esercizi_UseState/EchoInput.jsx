import React, { useState } from 'react';

const EchoInput = () => {
    const [testo, setTesto] = useState("")
    return (
        <div>
            <input className="text-center" type="text" value={testo} onChange={(event) => setTesto(event.target.value)} />
            <p className="text-center">Hai scritto: {testo}</p>
        </div>
    );
}
export default EchoInput;
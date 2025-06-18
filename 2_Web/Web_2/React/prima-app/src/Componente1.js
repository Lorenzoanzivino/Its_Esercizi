import React from 'react'

const Componente1 = (props) => {
  console.log(props)
  return (
    <div style={{
      color:"red",
      border:"1px #000 solid",
      fontWeight:"600",
      margin:"15px",
      padding:"15px",
      width:"300px",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      justifyContent: "center"
      }}>
      <div>componente1 di: {props.children}</div>
      <Anagrafica></Anagrafica>
      <Messaggio></Messaggio>
    </div>
  );
};

const Anagrafica = () => {
  return(<div>Anagrafica</div>)
}

const Messaggio = () => {
  return(<div>Messaggio</div>)
}

export default Componente1
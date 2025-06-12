const elementRoot=document.querySelector("#root");
const root=ReactDOM.createRoot(elementRoot);

const App=({children})=>{
    return(
        <div className="main">
            <h1>Primo componente</h1>
            {children}
        </div>
    )
}

const List=function () {
    return (
        <ul>
            <li>PHP</li>
            <li>JS</li>
            <li>Python</li>
        </ul>
    )
}

root.render(
    <>
        <App>
            <h2>Lista competenze</h2>
            <List/>
        </App>
    </>
)
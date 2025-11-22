import * as util from "../util.js"
console.log(util.API_KEY);
console.log(util.SECRET_KEY);

console.log("Funzia")

for(var i=0;i<4;i++){
    console.log(i)
}

console.log(i); // cosa stampa?

const arr1=[1,2,3];
console.log(arr1,...arr1);

const arr2=arr1;
arr1.push(4);
arr2.unshift(0);
console.log(arr1, arr2);

const prof={
    nome:"Rob",
    cognome:"Del",
    eta:48,
    indirizzo:{
        via:"CesarePavese",
        citta:"Roma"
    }
}

console.log(prof.indirizzo.via);
console.log(prof.nome, prof.cognome, prof.eta);

const prof2=new Object();

prof2.nome="Rob";
prof2.cognome="Del";

console.log(prof2)

function persona(){
    this.nome="rob";
    this.cognome="del";
}

const robdel=new persona("rob", "del");
const mariorossi=new persona("mario", "rossi");

mariorossi.telefono = "1234";

console.log(robdel,mariorossi);

const list={
ARS:"🇦🇷 Peso Argentino",
USD:"🇺🇸 Dólar",
EUR:"🇪🇺 Euro",
GBP:"🇬🇧 Libra",
JPY:"🇯🇵 Yen",
BRL:"🇧🇷 Real",
CLP:"🇨🇱 Peso Chileno",
COP:"🇨🇴 Peso Colombiano",
MXN:"🇲🇽 Peso Mexicano",
CAD:"🇨🇦 Dólar Canadiense",
AUD:"🇦🇺 Dólar Australiano",
CHF:"🇨🇭 Franco Suizo",
CNY:"🇨🇳 Yuan"
};

const from=document.querySelector("#from");
const to=document.querySelector("#to");
const amount=document.querySelector("#amount");
const value=document.querySelector("#value");
const info=document.querySelector("#info");
const hist=document.querySelector("#history");

Object.entries(list).forEach(([c,n])=>{
from.add(new Option(n,c));
to.add(new Option(n,c));
});
from.value="USD";
to.value="ARS";

function toast(t){
const e=document.querySelector("#toast");
e.textContent=t;
e.classList.add("show");
setTimeout(()=>e.classList.remove("show"),1800);
}

function loadHist(){
const h=JSON.parse(localStorage.getItem("hist")||"[]");
hist.innerHTML=h.map(x=>`<li>${x}</li>`).join("");
}
loadHist();

async function convert(){
const a=parseFloat(amount.value)||0;
const f=from.value;
const t=to.value;
if(f===t){
value.textContent=a.toLocaleString();
info.textContent="Misma moneda";
return;
}
value.textContent="Consultando...";
const r=await fetch(`https://open.er-api.com/v6/latest/${f}`);
const d=await r.json();
const rate=d.rates[t];
const res=a*rate;
value.textContent=new Intl.NumberFormat("es-AR",{maximumFractionDigits:2}).format(res)+" "+t;
info.textContent=`1 ${f} = ${rate.toFixed(4)} ${t}`;
let h=JSON.parse(localStorage.getItem("hist")||"[]");
h.unshift(`${new Date().toLocaleTimeString()} - ${a} ${f} → ${res.toFixed(2)} ${t}`);
h=h.slice(0,10);
localStorage.setItem("hist",JSON.stringify(h));
loadHist();
}

amount.addEventListener("input",convert);
from.addEventListener("change",convert);
to.addEventListener("change",convert);

document.querySelector("#swap").onclick=()=>{
[from.value,to.value]=[to.value,from.value];
document.querySelector("#swap").animate([{transform:"rotate(0deg)"},{transform:"rotate(180deg)"}],{duration:400});
convert();
};

document.querySelector("#copy").onclick=()=>{
navigator.clipboard.writeText(value.textContent);
toast("Resultado copiado");
};

document.querySelector("#clear").onclick=()=>{
localStorage.removeItem("hist");
loadHist();
toast("Historial eliminado");
};

convert();

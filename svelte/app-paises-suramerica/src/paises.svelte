<script>
    export let pais;
    let p;

    /* [0]=Nombre_pais [1]=capital [2]=poblacion [3]=moneda [4]=área [5]=bandera */
    const paises = {
        "colombia": ["Colombia", "Bogotá", "51,52 millones", "Peso colombiano", "1,142 millones km²", "colombia.png"],
        "venezuela": ["Venezuela", "Caracas", "28,2 millones", "Bolívar", "916.445 km²", "venezuela.png"],
        "ecuador": ["Ecuador", "Quito", "17,8 millones", "Dólar estadounidense", "256.378 km²", "ecuador.png"],
        "peru": ["Perú", "Lima", "33,71 millones", "Sol peruano", "1.285.215 km²", "peru.jpg"],
        "brasil": ["Brasil", "Brasilia", "214,3 millones", "Real brasileño", "8,51 millones km²", "brasil.jpg"]
    };

    p = paises[pais];
</script>

<div class="main">
    <div class="col1">
        <img src={`./src/assets/${p[5]}`} alt="Bandera_{p[0]}" width="300" height="200">
    </div>
    <div class="col2">
        <div class="linea"><strong>País:</strong> {p[0]}</div>
        <div class="linea"><strong>Capital:</strong> {p[1]}</div>
        <div class="linea"><strong>Población:</strong> {p[2]}</div>
        <div class="linea"><strong>Moneda:</strong> {p[3]}</div>
        <div class="linea"><strong>Extensión:</strong> {p[4]}</div>
    </div>
</div>

<style>
    .main {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        grid-gap: 5px;
        grid-auto-rows: minmax(100px, auto);
        border-radius: 10px;
        border-style: solid;
        border-color: rgb(186, 190, 182);
        border-width: 2px;
        margin-left: auto;
        margin-right: auto;
        width: 600px;
        box-shadow: 5px 5px 5px black;
        margin-bottom: 10px;
    }

    .col1 {
        grid-column: 1;
        grid-row: 1;
        margin: 5px;
        padding: 5px;
    }

    .col2 {
        grid-column: 2;
        grid-row: 1;
        margin: 5px;
        padding: 5px;
        border-color: black;
        width: max-content;
    }

    strong {
        color: blue;
        font-weight: bolder;
    }

    .linea {
        font-size: 20px;
        margin-bottom: 18px;
    }
</style>

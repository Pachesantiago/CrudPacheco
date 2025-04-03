<script>
    export let numero; // Exportamos la variable numero para poder llamarla en App.svelte
    let resultado; // Variable local

    $: if (numero === 0) // Se coloca el símbolo $: para generar reactividad en el if para resultado
        resultado = "neutro";
    else
        if (numero % 2 === 0)
            resultado = "par";
        else
            resultado = "impar";
</script>

<!-- Las variables las llamamos entre llaves -->
<p>El número {numero} es {resultado}</p>

<style>
    p {
        color: rgb(34, 5, 112);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 25px;
    }
</style>

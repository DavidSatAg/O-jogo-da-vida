<template>
    <div>
        <h1>Jogo da vida</h1>
        <div v-for="(linha, id) in m" :key="id" class="container">
            <div v-for="(quadrado, id) in linha" :key="id" class ="quadrado" :class="{vivo: quadrado==1}"></div>
        </div>
    </div>
</template>

<script>


function conta_vivos(m, x, y) {
    const delta_coord = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 1],
        [1, -1], [1, 0], [1, 1],
    ]
    let coord_vizinhos = []
    for (let k = 0; k < delta_coord.length; k++) {
        coord_vizinhos.push([x + delta_coord[k][0], y + delta_coord[k][1]])
    }
    let coord_vizinhos_vivos = coord_vizinhos.filter((e) => e[0] >= 0 && e[0] < m.length && e[1] >= 0 && e[1] < m[0].length && m[e[0]][e[1]] == 1)
    return coord_vizinhos_vivos.length
}

function atualiza(m) {
    let nm = new Array(m.length)
    for (let i = 0; i < m.length; i++) {
        nm[i] = new Array(m[0].length).fill(0)
    }
    for (let x = 0; x < m.length; x++) {
        for (let y = 0; y < m[0].length; y++) {
            let vivos = conta_vivos(m, x, y)
            if (m[x][y] == 1) {
                if (vivos == 2 || vivos == 3) {
                    nm[x][y] = 1
                }
            }
            else {
                if (vivos == 3) {
                    nm[x][y] = 1
                }
            }
        }
    }
    return nm
}

export default {
    name: 'Life',
    data() {
        return {
            m: []
        }
    },
    created() {
        this.matriz()
    },
    mounted() {
        setInterval(() => {
            this.recarrega()
        }, 500)
    },
    methods: {
        recarrega() {
            this.m = atualiza(this.m)
        },
        matriz() {
            let m = new Array(16)
            for (let i = 0; i < 16; i++) {
                m[i] = new Array(30)
                for (let j = 0; j < 30; j++) {
                    m[i][j] = Math.floor(Math.random() * 2)
            this.m = m
    }
}
        }
    }
}
</script>

<style>
.container {
    display: flex;
    justify-content: center;
}
.quadrado {
    width: 40px;
    height: 40px;
    border: 1px solid

}
.vivo {
    background-color: rgb(110, 197, 110);
}
</style>
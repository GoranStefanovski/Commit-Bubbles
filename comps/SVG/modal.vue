<script>
export default {
  name: 'modal',
  props: {
    pickedAuthorObject: Object
  },
  methods: {
    setAuthorZero() {
        this.$emit('setAuthor')
    },
    commitDate(ts) {
      return moment(new Date(ts)).format('MM/DD/yy HH:mm:ss')
    }
  }
}
</script>

<template>
    <g font-family="Verdana" font-size="16" @click="setAuthorZero()">
      <rect style="stroke:rgb(0,0,0);stroke-width:2" x="300" y="300" height="300" width="400" fill="white"
            opacity="0.7"/>
      <text class="close-btn" @click="setAuthorZero()" x="55%" y="330">X</text>
      <text x="320" y="330">Selected Commit</text>
      <text x="320" y="380">Commit:</text>
      <foreignObject x="395" y="363" width="900" height="100">
        <a _target="_blank" v-bind:href="pickedAuthorObject.commitUrl">
          {{ pickedAuthorObject.message }}
        </a>
      </foreignObject>
      <text x="320" y="430">Author: {{ pickedAuthorObject.author }}</text>
      <text x="320" y="480">Date/Time: {{ commitDate(pickedAuthorObject.ts) }}</text>
      <text x="320" y="530">Size: {{ pickedAuthorObject.size }}</text>
      <text x="320" y="580">Test Percentage: {{ pickedAuthorObject.testPercentage }}</text> 
    </g>
</template>

<style scoped>
.close-btn:hover {
  cursor: pointer;
}
</style>
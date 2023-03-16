<script>
export default {
  name: 'modal',
  props: {
    pickedCommitObject: Object
  },
  methods: {
    setCommitZero() {
        this.$emit('setCommit')
    },
    commitDate(ts) {
      return moment(new Date(ts)).format('MM/DD/yy HH:mm:ss')
    }
  }
}
</script>

<template>
    <g font-family="Verdana" font-size="16" @click="setCommitZero()">
      <rect style="stroke:rgb(0,0,0);stroke-width:2" x="300" y="300" height="300" width="600" fill="white"
            opacity="0.7"/>
      <text class="close-btn" @click="setCommitZero()" x="810" y="330">X</text>
      <text x="320" y="330">Selected Commit</text>
      <text x="320" y="380">Commit:</text>
      <foreignObject x="395" y="363" width="900" height="100">
        <a _target="_blank" v-bind:href="pickedCommitObject.commitUrl">
          {{ pickedCommitObject.message }}
        </a>
      </foreignObject>
      <text x="320" y="430">Author: {{ pickedCommitObject.author }}</text>
      <text x="320" y="480">Date/Time: {{ commitDate(pickedCommitObject.ts) }}</text>
      <text x="320" y="530">Size: {{ pickedCommitObject.size }}</text>
      <text x="320" y="580">Test Percentage: {{ pickedCommitObject.testPercentage }}</text>
    </g>
</template>

<style scoped>
.close-btn:hover {
  cursor: pointer;
}
</style>
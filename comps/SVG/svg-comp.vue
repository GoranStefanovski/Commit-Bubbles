<script>
import SkModal from './modal.vue'

export default {
  name: 'svg-comp',
  props: {
    dataSource: Object
  },
  components: {
    SkModal,
  },
  directives: {},
  data() {
    return {
      windowWidth: window.innerWidth - 50,
      chartHeight: 680,
      topMargin: 100,
      colors: ["#FFA07A", "#20B2AA", "#778899", "#B0C4DE", "#F5F5DC", "#00FF00", "#000000", "#32CD32", "#FAF0E6", "#0000FF", "#FF00FF", "#8A2BE2", "#800000", "#A52A2A", "#66CDAA", "#DEB887", "#0000CD", "#5F9EA0", "#7FFF00", "#9370DB", "#D2691E", "#FF7F50", "#7B68EE", "#6495ED", "#48D1CC", "#DC143C", "#C71585", "#00FFFF", "#191970", "#00008B", "#F5FFFA", "#008B8B", "#FFE4E1", "#B8860B", "#A9A9A9", "#006400", "#000080", "#BDB76B", "#8B008B", "#808000", "#6B8E23", "#FF8C00", "#FFA500", "#9932CC", "#FF4500", "#8B0000", "#DA70D6", "#E9967A", "#EEE8AA", "#8FBC8F", "#98FB98", "#483D8B", "#AFEEEE", "#2F4F4F", "#DB7093", "#00CED1", "#9400D3", "#FFDAB9", "#FF1493", "#CD853F", "#00BFFF", "#FFC0CB", "#696969", "#DDA0DD", "#1E90FF", "#B0E0E6", "#B22222", "#800080", "#FFFAF0", "#FF0000", "#228B22", "#BC8F8F", "#FF00FF", "#4169E1", "#DCDCDC", "#FA8072", "#FFD700", "#FAA460", "#DAA520", "#2E8B57", "#808080", "#008000", "#A0522D", "#ADFF2F", "#C0C0C0", "#87CEEB", "#FF69B4", "#6A5ACD", "#CD5C5C", "#708090", "#4B0082", "#00FF7F", "#F0E68C", "#4682B4", "#E6E6FA", "#D2B48C", "#008080", "#7CFC00", "#D8BFD8", "#FFFACD", "#FF6347", "#ADD8E6", "#40E0D0", "#F08080", "#EE82EE", "#F5DEB3", "#FAFAD2", "#90EE90", "#D3D3D3", "#FFFF00", "#FFB6C1"],
      selectedAuthors: [],
      clickedCommit: 0,
      commits: [],
      i: 10,
      pickedCommitObject: {},
      queryAuthors: []
    }
  },
  mounted() {
    this.checkAllAuthors;
  },
  watch: {
    // whenever question changes, this function will run
    selectedAuthors(a, b) {
      router.push({path: '/', query: {authors: this.selectedAuthors.join(",")}})
    }
  },
  computed: {
    startDate() {
      return moment(new Date(this.from)).format('Do MMMM yyyy')
    },
    endDate() {
      return moment(new Date(this.to)).format('Do MMMM yyyy')
    },
    authors() {
      return _.uniq(_.map(this.commits, 'author'))
    },
    selected() {
      return {authors: this.authors.slice(0)}
    },
    from() {
      return _.min(this.getValues)
    },
    to() {
      return _.max(this.getValues)
    },
    timeSpan() {
      let timespan = moment.duration(moment(this.from).diff(moment(this.to))).humanize();
      timespan = timespan.charAt(0).toUpperCase() + timespan.slice(1)
      return timespan;
    },
    getValues() {
      return _.map(this.commits, "ts")
    },
  },
  created() {
    fetch(this.dataSource)
        .then(response => response.json())
        .then(data => {
          this.commits = data;
          // this.selectedAuthors = this.authors;
        });
    if (this.$route.query.authors) {
      this.selectedAuthors = this.$route.query.authors.split(',');
    }
  },
  methods: {
    clickAuthor(dat) {
      this.clickedCommit = dat.hash;
      this.pickedCommitObject = dat;
    },
    checkAllAuthors() {
      this.selectedAuthors = this.authors;
    },
    cleanAllAuthors() {
      this.selectedAuthors = [];
    },
    addToUrl(author) {

    }
  }
}
</script>

<template>
  <h2>{{ timeSpan }} of commits shown between {{ startDate }} and {{ endDate }}</h2>
  <div>Show authors:
    <label v-for="author in authors" v-bind:key="author" :style="'color: ' + colors[authors.indexOf(author)]">
      <input type="checkbox" v-model="selectedAuthors" :value="author" @click="addToUrl(author)"> {{ author }}
    </label>
    <button @click="checkAllAuthors()" style="margin: 0 0 5px 5px">All authors</button>
    <button @click="cleanAllAuthors()" style="margin: 0 0 5px 5px">None
    </button>
  </div>
  <svg xmlns="http://www.w3.org/2000/svg" xmlns:xl="http://www.w3.org/1999/xlink" version="1.1" width="100%"
       :height="chartHeight + topMargin + 5"
       xmlns:dc="http://purl.org/dc/elements/1.1/">
    <g transform="translate(10,2.5) rotate(0)">


      <rect fill="#FEFCFF" x="100" :y="topMargin" :width="windowWidth - 100" :height="chartHeight"
      />
      <g font-family="Verdana" font-size="16">
        <text x="0" :y="topMargin + 8">All Test</text>
        <text x="0" :y="chartHeight/2 + 5 + topMargin">Equal</text>
        <text x="0" :y="chartHeight + topMargin">All Prod</text>
        <text :x="windowWidth-70" :y="chartHeight/2 + 17 + topMargin">Time &#10148;</text>
      </g>
      <g style="stroke:rgb(0,0,0);stroke-width:2">
        <line x1="100" :y1="chartHeight/2 + topMargin" :x2="windowWidth" :y2="chartHeight/2 + topMargin"/>
        <line x1="100" :y1="topMargin +2" x2="100" :y2="chartHeight + topMargin+2"/>
      </g>
      <g font-family="Verdana" font-size="8" v-for="i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]" v-bind:key="i"
         style="stroke:rgb(0,0,0);stroke-width:0.5">
        <line v-if="i !== 5" x1="100" stroke-dasharray="10,35"
              :y1="chartHeight + 2 - (chartHeight/10 * i) + topMargin" :x2="windowWidth"
              :y2="chartHeight - (chartHeight/10 * i) + topMargin"/>
        <text fill="white" x="70" :y="chartHeight + 3  - (chartHeight/10 * i) + topMargin">
          {{ 100 - (10 * i) }}:{{ (10 * i) }}
        </text>
      </g>
      <g stroke="black">
        <circle v-for="commit in commits" v-bind:key="commit" v-show="selectedAuthors.indexOf(commit.author) > -1"
                :cx="100 + (commit.ts - from) * (windowWidth - 100) / (to - from)"
                :cy="chartHeight - (commit.testPercentage * chartHeight/100) + topMargin"
                :r="commit.size * (chartHeight/600)"
                :stroke-opacity="(clickedCommit === commit.hash) ? 1 : 0"
                :fill="colors[authors.indexOf(commit.author)]" fill-opacity="0.5"
                @click="clickAuthor(commit)"/>
      </g>
      <sk-modal v-show="clickedCommit" :pickedCommitObject="pickedCommitObject"
                @setCommit="clickedCommit = 0"></sk-modal>
    </g>

  </svg>
<!--  <pre>-->
<!--    {{ dataSource }}-->
<!--  </pre>-->
</template>

<style scoped>
.close-btn:hover {
  cursor: pointer;
}
</style>
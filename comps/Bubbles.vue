<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  directives: {},
  data() {
    return {
      chartHeight: 680,
      topMargin: 100,
      colors: ["#FFA07A", "#20B2AA", "#778899", "#B0C4DE", "#F5F5DC", "#00FF00", "#000000", "#32CD32", "#FAF0E6", "#0000FF", "#FF00FF", "#8A2BE2", "#800000", "#A52A2A", "#66CDAA", "#DEB887", "#0000CD", "#5F9EA0", "#7FFF00", "#9370DB", "#D2691E", "#FF7F50", "#7B68EE", "#6495ED", "#48D1CC", "#DC143C", "#C71585", "#00FFFF", "#191970", "#00008B", "#F5FFFA", "#008B8B", "#FFE4E1", "#B8860B", "#A9A9A9", "#006400", "#000080", "#BDB76B", "#8B008B", "#808000", "#6B8E23", "#FF8C00", "#FFA500", "#9932CC", "#FF4500", "#8B0000", "#DA70D6", "#E9967A", "#EEE8AA", "#8FBC8F", "#98FB98", "#483D8B", "#AFEEEE", "#2F4F4F", "#DB7093", "#00CED1", "#9400D3", "#FFDAB9", "#FF1493", "#CD853F", "#00BFFF", "#FFC0CB", "#696969", "#DDA0DD", "#1E90FF", "#B0E0E6", "#B22222", "#800080", "#FFFAF0", "#FF0000", "#228B22", "#BC8F8F", "#FF00FF", "#4169E1", "#DCDCDC", "#FA8072", "#FFD700", "#FAA460", "#DAA520", "#2E8B57", "#808080", "#008000", "#A0522D", "#ADFF2F", "#C0C0C0", "#87CEEB", "#FF69B4", "#6A5ACD", "#CD5C5C", "#708090", "#4B0082", "#00FF7F", "#F0E68C", "#4682B4", "#E6E6FA", "#D2B48C", "#008080", "#7CFC00", "#D8BFD8", "#FFFACD", "#FF6347", "#ADD8E6", "#40E0D0", "#F08080", "#EE82EE", "#F5DEB3", "#FAFAD2", "#90EE90", "#D3D3D3", "#FFFF00", "#FFB6C1"],
      selectedAuthors: [],
      clickedAuthor: 0,
      dataNew: {
        commits: [
          {
            id: 1,
            ts: 1288202623005,
            hash: "1234567890",
            testPercentage: 100,
            size: 55,
            author: "John Doe",
            message: "some words in a commit message",
            commitUrl: "https://github.com/paul-hammant/Commit-Bubbles-Vue/mockCommits/1234567890.txt"
          },
          {
            id: 2,
            ts: 1288121623006,
            hash: "13432435645",
            testPercentage: 30,
            size: 81,
            author: "John Doe",
            message: "some changes",
            commitUrl: "https://github.com/paul-hammant/Commit-Bubbles-Vue/mockCommits/13432435645.txt"
          },
          {
            id: 3,
            ts: 1288128023006,
            hash: "12232435645",
            testPercentage: 50,
            size: 50,
            message: "testing testing 123",
            author: "A bug fix",
            commitUrl: "https://github.com/paul-hammant/Commit-Bubbles-Vue/mockCommits/12232435645.txt"
          },
          {
            id: 4,
            ts: 1288202823006,
            hash: "12332343455",
            testPercentage: 55,
            size: 50,
            author: "Hector",
            message: "the test pyramid is best",
            commitUrl: "https://github.com/paul-hammant/Commit-Bubbles-Vue/mockCommits/12332343455.txt"
          },
          {
            id: 5,
            ts: 1288323623006,
            hash: "2342342344",
            testPercentage: 15,
            size: 22,
            author: "Mildred",
            message: "testing testing 123",
            commitUrl: "https://github.com/paul-hammant/Commit-Bubbles-Vue/mockCommits/2342342344.txt"
          }
        ]
      },
      i: 10,
      pickedAuthorObject: {}
    }
  },
  computed: {
    startDate() {
      return moment(new Date(this.from)).format('MM/DD/yy HH:mm')
    },
    endDate() {
      return moment(new Date(this.to)).format('MM/DD/yy HH:mm')
    },
    authors() {
      return _.uniq(_.map(this.dataNew.commits, 'author'))
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
      return moment.duration(moment(this.from).diff(moment(this.to))).humanize()
    },
    getValues() {
      return _.map(this.dataNew.commits, "ts")
    },

  },
  mounted() {
    this.checkAllAuthors;
    this.selectedAuthors = this.authors;
  },
  methods: {
    clickAuthor(dat) {
      this.clickedAuthor = dat.id;
      this.pickedAuthorObject = dat;
      console.log('OVBDFEDASDLKJASDLJASDLKJASDLKASJDLASKDJALSKDJ')
    },
    checkAllAuthors() {
      this.selectedAuthors = this.authors;
    },
    cleanAllAuthors() {
      this.selectedAuthors = [];
    },
    commitDate(ts) {
      return moment(new Date(ts)).format('MM/DD/yy HH:mm:ss')
    }
  }
}
</script>

<template>
  <svg xmlns="http://www.w3.org/2000/svg" xmlns:xl="http://www.w3.org/1999/xlink" version="1.1" width="1220"
       :height="chartHeight + topMargin + 5"
       xmlns:dc="http://purl.org/dc/elements/1.1/">
    <rect fill="#FEFCFF" x="100" :y="topMargin" width="1100" :height="chartHeight"
    />
    <g font-family="Verdana" font-size="16">
      <text x="0" :y="topMargin + 8">All Test</text>
      <text x="0" :y="chartHeight/2 + 5 + topMargin">Equal</text>
      <text x="0" :y="chartHeight + topMargin">All Prod</text>
      <text x="1140" :y="chartHeight/2 + 17 + topMargin">Time &#10148;</text>
    </g>
    <g style="stroke:rgb(0,0,0);stroke-width:2">
      <line x1="100" :y1="chartHeight/2 + topMargin" x2="1200" :y2="chartHeight/2 + topMargin"/>
      <line x1="100" :y1="topMargin +2" x2="100" :y2="chartHeight + topMargin+2"/>
    </g>
    <g font-family="Verdana" font-size="8" v-for="i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]" v-bind:key="i"
       style="stroke:rgb(0,0,0);stroke-width:0.5">
      <line v-if="i !== 5" x1="100" stroke-dasharray="10,35"
            :y1="chartHeight + 2 - (chartHeight/10 * i) + topMargin" x2="1200"
            :y2="chartHeight - (chartHeight/10 * i) + topMargin"/>
      <text fill="white" x="70" :y="chartHeight + 3  - (chartHeight/10 * i) + topMargin">
        {{ 100 - (10 * i) }}:{{ (10 * i) }}
      </text>
    </g>
    <g stroke="black">
      <circle v-for="commit in dataNew.commits" v-bind:key="commit" v-show="selectedAuthors.indexOf(commit.author) > -1"
              :cx="100 + (commit.ts - from) * 1100 / (to - from)"
              :cy="chartHeight - (commit.testPercentage * chartHeight/100) + topMargin"
              :r="commit.size * (chartHeight/600)"
              :stroke-opacity="(clickedAuthor === commit.id) ? 1 : 0"
              :fill="colors[authors.indexOf(commit.author)]" fill-opacity="0.5"
              @click="clickAuthor(commit)"/>
    </g>
    <foreignObject class="node" x="0" y="0" width="1200" :height="topMargin">
      <body xmlns="http://www.w3.org/1999/xhtml">
      <h2>{{ timeSpan }} shown between {{ startDate }} and {{ endDate }}</h2>
      <div>Show authors:
        <label v-for="author in authors" v-bind:key="author" :style="'color: ' + colors[authors.indexOf(author)]">
          <input type="checkbox" v-model="selectedAuthors" :value="author"> {{ author }}
        </label>
        <button @click="checkAllAuthors()" style="margin: 0 0 5px 5px">All authors</button>
        <button @click="cleanAllAuthors()" style="margin: 0 0 5px 5px">None
        </button>
      </div>
      </body>
    </foreignObject>
    <g font-family="Verdana" font-size="16" v-show="clickedAuthor" @click="clickedAuthor = 0">
      <rect style="stroke:rgb(0,0,0);stroke-width:2" x="300" y="300" height="300" width="400" fill="white"
            opacity="0.7"/>
      <text class="close-btn" @click="clickedAuthor = 0" x="55%" y="330">X</text>
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
  </svg>
</template>

<style scoped>
.close-btn:hover {
  cursor: pointer;
}
</style>
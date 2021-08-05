<template>
  <b-container fluid>
    <oi-navbar />
    <b-row>
      <b-col cols="auto" class="py-2">
        <oi-menu />
      </b-col>
      <b-col>
        <p />
        <h1 class="ui header">Overwatch Coaching Index</h1>
        <br />

        <div class="ui horizontal divider">
          <video-cards :videos="videos" />
        </div>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
// import filterByPredicate from '../../util/filter'
import heroResults from '../../../hero_results.json'
export default {
  data() {
    return { heroResults }
  },

  computed: {
    // created() {
    //   console.log(this.$route)
    //   this.hero = this.$route.params.hero
    //   this.rank = this.$route.params.rank
    // },
    videos() {
      const hero = this.$route.query.hero
      const rank = this.$route.query.rank
      let videos = []
      if (hero && rank) {
        videos = this.heroResults.heroes[hero].videos.filter((item) => item.rank.includes(rank))
      } else if (!hero && rank) {
        videos = this.heroResults.ranks[rank].videos
      } else if (hero && !rank) {
        videos = this.heroResults.heroes[hero].videos
      }
      return videos
    },
  },
}
</script>
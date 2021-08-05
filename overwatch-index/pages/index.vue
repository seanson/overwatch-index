<template>
  <b-container fluid>
    <oi-navbar />
    <b-row>
      <b-col cols="auto" class="py-2">
        <oi-menu />
      </b-col>
      <b-col>
        <p></p>
        <h1 class="ui header">Overwatch Coaching Index</h1>
        <br />
        <p class="intro">
          This is a page in progress for helping Overwatch players find coaching and VOD reviews tailored to their
          specific hero or competitive rank. It is currently a very early work in progress so content and functionality
          will be limited. Updates are currently generated every four hours.
        </p>

        <div class="ui horizontal divider">
          <h3>Latest Videos</h3>
        </div>
        <video-cards :videos="sortedResults.slice(0, 20)" />
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import sortedResults from '../../sorted_results.json'
export default {
  data() {
    return { sortedResults }
  },
}
</script>

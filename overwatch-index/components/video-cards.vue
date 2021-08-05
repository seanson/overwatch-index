<template>
  <b-card-group>
    <b-card
      v-for="(video, index) in videos"
      :key="index"
      no-body
      bg-variant="light"
      :title="video.snippet.title"
      :img-src="video.snippet.thumbnails.medium.url"
      :img-width="video.snippet.thumbnails.medium.width"
      style="max-width: 20rem; min-width: 20rem"
      class="mb-2"
    >
      <b-card-body>
        <b-link :href="'https://www.youtube.com/watch?v=' + video.snippet.resourceId.videoId" target="_blank">
          <h4>{{ video.snippet.title }}</h4>
        </b-link>
        <b-card-text>
          <a :href="'https://www.youtube.com/watch?v=' + video.snippet.resourceId.videoId" target="_blank">
            <small class="text-muted"
              >{{ video['snippet']['publishedAt'].split('T')[0] }} - <b>{{ video.snippet.channelTitle }}</b></small
            >
          </a>
          <br />
        </b-card-text>
      </b-card-body>

      <template #footer>
        <span v-for="rank in video.rank" :key="rank" class="px-0">
          <span v-for="hero in video.heroes" :key="hero" class="px-1">
            <b-badge v-if="hero" :to="`/heroes?hero=${hero}&rank=${rank}`"
              >{{ hero | capitalize }} - {{ rank | capitalize }}</b-badge
            >
          </span>
        </span>
      </template>
    </b-card>
  </b-card-group>
</template>

<script>
export default {
  props: {
    videos: {
      type: Array,
      required: true,
    },
  },
}
</script>

<template>
  <b-list-group mode="vertical">
    <div v-for="item in ['tank', 'dps', 'support', 'ranks']" :key="item">
      <b-list-group-item class="d-flex py-1"
        ><h4>{{ item | capitalize }}</h4>
      </b-list-group-item>
      <b-list-group-item
        v-for="(hero, key) in heroes[item]"
        :key="hero.name"
        :to="item === 'ranks' ? `/heroes?rank=${key}` : `/heroes?hero=${key}`"
        class="d-flex justify-content-between align-items-center text-left py-0"
      >
        <span class="mr-3">
          <font-awesome-icon
            v-if="hero.icon !== undefined"
            :icon="hero.icon"
            style="max-width: 1rem; min-width: 1rem"
          />
          <span class="px-1">{{ hero.name }}</span>
        </span>
        <b-badge variant="info">{{ hero.videos.length }}</b-badge>
      </b-list-group-item>
    </div>
  </b-list-group>
</template>

<script>
import filterByPredicate from '../util/filter'
import heroResults from '../../hero_results.json'
export default {
  data() {
    return { heroResults }
  },

  computed: {
    heroes() {
      return {
        tank: filterByPredicate(this.heroResults.heroes, (item) => item.class === 'tank'),
        dps: filterByPredicate(this.heroResults.heroes, (item) => item.class === 'dps'),
        support: filterByPredicate(this.heroResults.heroes, (item) => item.class === 'support'),
        ranks: this.heroResults.ranks,
      }
    },
  },
}
</script>

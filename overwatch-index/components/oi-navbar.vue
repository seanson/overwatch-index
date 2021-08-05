<template>
  <div>
    <b-navbar type="dark" variant="secondary" class="py-0">
      <b-navbar-brand to="/">Overwatch Index</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="align-items-center text-center ml-auto">
          <!-- Let's get search fixed again -->
          <!-- <b-nav-form>
              <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
              <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
            </b-nav-form> -->

          <b-nav-item href="https://discord.gg/uRzm3YcxHH">
            <font-awesome-icon :icon="['fab', 'discord']" /> Discord
          </b-nav-item>
          <b-nav-item href="https://github.com/seanson/overwatch-index">
            <font-awesome-icon :icon="['fab', 'github']" /> GitHub
          </b-nav-item>
          <b-nav-item href="https://trello.com/b/n4Qc6ZTM/overwatch-index">
            <font-awesome-icon :icon="['fab', 'trello']" /> Trello
          </b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>
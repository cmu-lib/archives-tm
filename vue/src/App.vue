<template>
  <b-container fluid class="p-0 d-flex flex-column parent">
    <b-navbar toggleable="lg" type="dark" variant="secondary">
      <b-navbar-brand to="/">Herb Simon TM</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item to="/">Home</b-nav-item>
        </b-navbar-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-dropdown text="API">
            <b-dropdown-item href="/api/">Browsable API</b-dropdown-item>
          </b-nav-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <router-view></router-view>
    <nav class="navbar sticky-bottom navbar-dark bg-secondary">
      <b-navbar-nav>
        <b-nav-text>
          ©
          <a href="https://library.cmu.edu">Carnegie Mellon University Libraries</a> 2019-2020. Built by
          <a href="https://matthewlincoln.net">Matthew Lincoln</a>.
        </b-nav-text>
      </b-navbar-nav>
      <b-navbar-nav class="ml-auto">
        <b-nav-item href="https://github.com/cmu-lib/archives-tm">GitHub</b-nav-item>
      </b-navbar-nav>
    </nav>
  </b-container>
</template>

<script>
export default {
  components: {}
};
</script>
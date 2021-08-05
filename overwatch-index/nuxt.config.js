export default {
  // Disable server-side rendering: https://go.nuxtjs.dev/ssr-mode
  ssr: false,

  // Target: https://go.nuxtjs.dev/config-target
  target: 'static',

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'overwatch-index',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    'bootstrap/dist/css/bootstrap.css',
    'bootstrap-vue/dist/bootstrap-vue.css',
    '@/assets/theme.css',
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    // '@/plugins/element-ui'
    '@/plugins/bootstrap-ui',
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
    '@nuxtjs/fontawesome',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {},

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    transpile: [/^element-ui/],
  },

  fontawesome: {
    icons: {
      solid: true,
      brands: true,
      // [
      //   "faArrowAltCircleRight",
      //   "faBomb",
      //   "faBowlingBall",
      //   "faBug",
      //   "faBullseye",
      //   "faCircle",
      //   "faClock",
      //   "faClone",
      //   "faCloud",
      //   "faDna",
      //   "faEye",
      //   "faFlag",
      //   "faHammer",
      //   "faHandPointer",
      //   "faHandRock",
      //   "faHistory",
      //   "faMedkit",
      //   "faMusic",
      //   "faRedo",
      //   "faRocket",
      //   "faShieldAlt",
      //   "faSignLanguage",
      //   "faSnowflake",
      //   "faSocks",
      //   "faStar",
      //   "faSyringe",
      //   "faUser",
      // ]
    }
  },
}

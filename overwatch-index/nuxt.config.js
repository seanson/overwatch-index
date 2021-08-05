const TITLE = "Overwatch Index"
const DESCRIPTION = "Overwatch Index is a service for helping players find coaching and VOD reviews tailored to their specific hero or competitive rank."
const URL = "https://overwatch.website"
const PREVIEW_IMAGE = `${URL}/static/images/site_preview.jpg`

export default {
  // Disable server-side rendering: https://go.nuxtjs.dev/ssr-mode
  ssr: false,

  // Target: https://go.nuxtjs.dev/config-target
  target: 'static',

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: TITLE,
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'title', name: 'title', content: TITLE },
      { hid: 'description', name: 'description', content: DESCRIPTION },
      { name: 'format-detection', content: 'telephone=no' },
      // facebook, discord, etc. metadata
      { hid: 'og:type', property: 'og:type', content: 'website' },
      { hid: 'og:url', property: 'og:url', content: URL },
      { hid: 'og:title', property: 'og:title', content: TITLE },
      { hid: 'og:description', property: 'og:description', content: DESCRIPTION },
      { hid: 'og:image', property: 'og:image', content: PREVIEW_IMAGE },
      // twitter metadata
      { hid: 'twitter:card', property: 'twitter:card', content: 'summary_large_image' },
      { hid: 'twitter:url', property: 'twitter:url', content: URL },
      { hid: 'twitter:title', property: 'twitter:title', content: TITLE },
      { hid: 'twitter:description', property: 'twitter:description', content: DESCRIPTION },
      { hid: 'twitter:image', property: 'twitter:image', content: PREVIEW_IMAGE },
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      { rel: "apple-touch-icon", sizes: "180x180", href: '/apple-touch-icon.png' },
      { rel: 'icon', type: 'image/png', sizes: "32x32", href: '/favicon-32x32.png' },
      { rel: 'icon', type: 'image/png', sizes: "16x16", href: '/favicon-16x16.png' },
      { rel: 'manifest', href: '/site.webmanifest' },
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

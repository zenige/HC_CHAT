import routesConfig from './routes.config'
import translation from './static/translation'
const webpack = require('webpack')

export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'client',
    htmlAttrs: {
      lang: 'en',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' },
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {
        href: 'https://fonts.googleapis.com/css?family=Roboto:400,300,100,500,700,900',
        rel: 'stylesheet',
        type: 'text/css',
      },
      {
        href: 'https://use.fontawesome.com/releases/v5.1.0/css/all.css',
        rel: 'stylesheet',
      },
    ],
  },

  /**
   *  Global JS
   */
  script: [
    { src: 'assets/hc-libs/js/main/jquery.min.js' },
    { src: 'assets/hc-libs/js/main/bootstrap.bundle.min.js' },
    { src: 'assets/hc-libs/js/plugins/loaders/blockui.min.js' },
    { src: 'assets/hc-libs/js/app.js' },
    { src: 'assets/hc-libs/js/swiper.js' },
  ],

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    'assets/hc-libs/css/icons/icomoon/styles.css',
    'assets/hc-libs/css/bootstrap.min.css',
    'assets/hc-libs/css/bootstrap_limitless.min.css',
    'assets/hc-libs/css/layout.min.css',
    'assets/hc-libs/css/components.min.css',
    'assets/hc-libs/css/colors.min.css',
    'assets/hc-libs/css/font.css',
    'assets/hc-libs/css/icons/material/icons.css',
    'assets/hc-libs/css/cd-tabs_vla.css',
    'assets/hc-libs/css/healthcare.css',
    'assets/hc-libs/css/main_class.css',
    'assets/hc-libs/css/main_hc.css',
    'assets/hc-libs/css/swiper-bundle.css',
    'assets/scss/_global.scss',
    'assets/scss/_override.scss',
    'assets/scss/_variables.scss',
    'assets/scss/_baseline.scss',
  ],

  styleResources: {
    scss: ['/assets/scss/_variables.scss'],
  },

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/bootstrap
    'bootstrap-vue/nuxt',
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    'nuxt-i18n',
  ],

  i18n: {
    locales: [
      {
        code: 'th',
        iso: 'th-TH',
        name: 'ภาษาไทย',
      },
      {
        code: 'en',
        iso: 'en-US',
        name: 'English',
      },
    ],
    defaultLocale: 'en',
    vueI18n: {
      fallbackLocale: 'en',
      messages: {
        en: translation.en,
        th: translation.th,
      },
    },
    detectBrowserLanguage: {
      useCookie: true,
      alwaysRedirect: false,
    },
  },

  router: {
    extendRoutes(routes, resolve) {
      routes.splice(
        0,
        routes.length,
        ...routesConfig.map((route) => ({
          ...route,
          name: route.name,
          component: resolve(__dirname, route.component),
        }))
      )
    },
  },

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    baseURL: 'http://localhost:200/',
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    plugins: [
      new webpack.ProvidePlugin({
        $: 'jquery',
        jQuery: 'jquery',
        'window.jQuery': 'jquery',
      }),
    ],
  },
}

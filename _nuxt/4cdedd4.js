(window.webpackJsonp=window.webpackJsonp||[]).push([[6,4,5],{331:function(t,e,r){"use strict";r.r(e);r(111);var n={props:{videos:{type:Array,required:!0}}},o=r(71),component=Object(o.a)(n,(function(){var t=this,e=t._self._c;return e("b-card-group",t._l(t.videos,(function(video,r){return e("b-card",{key:r,staticClass:"mb-2",staticStyle:{"max-width":"20rem","min-width":"20rem"},attrs:{"no-body":"","bg-variant":"light",title:video.snippet.title,"img-src":video.snippet.thumbnails.medium.url,"img-width":video.snippet.thumbnails.medium.width}},[e("b-card-body",[e("b-link",{attrs:{href:"https://www.youtube.com/watch?v="+video.snippet.resourceId.videoId,target:"_blank"}},[e("h4",[t._v(t._s(video.snippet.title))])]),t._v(" "),e("b-card-text",[e("a",{attrs:{href:"https://www.youtube.com/watch?v="+video.snippet.resourceId.videoId,target:"_blank"}},[e("small",{staticClass:"text-muted"},[t._v(t._s(video.snippet.publishedAt.split("T")[0])+" - "),e("b",[t._v(t._s(video.snippet.channelTitle))])])])])],1),t._v(" "),e("b-card-footer",{staticStyle:{"min-height":"33px","max-height":"3.5rem"},attrs:{"footer-class":"align-content-center py-1"}},t._l(video.rank,(function(r){return e("span",{key:r,staticClass:"px-0"},t._l(video.heroes,(function(n){return e("span",{key:n,staticClass:"px-1"},[n?e("b-badge",{attrs:{to:"/heroes?hero=".concat(n,"&rank=").concat(r)}},[t._v(t._s(t._f("capitalize")(n))+" - "+t._s(t._f("capitalize")(r)))]):t._e()],1)})),0)})),0)],1)})),1)}),[],!1,null,null,null);e.default=component.exports},332:function(t,e,r){"use strict";r.r(e);var n=r(71),component=Object(n.a)({},(function(){var t=this,e=t._self._c;return e("div",[e("b-navbar",{staticClass:"py-0",attrs:{type:"dark",variant:"secondary"}},[e("b-navbar-brand",{attrs:{to:"/"}},[t._v("Overwatch Index")]),t._v(" "),e("b-navbar-toggle",{attrs:{target:"nav-collapse"}}),t._v(" "),e("b-collapse",{attrs:{id:"nav-collapse","is-nav":""}},[e("b-navbar-nav",{staticClass:"align-items-center text-center ml-auto"},[e("b-nav-item",{attrs:{href:"https://discord.gg/uRzm3YcxHH"}},[e("font-awesome-icon",{attrs:{icon:["fab","discord"]}}),t._v(" Discord\n        ")],1),t._v(" "),e("b-nav-item",{attrs:{href:"https://github.com/seanson/overwatch-index"}},[e("font-awesome-icon",{attrs:{icon:["fab","github"]}}),t._v(" GitHub\n        ")],1),t._v(" "),e("b-nav-item",{attrs:{href:"https://trello.com/b/n4Qc6ZTM/overwatch-index"}},[e("font-awesome-icon",{attrs:{icon:["fab","trello"]}}),t._v(" Trello\n        ")],1)],1)],1)],1)],1)}),[],!1,null,null,null);e.default=component.exports},339:function(t,e,r){"use strict";r.r(e);r(55),r(33),r(112),r(113);var n=r(333),o={data:function(){return{heroResults:n}},computed:{videos:function(){var t=this.$route.query.hero,e=this.$route.query.rank,r=[];return t&&e?r=this.heroResults.heroes[t].videos.filter((function(t){return t.rank.includes(e)})):!t&&e?r=this.heroResults.ranks[e].videos:t&&!e&&(r=this.heroResults.heroes[t].videos),r}}},l=r(71),component=Object(l.a)(o,(function(){var t=this,e=t._self._c;return e("b-container",{attrs:{fluid:""}},[e("oi-navbar"),t._v(" "),e("b-row",[e("b-col",{staticClass:"py-2",attrs:{cols:"auto"}},[e("oi-menu")],1),t._v(" "),e("b-col",[e("p"),t._v(" "),e("h1",{staticClass:"ui header"},[t._v("Overwatch Coaching Index")]),t._v(" "),e("br"),t._v(" "),e("div",{staticClass:"ui horizontal divider"},[e("video-cards",{attrs:{videos:t.videos}})],1)])],1)],1)}),[],!1,null,null,null);e.default=component.exports;installComponents(component,{OiNavbar:r(332).default,OiMenu:r(335).default,VideoCards:r(331).default})}}]);
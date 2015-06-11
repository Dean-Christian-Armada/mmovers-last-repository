var g=document,l=Array,m=Error,aa=parseInt,n=String;function ba(a,b){return a.keyCode=b}function p(a,b){return a.currentTarget=b}function q(a,b){return a.disabled=b}
var r="shift",t="exec",u="replace",ca="preventDefault",v="keyCode",w="toString",da="propertyIsEnumerable",ea="checked",x="split",y="style",z="push",fa="slice",A="value",B="indexOf",C="type",ga="name",D="length",E="prototype",ha="target",F="call",G,H=this,I=function(a){var b=typeof a;if("object"==b)if(a){if(a instanceof l)return"array";if(a instanceof Object)return b;var c=Object[E][w][F](a);if("[object Window]"==c)return"object";if("[object Array]"==c||"number"==typeof a[D]&&"undefined"!=typeof a.splice&&
"undefined"!=typeof a[da]&&!a[da]("splice"))return"array";if("[object Function]"==c||"undefined"!=typeof a[F]&&"undefined"!=typeof a[da]&&!a[da]("call"))return"function"}else return"null";else if("function"==b&&"undefined"==typeof a[F])return"object";return b},ia=function(a){var b=I(a);return"array"==b||"object"==b&&"number"==typeof a[D]},J=function(a){return"string"==typeof a},ja=function(a){var b=typeof a;return"object"==b&&null!=a||"function"==b},ka=function(a,b){function c(){}c.prototype=b[E];
a.t=b[E];a.prototype=new c;a.v=function(a,c,f){for(var h=l(arguments[D]-2),k=2;k<arguments[D];k++)h[k-2]=arguments[k];return b[E][c].apply(a,h)}};var K=function(a){if(m.captureStackTrace)m.captureStackTrace(this,K);else{var b=m().stack;b&&(this.stack=b)}a&&(this.message=n(a))};ka(K,m);K[E].name="CustomError";var la=function(a,b){for(var c=a[x]("%s"),d="",e=l[E][fa][F](arguments,1);e[D]&&1<c[D];)d+=c[r]()+e[r]();return d+c.join("%s")},ma=n[E].trim?function(a){return a.trim()}:function(a){return a[u](/^[\s\xa0]+|[\s\xa0]+$/g,"")},ua=function(a,b){if(b)a=a[u](na,"&amp;")[u](oa,"&lt;")[u](pa,"&gt;")[u](qa,"&quot;")[u](ra,"&#39;")[u](sa,"&#0;");else{if(!ta.test(a))return a;-1!=a[B]("&")&&(a=a[u](na,"&amp;"));-1!=a[B]("<")&&(a=a[u](oa,"&lt;"));-1!=a[B](">")&&(a=a[u](pa,"&gt;"));-1!=a[B]('"')&&(a=a[u](qa,"&quot;"));
-1!=a[B]("'")&&(a=a[u](ra,"&#39;"));-1!=a[B]("\x00")&&(a=a[u](sa,"&#0;"))}return a},na=/&/g,oa=/</g,pa=/>/g,qa=/"/g,ra=/'/g,sa=/\x00/g,ta=/[\x00&<>"']/,va=function(a,b){return a<b?-1:a>b?1:0},wa=function(a){return n(a)[u](/\-([a-z])/g,function(a,c){return c.toUpperCase()})},xa=function(a,b){var c=J(b)?n(b)[u](/([-()\[\]{}+?*.$\^|,:#<!\\])/g,"\\$1")[u](/\x08/g,"\\x08"):"\\s";return a[u](new RegExp("(^"+(c?"|["+c+"]+":"")+")([a-z])","g"),function(a,b,c){return b+c.toUpperCase()})};var ya=function(a,b){b.unshift(a);K[F](this,la.apply(null,b));b[r]()};ka(ya,K);ya[E].name="AssertionError";var L=function(a,b,c){if(!a){var d="Assertion failed";if(b)var d=d+(": "+b),e=l[E][fa][F](arguments,2);throw new ya(""+d,e||[]);}return a};var M=l[E],za=M[B]?function(a,b,c){L(null!=a[D]);return M[B][F](a,b,c)}:function(a,b,c){c=null==c?0:0>c?Math.max(0,a[D]+c):c;if(J(a))return J(b)&&1==b[D]?a[B](b,c):-1;for(;c<a[D];c++)if(c in a&&a[c]===b)return c;return-1},Aa=M.forEach?function(a,b,c){L(null!=a[D]);M.forEach[F](a,b,c)}:function(a,b,c){for(var d=a[D],e=J(a)?a[x](""):a,f=0;f<d;f++)f in e&&b[F](c,e[f],f,a)},Ba=function(a){var b=a[D];if(0<b){for(var c=l(b),d=0;d<b;d++)c[d]=a[d];return c}return[]};var Ca=function(a,b,c){for(var d in a)b[F](c,a[d],d,a)},Da="constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf".split(" "),Ea=function(a,b){for(var c,d,e=1;e<arguments[D];e++){d=arguments[e];for(c in d)a[c]=d[c];for(var f=0;f<Da[D];f++)c=Da[f],Object[E].hasOwnProperty[F](d,c)&&(a[c]=d[c])}};var N;a:{var Fa=H.navigator;if(Fa){var Ga=Fa.userAgent;if(Ga){N=Ga;break a}}N=""};var O=function(){return-1!=N[B]("Edge")};var Ha=-1!=N[B]("Opera")||-1!=N[B]("OPR"),P=-1!=N[B]("Edge")||-1!=N[B]("Trident")||-1!=N[B]("MSIE"),Q=-1!=N[B]("Gecko")&&!(-1!=N.toLowerCase()[B]("webkit")&&!O())&&!(-1!=N[B]("Trident")||-1!=N[B]("MSIE"))&&!O(),R=-1!=N.toLowerCase()[B]("webkit")&&!O(),Ia=function(){var a=N;if(Q)return/rv\:([^\);]+)(\)|;)/[t](a);if(P&&O())return/Edge\/([\d\.]+)/[t](a);if(P)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/[t](a);if(R)return/WebKit\/(\S+)/[t](a)},Ja=function(){var a=H.document;return a?a.documentMode:void 0},
Ka=function(){if(Ha&&H.opera){var a=H.opera.version;return"function"==I(a)?a():a}var a="",b=Ia();b&&(a=b?b[1]:"");return P&&!O()&&(b=Ja(),b>parseFloat(a))?n(b):a}(),La={},S=function(a){var b;if(!(b=La[a])){b=0;for(var c=ma(n(Ka))[x]("."),d=ma(n(a))[x]("."),e=Math.max(c[D],d[D]),f=0;0==b&&f<e;f++){var h=c[f]||"",k=d[f]||"",W=RegExp("(\\d*)(\\D*)","g"),kb=RegExp("(\\d*)(\\D*)","g");do{var X=W[t](h)||["","",""],Y=kb[t](k)||["","",""];if(0==X[0][D]&&0==Y[0][D])break;b=va(0==X[1][D]?0:aa(X[1],10),0==Y[1][D]?
0:aa(Y[1],10))||va(0==X[2][D],0==Y[2][D])||va(X[2],Y[2])}while(0==b)}b=La[a]=0<=b}return b},Ma=H.document,Na=Ja(),Oa=!Ma||!P||!Na&&O()?void 0:Na||("CSS1Compat"==Ma.compatMode?aa(Ka,10):5);var Pa=!P||P&&(O()||9<=Oa);!Q&&!P||P&&P&&(O()||9<=Oa)||Q&&S("1.9.1");P&&S("9");var T=function(a,b){return J(b)?a.getElementById(b):b},Qa=function(a,b,c,d){a=d||a;var e=b&&"*"!=b?b.toUpperCase():"";if(a.querySelectorAll&&a.querySelector&&(e||c))return a.querySelectorAll(e+(c?"."+c:""));if(c&&a.getElementsByClassName){b=a.getElementsByClassName(c);if(e){a={};for(var f=d=0,h;h=b[f];f++)e==h.nodeName&&(a[d++]=h);a.length=d;return a}return b}b=a.getElementsByTagName(e||"*");if(c){a={};for(f=d=0;h=b[f];f++){var e=h.className,k;if(k="function"==typeof e[x])k=0<=za(e[x](/\s+/),c);k&&
(a[d++]=h)}a.length=d;return a}return b},Sa=function(a,b){Ca(b,function(b,d){"style"==d?a[y].cssText=b:"class"==d?a.className=b:"for"==d?a.htmlFor=b:d in Ra?a.setAttribute(Ra[d],b):0==d.lastIndexOf("aria-",0)||0==d.lastIndexOf("data-",0)?a.setAttribute(d,b):a[d]=b})},Ra={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"},Ua=function(a,
b,c){var d=arguments,e=d[0],f=d[1];if(!Pa&&f&&(f[ga]||f[C])){e=["<",e];f[ga]&&e[z](' name="',ua(f[ga]),'"');if(f[C]){e[z](' type="',ua(f[C]),'"');var h={};Ea(h,f);delete h[C];f=h}e[z](">");e=e.join("")}e=g.createElement(e);f&&(J(f)?e.className=f:"array"==I(f)?e.className=f.join(" "):Sa(e,f));2<d[D]&&Ta(g,e,d,2);return e},Ta=function(a,b,c,d){function e(c){c&&b.appendChild(J(c)?a.createTextNode(c):c)}for(;d<c[D];d++){var f=c[d];if(!ia(f)||ja(f)&&0<f.nodeType)e(f);else{var h;a:{if(f&&"number"==typeof f[D]){if(ja(f)){h=
"function"==typeof f.item||"string"==typeof f.item;break a}if("function"==I(f)){h="function"==typeof f.item;break a}}h=!1}Aa(h?Ba(f):f,e)}}};var Va=function(a){var b=a[C];if(void 0===b)return null;switch(b.toLowerCase()){case "checkbox":case "radio":return a[ea]?a[A]:null;case "select-one":return b=a.selectedIndex,0<=b?a.options[b][A]:null;case "select-multiple":for(var b=[],c,d=0;c=a.options[d];d++)c.selected&&b[z](c[A]);return b[D]?b:null;default:return void 0!==a[A]?a[A]:null}};var Wa=function(a){Wa[" "](a);return a};Wa[" "]=function(){};var Xa=!P||P&&(O()||9<=Oa),Ya=P&&!S("9");!R||S("528");Q&&S("1.9b")||P&&S("8")||Ha&&S("9.5")||R&&S("528");Q&&!S("8")||P&&S("9");var Za=function(a,b){this.type=a;this.target=b;p(this,this[ha]);this.defaultPrevented=this.p=!1};Za[E].preventDefault=function(){this.defaultPrevented=!0};var U=function(a,b){Za[F](this,a?a[C]:"");this.target=null;p(this,null);this.relatedTarget=null;this.button=this.screenY=this.screenX=this.clientY=this.clientX=this.offsetY=this.offsetX=0;ba(this,0);this.charCode=0;this.metaKey=this.shiftKey=this.altKey=this.ctrlKey=!1;this.n=this.state=null;a&&this.r(a,b)};ka(U,Za);
U[E].r=function(a,b){var c=this.type=a[C];this.target=a[ha]||a.srcElement;p(this,b);var d=a.relatedTarget;if(d){if(Q){var e;a:{try{Wa(d.nodeName);e=!0;break a}catch(f){}e=!1}e||(d=null)}}else"mouseover"==c?d=a.fromElement:"mouseout"==c&&(d=a.toElement);this.relatedTarget=d;this.offsetX=R||void 0!==a.offsetX?a.offsetX:a.layerX;this.offsetY=R||void 0!==a.offsetY?a.offsetY:a.layerY;this.clientX=void 0!==a.clientX?a.clientX:a.pageX;this.clientY=void 0!==a.clientY?a.clientY:a.pageY;this.screenX=a.screenX||
0;this.screenY=a.screenY||0;this.button=a.button;ba(this,a[v]||0);this.charCode=a.charCode||("keypress"==c?a[v]:0);this.ctrlKey=a.ctrlKey;this.altKey=a.altKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey;this.state=a.state;this.n=a;a.defaultPrevented&&this[ca]()};U[E].preventDefault=function(){U.t[ca][F](this);var a=this.n;if(a[ca])a[ca]();else if(a.returnValue=!1,Ya)try{(a.ctrlKey||112<=a[v]&&123>=a[v])&&ba(a,-1)}catch(b){}};var $a="closure_listenable_"+(1E6*Math.random()|0),ab=0;var bb=function(a,b,c,d,e,f){this.c=a;this.h=b;this.src=c;this.type=d;this.k=!!e;this.l=f;this.key=++ab;this.f=this.j=!1};bb[E].o=function(){this.f=!0;this.l=this.src=this.h=this.c=null};var cb=function(a){this.src=a;this.b={};this.m=0};cb[E].add=function(a,b,c,d,e){var f=a[w]();a=this.b[f];a||(a=this.b[f]=[],this.m++);var h;a:{for(h=0;h<a[D];++h){var k=a[h];if(!k.f&&k.c==b&&k.k==!!d&&k.l==e)break a}h=-1}-1<h?(b=a[h],c||(b.j=!1)):(b=new bb(b,null,this.src,f,!!d,e),b.j=c,a[z](b));return b};cb[E].s=function(a){var b=a[C];if(!(b in this.b))return!1;var c=this.b[b],d=za(c,a),e;if(e=0<=d)L(null!=c[D]),M.splice[F](c,d,1);e&&(a.o(),0==this.b[b][D]&&(delete this.b[b],this.m--));return e};var db="closure_lm_"+(1E6*Math.random()|0),eb={},fb=0,gb=function(a,b,c,d,e){if("array"==I(b)){for(var f=0;f<b[D];f++)gb(a,b[f],c,d,e);return null}c=hb(c);if(a&&a[$a])a=a.w(b,c,d,e);else{if(!b)throw m("Invalid event type");var f=!!d,h=ib(a);h||(a[db]=h=new cb(a));c=h.add(b,c,!1,d,e);c.h||(d=jb(),c.h=d,d.src=a,d.c=c,a.addEventListener?a.addEventListener(b[w](),d,f):a.attachEvent(lb(b[w]()),d),fb++);a=c}return a},jb=function(){var a=mb,b=Xa?function(c){return a[F](b.src,b.c,c)}:function(c){c=a[F](b.src,
b.c,c);if(!c)return c};return b},lb=function(a){return a in eb?eb[a]:eb[a]="on"+a},ob=function(a,b,c,d){var e=!0;if(a=ib(a))if(b=a.b[b[w]()])for(b=b.concat(),a=0;a<b[D];a++){var f=b[a];f&&f.k==c&&!f.f&&(f=nb(f,d),e=e&&!1!==f)}return e},nb=function(a,b){var c=a.c,d=a.l||a.src;if(a.j&&"number"!=typeof a&&a&&!a.f){var e=a.src;if(e&&e[$a])e.A(a);else{var f=a[C],h=a.h;e.removeEventListener?e.removeEventListener(f,h,a.k):e.detachEvent&&e.detachEvent(lb(f),h);fb--;(f=ib(e))?(f.s(a),0==f.m&&(f.src=null,e[db]=
null)):a.o()}}return c[F](d,b)},mb=function(a,b){if(a.f)return!0;if(!Xa){var c;if(!(c=b))a:{c=["window","event"];for(var d=H,e;e=c[r]();)if(null!=d[e])d=d[e];else{c=null;break a}c=d}e=c;c=new U(e,this);d=!0;if(!(0>e[v]||void 0!=e.returnValue)){a:{var f=!1;if(0==e[v])try{ba(e,-1);break a}catch(h){f=!0}if(f||void 0==e.returnValue)e.returnValue=!0}e=[];for(f=c.currentTarget;f;f=f.parentNode)e[z](f);for(var f=a[C],k=e[D]-1;!c.p&&0<=k;k--){p(c,e[k]);var W=ob(e[k],f,!0,c),d=d&&W}for(k=0;!c.p&&k<e[D];k++)p(c,
e[k]),W=ob(e[k],f,!1,c),d=d&&W}return d}return nb(a,new U(b,this))},ib=function(a){a=a[db];return a instanceof cb?a:null},pb="__closure_events_fn_"+(1E9*Math.random()>>>0),hb=function(a){L(a,"Listener can not be null.");if("function"==I(a))return a;L(a.handleEvent,"An object listener must have handleEvent method.");a[pb]||(a[pb]=function(b){return a.handleEvent(b)});return a[pb]};var rb=function(a,b,c){var d=qb[c];if(!d){var e=wa(c),d=e;void 0===a[y][e]&&(e=(R?"Webkit":Q?"Moz":P?"ms":Ha?"O":null)+xa(e),void 0!==a[y][e]&&(d=e));qb[c]=d}(c=d)&&(a[y][c]=b)},qb={};var sb=function(a,b){var c=[];1<arguments[D]&&(c=l[E][fa][F](arguments)[fa](1));var d=Qa(g,"th","tct-selectall",a);if(0!=d[D]){var d=d[0],e=0,f=Qa(g,"tbody",null,a);f[D]&&(e=f[0].rows[D]);this.d=Ua("input",{type:"checkbox"});d.appendChild(this.d);e?gb(this.d,"click",this.u,!1,this):q(this.d,!0);this.e=[];this.g=[];this.i=[];d=Qa(g,"input",null,a);for(e=0;f=d[e];e++)"checkbox"==f[C]&&f!=this.d?(this.e[z](f),gb(f,"click",this.q,!1,this)):"action"==f[ga]&&(0<=c[B](f[A])?this.i[z](f):this.g[z](f),q(f,
!0))}};G=sb[E];G.e=null;G.a=0;G.d=null;G.g=null;G.i=null;G.u=function(a){for(var b=a[ha][ea],c=a=0,d;d=this.e[c];c++)d.checked=b,a+=1;this.a=b?this.e[D]:0;for(c=0;b=this.g[c];c++)q(b,!this.a);for(c=0;b=this.i[c];c++)q(b,1!=a?!0:!1)};G.q=function(a){this.a+=a[ha][ea]?1:-1;this.d.checked=this.a==this.e[D];a=0;for(var b;b=this.g[a];a++)q(b,!this.a);for(a=0;b=this.i[a];a++)q(b,1!=this.a?!0:!1)};var tb=function(){var a=T(g,"kinds");a&&new sb(a);(a=T(g,"pending_backups"))&&new sb(a);(a=T(g,"backups"))&&new sb(a,"Restore");var b=T(g,"ae-datastore-admin-filesystem");b&&gb(b,"change",function(){var a="gs"==Va(b);T(g,"gs_bucket_tr")[y].display=a?"":"none"});if(a=T(g,"confirm_delete_form")){var c=T(g,"confirm_readonly_delete");c&&(a.onsubmit=function(){var a=T(g,"confirm_message");if(J("color"))rb(a,"red","color");else for(var b in"color")rb(a,"color"[b],b);return c[ea]})}},V=["ae","Datastore",
"Admin","init"],Z=H;V[0]in Z||!Z.execScript||Z.execScript("var "+V[0]);for(var ub;V[D]&&(ub=V[r]());)V[D]||void 0===tb?Z=Z[ub]?Z[ub]:Z[ub]={}:Z[ub]=tb;

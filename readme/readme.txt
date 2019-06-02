plugin for CudaText.
works for CSS lexers: CSS, SCSS, Sass, LESS, Stylus and HTML.
uses database of site htmlbook.ru.

when single-line selection is made, plugin finds such CSS property in its database and shows information about that property in the statusbar. for example, if property is [IE 9.0+, Chrome 19.0+/26.0+, Firefox 16.0+, etc], plugin shows: "IE 9; Chr 19/26; Mz 16".

IE: Internet Explorer
Chr: Chrome
Op: Opera
Sf: Safari
Mz: Firefox
An: Android
iOS: iOS

config file is available, use menu item: Options / Settings-plugins / CSS Property Info / Config.
option "status_alt": if "1", then result will be shown in the alternative (yellowish) statusbar.

author: Medvosa, https://github.com/medvosa
license: MIT

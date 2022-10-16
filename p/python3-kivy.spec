Name:           python3-kivy
Version:        2.1.0
Release:        1
URL:            http://kivy.org/
Summary:        Hardware-accelerated multitouch application library
License:        LGPL-3.0
Group:          Development/Languages/Python
Source:         https://github.com/kivy/kivy/releases/download/%{version}/Kivy-%{version}.tar.gz
BuildRequires:  mesa-libGL-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  gstreamer1-devel SDL2_ttf-devel SDL2_image-devel SDL2_mixer-devel git
Requires:       mtdev
Requires:       python3-pillow
Requires:       python3-pygame

%description
Kivy is an open source software library for rapid development of applications
that make use of innovative user interfaces, such as multi-touch apps.

%package examples
Summary:        Hardware-accelerated multitouch application library - Examples
Group:          Documentation/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description examples
Kivy is an open source software library for rapid development of applications
that make use of innovative user interfaces, such as multi-touch apps.

This package contains the developer examples

%prep
%setup -q -n Kivy-%{version}
#sed -i "s|data_file_prefix = 'share/kivy-'|data_file_prefix = '%{_docdir}/%{name}/'|" setup.py
#sed -i "s|#!/usr/bin/python||" kivy/lib/osc/OSC.py # Fix non-executable script
#rm examples/demo/pictures/images/.empty # Remove empty file
#rm -r examples/audio # Remove content with non-commercial only license (bnc#749340)

%build
CFLAGS="%{optflags} -fno-strict-aliasing" python3 setup.py build
#cd doc && make html && rm -r build/html/.buildinfo # Build HTML documentation

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%doc AUTHORS LICENSE *.md
%{python3_sitearch}/*

%files examples
%{_datadir}/kivy-examples

%changelog
* Sun Oct 09 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.0
- Rebuilt for Fedora
* Mon Dec 17 2012 saschpe@suse.de
- Update to version 1.5.1:
  + Widgets
  - [#847] Avoid to react on scrollleft/right on Button + FileChooser
  + Graphics
  - [#856] Fix Line instruction
  + Examples
  - [#848,#855] Fix Kivy catalog to work from a different cwd
- Changes from version 1.5.0:
  + Core
  - [#731] BoundedNumericProperty can have float bounds
  - [#755] Fix SetWindowLongPtr on 32/64 Windows
  - [#768] Fix AsyncImage loader on iOS
  - [#778] Prevent the Pygame parachute if we don't have the required
  - [#779] Better DPI support, with new sp and dp units
  - [#783] New screen module for simulating different DPI devices
  - [#789] Fix on_resize dispatch on Windows and OSX
  - Allow multiple providers in Kivy env variables
  - Fix line off-by-one issue in Kv errors
  - New errorhandler/errorvalue in Property class
  - New experimental X11 window provider, that support transparent
  - Normalize android pressure and radius
  - Reduce gstreamer audio/video out-of-sync
  - Support ability to stop/restart the EventLoop
  + Graphics
  - [#481] Avoid error in case of multiple Canvas.rremove()
  - [#610] Add more information when GLEW fail to initialize
  - [#671] Allow source unicode filename in BindTexture
  - [#790] Allow to change Stencil operators
  - Avoid BGRA->RGBA conversion for OSX if the GPU support BRGA.
  - Fix issue with Cython 0.14, "by" is now considered as a keyword
  - Line: add bezier and bezier_precision properties
  - Line: fix missing ellipse/circle/rectangle in the Line constructor
  - Texture: always flip the texture vertically for Image and Label
  + Widgets
  - [#618] Raise exception if ScreenManager.start() is called twice
  - [#648] Avoid touch event propagation on ScreenManager transition
  - [#662] Enhance TextInput performance
  - [#706] Fix pos_hint Boxlayout calculation
  - [#725] Fix collapse management in Accordion
  - [#734] Fix widget opacity when passed in the constructor
  - [#736] Fix slider bug when min < 0, max < 0 and step > 0
  - [#737] Better swipe gesture detection for Carousel
  - [#747] Honor index in Carousel.add_widget() (and Bubble)
  - [#750] New CodeInput widget
  - [#771] Dispatch modalview.on_open after animation
  - [#785] Allow event binding in Widget constructor
  - [#819] Fix canvas positioning when inserting at first position
  - [#824] Add top-to-bottom + right-to-left Stacklayout orientations.
  - [#832] Fix shorten routine
  - Automatically register new Widget classes in Factory
  - Enhance ScrollView scrolling
  - Fix Carousel API, containers are now hidden, and
  - Fix Label.color property for markup labels
  - Multiples fixes to TabbedPanel (tab_strip, unbind, tab selection)
  + Others
  - [#670] New compass demo for Android using sensors
  - Many many fixes on the documentation, thanks for all the PR!
  - New KivyCatalog example: interactive Kv editor
  - Started Guide 2.0
* Mon Oct 22 2012 dmacvicar@suse.de
- Update to version 1.4.1:
  + Core
  - [#625] Extend NumericProperty to support DPI notation
  - [#660] Add callbacks support on ConfigParser for a (section, key)
  - [#666] Fix Markup text disapear on GL reloading
  - [#678] Enhance UrlRequest for small chunks, callbacks and GC
  - [#679] New Audio.get_pos()
  - [#680] Fix key translations on Keyboard
  - Force on_parent dispatching for children in a kv rule
  - Expose 'app' instance keyword in Kv language
  + Graphics
  - [#686] Added opacity support in the graphics pipeline
  - Enhanced Line instruction that support width, joint, cap.
  - Added Line.circle/ellipse/rectangle properties
  + Widgets
  - [#664] Fix TextInput crashes is some cases
  - [#686] New Widget.opacity property
  - [#690] New TextInput.background_normal/active
  - [#694] Fix Slider value when min and step > 0
  - [#676] Fix Carousel.remove_widget()
  - [#669] Fix SettingNumeric with int/float values
  - [#698] Enhance BoxLayout to support pos_hint
  - Fix ModalView background property
  + Windows
  - [#675] Fix WM_Touch / WM_Pen for 32 bits / 64 bits
  + Others
  - [#462] Fixes gstreamer packaging with PyInstaller
  - [#659] Updated documentation concerning PyInstaller 2.0
- Changes from 1.4.0:
  + Core
  - [#513] Fix nested template
  - [#547] Fix url loader with querystring
  - [#576] Markup text can be vertically aligned
  - [#585] Enhance add_widget() to raise an Exception on multiple parents
  - [#642] Support of smb:// in url loader with pysmb
  - Enhance AliasProperty to cache the result if use_cache is set to True
  - Enhance App.get_application_config() to get a correct config filename on all platforms
  - Fix Animation.stop_all() + new Animation.cancel()
  - Fix Property.unbind() for bounded methods
  + Graphics
  - [#516] Fix crash when loading 1bit image
  - [#546] Fix Quad() initialization
  + Widgets
  - [#543] Fix multiple content in TabbedPanel from Kv
  - [#549] Enhance TabbedPanel to introduce default_tab_class
  - [#562] Popup can now define the content in Kv
  - [#593] Enhance TextInput with select_all() and select_text() methods
  - [#658] Fix usage of Camera within Kv
  - Enhanced VideoPlayer to have pause ability and state property
  - Enhance Image widget to add keep_data for further pixel collision detection
  - New Carousel widget
  - New Checkbox widget
  - New Dropdown widget
  - New ModalView widget
  - New RelativeLayout, identical from FloatLayout with relative coordinates
  - New ScreenManager widget for changing views with transitions
  - New Slider.step property
  - New Spinner widget
  + Windows
  - [#621] Fix ghost touch due to a raise condition
  - Add python scripts into the PATH
  - Enhance input wm_touch/pen to be compatible with 64bits
  - Severals fixes around window resizing
  + Others
  - New Getting Started
  - Tons of documentation typo, fixes. Really, a ton.
* Tue Jun 26 2012 saschpe@suse.de
- Update to version 1.3.0:
  + Core
  - [#420] Fix pygame error when texture is too large
  - [#450] Updated Sound class to use Kivy properties
  - [#467] New Sound.length
  - [#484] New kivy.interactive module: doesn't break REPL anymore
  - [#487] Make default values in properties optionals
  - [#489] Replaced all relative import with absolute imports
  - [#498] Fixes Image to allow re-loading of image from disk
  - [#503] Renamed unicode parameter to codepoint in all on_key_*
  - Changed default screenshot to be PNG instead of JPEG
  - Enhance Kv lang rules lookup
  - Enhance Label initialitazion
  - Fixes crash on App when the configuration file cannot be read
  - Fixes for graphics reloading mechanism, force the GC before
  - New default UI theme
  - New KIVY_NO_CONFIG, KIVY_NO_FILELOG, KIVY_NO_CONSOLELOG env
  - New kivy.utils.escape_markup() to escape untrusted text when
  - Support MacOSX clipboard
  + Graphics
  - [#118] Fixes for glColorMask on android
  - [#447] Add new ClearColor and ClearBuffers instructions
  - [#463] Fixes glGetIntegerv with new Cython
  - [#479] Fixes for Translate instance when args passed in on
  - Avoid drawing of empty VBO
  - Enhance Stencil instruction, you can nest up to 128 layers instead
  - Fixes crash when texture is empty (0px width or height)
  - Fixes Point instruction when new point is appended
  - Fixes to enable support of NPOT texture on android/ios platform
  + Widgets
  - [#401] New Scatter.do_collide_after_children property
  - [#419] New TabbedPanel widget
  - [#437] New TextInput.readonly property
  - [#447] Fix popup background resizing when Window resize
  - [#480] Fixes StackLayout size_hint missing calculation
  - [#485] Fixes VideoPlayer scrollbar with multitouch
  - [#490] Fixes ToggleButton memory leak
  - Add FileChooser.file_encodings for a better unicode conversion
  - Better handling of mousewheel in Button
  - Delayed Label texture creation
  - Enhance RST widget to support :align: in image directive
  - Fixes RST widget to use document root for loading images and
  - New Popup.dismiss(animation) attribute to disable the fadeout when
  - New RstDocument.goto(reference) for scrolling the document to a
  - New Undo/Redo for TextInput
* Fri May  4 2012 prusnak@opensuse.org
- Updated to version 1.2.0
  * Core
  - [#325] New Window.mouse_pos to get the main mouse position anytime
  - [#427] Improved markup positioning with glpyhs+kerning
  - Avoid rendering of empty text lines
  - Fixed setter() and getter() EventDispatcher methods
  - Implement new Dropfile event, to be able to open files on macosx
  - Optimized texture upload from 3 to 1 upload in somes cases
  - The system/Window can now "pause" the application if the app support it
  * Graphics
  - Disable mipmapping for people using Desktop GL kivy < 3.0
  - Enhanced graphics engine to support OpenGL reloading / context-lost
  - Optimized shaders uniform upload if not used
  - Optimized VBO drawing by using a GPU buffer for storing indices
  * Modules
  - [#415] Recorder now record keyboards events
  - [#309] Fixes for inspector / memory leak
  - New webdebugger module for having statistics on the current running app
  * Widget
  - [#331] New VideoPlayer widget: Video + controls buttons, annotations and
  - [#411] Propagate touchs to children for Label and Button
  - [#412] Removed redundant background_texture on Bubble
  - [#416] New background_color and foreground_color to TextInput
  - [#429] New password mode to TextInput
  - [#431] Fixes clipboard for linux, works perfect on linux, windows and mac
  - [#439] Improve performance on TextInput dealing with large text
  - Enhanced FileChooser to delay the file creation over the time, and display
  - Enhance FileChooser to animate when scrollwheel is used
  - Enhance scrollview to animate when scrollwheel is used
  - Fixed Bubble not listening to color changes
  - New FileChooser.rootpath to restrict file browsing
  - New scrollview scrollbar (not touchable)
  - New ".. video::" directive in the RstDocument widget
  - New Video.seek() method
  - Updated filechooser icon theme
  * Examples
  - [#405] New examples dealing with unicode
  * Others
  - [#404] Fixes for msvc9 compilation errors
  - [#424] Fixed pyinstaller packaging for macosx
  - Add installation instructions for mageia
  - New instructions for packaging on iOS
* Wed Feb 29 2012 saschpe@suse.de
- Remove content with non-commercial only license (bnc#749340)
* Mon Feb 20 2012 saschpe@suse.de
- Updated runtime requirements
* Mon Feb 20 2012 saschpe@suse.de
- Update to version 1.1.1:
  * Core
  - [#403] Pygame audio loader doesn't work (in addition to camera opencv provider)
- Changes from version 1.1.0:
  * Core
  - [#319] Allow dynamic changes to url in Loader
  - [#371] Allow BoundedNumericProperty to have custom min/max per widget
  - [#373] Allow Property.dispatch() to be called from Python
  - [#376] Fix list.reverse() in ListProperty
  - [#386] Fix GC with Clock triggered events
  - [#306] Fix video uri support with gstreamer
  - Add support for italic/bold text in core/text
  - Better traceback when an exception happen within kv
  - Enhance properties exceptions
  - Fixes for camera frame update
  - Fixes for python-for-android project
  - Fixes list/dict properties on pop/popitem method
  - Merged android-support branch to master
  - New Atlas class for merging png/jpeg and acces with atlas://
  - New SettingPath in settings
  - New markup text rendering: "[b]Hello[/b] [color=ff0000]World[/color]"
  - New on_pause handler in App: used in android for sleeping
  - Removed text/cairo rendering, ttf doesn't work.
  - Various speedup on cython files
  * Graphics
  - [#375] Fix clear_color in Fbo
  - [#64] New Mesh instruction for custom 2D mesh
  - Fix black screenshot on GLES devices
  - Fix warnings of cython compilation + debian issues
  * Modules
  - [#389] Fix missing image for Touchring
  - New recorder module: you can save and replay touch events
  * Input
  - [#366] Fix time_end never set for all providers except mouse
  - [#377] Removed TUIO provider by default in configuration
  * Lang
  - [#364] Fixes for unicode BOM in .kv
  - Rewrite kvlang parser / builder: improved performance + fixes some design
  * Widget
  - [#317,#334,#335] Fix AsyncImage when source is empty or already loaded
  - [#318] Fix textinput auto scroll
  - [#386] Scatter will not accept touches if none of transformations are enabled
  - [#395] Enhance doc for label/textinput about unicode chars
  - Enhance FileChooser for feedback when item is selected
  - Enhance FileChooser to have a directory selection mode
  - Enhance Popup with more properties for styling
  - Fixes for Textinput focus
  - Fixes Layout when parent are changing
  - Fix for not propagating touch events in Popup
  - Fix Textinput with invalid selection when releasing shift key
  - New Bubble widget, for displaying contextual menu
  - New Copy/Cut/Paste menu in Textinput using Bubble
  - New RstDocument widget, for rendering RST text
  - See http://kivy.org/#changelog for more detail...
- Build HTML documentation and split out doc package
- Fixed several rpmlint issues
* Fri Sep 23 2011 saschpe@suse.de
- Update to version 1.0.7:
  * Core
  - [#32] Implement window rotation (0,90,180,270)
  - [#150] Fix to prevent gcc bug on Mageia
  - [#153] Add packaging doc and hooks for Windows and MacOSX
  - [#155] Replaced import in class methods with late binding
  - [#157] Implement Label.valign support
  - [#166] Prevent to open too many fonts at the same time
  - [#184] Remove unlink() in properties, not needed anymore
  - [#186] Fixes extension support for MacOSX
  - Disable window resizing until we are OpenGL context resistant
  - Enhance extensions wizard and auto-created setup.py
  - Enhance pixels from pygame surface
  - Enhance properties list to prevent memory leak
  - Enhance properties to store data inside Widget class
  - Fixes for Audio class creation
  - Fixes for Clock dictionnary crashes
  - Fixes for volume usage on gstreamer video implementation
  - Fixes infinite loop when we hit max iteration
  - Fixes ordering of Window.add_widget
  - Fixes to avoid resync error with gstreamer
  - New DDS Image loader using new S3TC support
  - New DictProperty property
  * Graphics
  - [#27] Implement mipmap support
  - [#130] Implement caching for Shader source/compilation result
  - [#161] Prevent to upload texture twice when NPOT is supported
  - [#182] Fix Rotation.angle caching with degrees/radians
  - [#190] Fix crash when too many vertices are pushed in VBO
  - Enhance Ellipse to add angle_start/angle_end properties
  - Enhance GridLayout to have minimum and default size per col/row
  - Enhance logging of OpenGL capabilities
  - Enhance texture memory by using native NPOT if available
  - Enhance texture upload by using the best pixel packing
  - Fixes Color.hsv property crashes
  - Fixes for GLES2 by using GL_UNSIGNED_SHORT in VBO
  - Fixes some typo on OpenGL wrapper
  - New $HEADER$ token that can be used in fragment/vertex shader code
  - New OpenGL Utils module for checking texture capabilities and others
  - New S3TC texture support
  - New Texture.colorfmt property
  * Input
  - Enhance Wacom support on linux platform
  - Fix leak/slowdown in MouseMotionEvent
  * Lang
  - [#189] Fixes for not allowing dot in properties name
  - Concat property value when the value is shifted to one level
  - Enhance key resolution ([x for x in list] can be used now.)
  - Enhance module/class resolution at import
  * Widget
  - [#139] Add TreeView.remove_node()
  - [#143] Fix crash when group is changing on ToggleButton
  - [#146] Fix invalid calculation for Image.norm_image_size
  - [#152] Fix Camera.play property
  - [#160] Prevent label creation until text is set
  - [#178] Set default values only on properties
  - Enhance ScrollView to have kind of kinetic movement
  - Fixes calculation of Stacklayout.size with padding
  - Fixes FloatLayout relayout when children size* is changing
  - Fixes for initial Label.font_name assignement
  - Fixes to prevent call of on_release twice
  - Fix ScrollView with grab events
  - New Image.allow_stretch property
  - New Popup (modal popup) widget
  - New Settings widget
  - New Switch widget
  - New Widget.uid property
* Fri Jun 24 2011 saschpe@gmx.de
- Initial version

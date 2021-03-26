URL:            http://moblin.org/
Summary:        Cairo integration for Clutter
Name:           clutter-box2d
Version:        0.10_20090803
Release:        1
License:        LGPLv2.1+
Group:          System/Libraries
Source0:        http://www.clutter-project.org/sources/clutter-box2d/0.10/%{name}-%{version}.tar.bz2
BuildRequires:  gtk2-devel pango-devel xmlto cairo-devel
BuildRequires:  clutter-devel >= 1.0
BuildRequires:  gtk-doc >= 1.4
BuildRequires:  gcc-c++

%description
Clutter is an open source software library for creating fast, visually
rich and animated graphical user interfaces. It uses OpenGL for drawing
primitives and has multiple backends, allowing its usage on different
platforms.

A glue layer between clutter and box2d that provides a special group where the
actors can be set to be static or dynamic in regard to a physics simulation. The
source tree currently contains an embedded version of box2d trunk.

Authors:
--------
         Matthew Allum <mallum@o-hand.com> - primary authour  
         Emmanuele Bassi <ebassi@o-hand.com> - python bindings, gobject/glib mastery  
         Iain Holmes <iain@o-hand.com> - GTK Clutter widget  
         Jorn Baayen <jorn@o-hand.com> - Gstreamer bits  
         Chris Lord <chris@o-hand.com> - Pixel shader bits 

%package devel
License:        LGPLv2.1+
Summary:        Cairo integration for Clutter
Requires:       clutter-box2d = %{version}  
Requires:       gtk2-devel
Requires:       clutter-devel >= 1.0
##Requires:       box2dreamer-0_10-devel box2dreamer-0_10-plugins-base-devel
Group:          System/Libraries

%description  devel
Clutter is an open source software library for creating fast, visually
rich and animated graphical user interfaces. It uses OpenGL for drawing
primitives and has multiple backends, allowing its usage on different
platforms.

Header files and libraries for building a extension library for the
clutter-box2d.

Authors:
--------
         Matthew Allum <mallum@o-hand.com> - primary authour  
         Emmanuele Bassi <ebassi@o-hand.com> - python bindings, gobject/glib mastery  
         Iain Holmes <iain@o-hand.com> - GTK Clutter widget  
         Jorn Baayen <jorn@o-hand.com> - Gstreamer bits  
         Chris Lord <chris@o-hand.com> - Pixel shader bits 

%package doc
License:        LGPLv2.1+
Summary:        GStreamer integration for Clutter
Group:          System/Libraries

%description doc
Clutter is an open source software library for creating fast, visually
rich and animated graphical user interfaces. It uses OpenGL for drawing
primitives and has multiple backends, allowing its usage on different
platforms.

Authors:
--------
         Matthew Allum <mallum@o-hand.com> - primary authour  
         Emmanuele Bassi <ebassi@o-hand.com> - python bindings, gobject/glib mastery  
         Iain Holmes <iain@o-hand.com> - GTK Clutter widget  
         Jorn Baayen <jorn@o-hand.com> - Gstreamer bits  
         Chris Lord <chris@o-hand.com> - Pixel shader bits 

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
./autogen.sh
%configure  --enable-gtk-doc --disable-static
make %{?jobs:-j%jobs}  

%install
DESTDIR=$RPM_BUILD_ROOT make install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README COPYING ChangeLog
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/clutter-1.0/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/girepository-1.0/ClutterBox2D-0.10.typelib
%{_datadir}/gir-1.0/ClutterBox2D-0.10.gir

%files doc
%{_datadir}/gtk-doc/html/clutter-box2d

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.10_20090803
- Rebuild for Fedora
* Tue Jun  8 2010 awafaa@opensuse.org
- Update to version 0.10_20090803
* Thu Aug  6 2009 glin@novell.com
- Update to commit dae84a82efe22b284cba8ca1985ce14bb4e86c99
- Clean up clutter-box2d.spec
* Thu Jun 11 2009 michael.meeks@novell.com
- Update to commit f6f8994a4666bcc79985396a3a0a09320db2b9f0

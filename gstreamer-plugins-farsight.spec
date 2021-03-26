Name:          gstreamer-plugins-farsight
Version:       0.12.11
Release:       9.1
Summary:       Gstreamer plugin for farsight
Group:         System/Multimedia
URL:           http://farsight.freedesktop.org
Source:        http://farsight.freedesktop.org/releases/gst-plugins-farsight/gst-plugins-farsight-%{version}.tar.gz
License:       LGPL
BuildRequires: gcc-c++, GConf2-devel
BuildRequires: gstreamer-plugins-base-devel
BuildRequires: libxml2-devel
BuildRoot:     %{_tmppath}/%{name}-%{version}-root

%description
Gstreamer plugin for farsight.

%prep
%setup -q -n gst-plugins-farsight-%{version}
sed -i 's|glib/gthread\.h|glib.h|' gst/rtpjitterbuffer/async_jitter_queue.h

%build
%configure
make

%install
rm -rf "$RPM_BUILD_ROOT"
%makeinstall

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%{_libdir}/gstreamer-0.10/lib*.la
%{_libdir}/gstreamer-0.10/lib*.so
%doc AUTHORS COPYING COPYING.LIB README

%changelog
* Wed Jun 15 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.12.11
- Rebuild for Fedora

* Wed Nov 18 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 0.12.11-1mamba
- package created by autospec

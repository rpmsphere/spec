%global debug_package %{nil}
%global url_ver	%(echo %{version} | tr '.' '_')

Name:		qstopmotion
Version:	2.5.2
Release:	1
Summary:	Creates stop-motion animation movies based on Qt5
License:	GPLv3+
Group:		Video/Utilities
URL:		http://www.qstopmotion.org/
Source0:	https://sourceforge.net/projects/qstopmotion/files/Version_%{url_ver}/%{name}-%{version}-Source.tar.gz
BuildRequires:	cmake
BuildRequires:	qt5-qttools-devel
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(libgphoto2)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	qwt-qt5-devel
BuildRequires:	qt5-qtmultimedia-devel

%description
qStopMotion is a application for creating stop-motion animation movies.
The users will be able to create stop-motions from pictures imported from
a camera or from the harddrive and export the animation to different video
formats such as mpeg or avi.

%prep
%setup -q -n %{name}-%{version}-Source
#chmod 0644 Changes.txt README.txt
sed -i 's|args != NULL|va_arg(args, const char *) != NULL|' src/technical/grabber/gphoto2/gpgrabber.cpp

%build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_CXX_FLAGS=-Wno-format-security .
%make_build

%install
%make_install

%files
%doc AUTHORS Changes.txt README.txt
%doc %{_docdir}/%{name}
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}.1.*

%changelog
* Sun Apr 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5.2
- Rebuild for Fedora
* Wed Aug 10 2016 daviddavid <daviddavid> 2.3.1-1.mga6
+ Revision: 1045282
- initial package qstopmotion

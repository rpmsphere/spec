%undefine _debugsource_packages

Name:           screencloud
License:        GPL-2.0
Group:          Productivity/Networking/Other
Summary:        Easy to use screenshot sharing application
Version:        1.5.3
Release:        1
Source0:        %{name}-%{version}.tar.gz       
URL:            https://screencloud.net
BuildRequires:  gcc-c++ cmake
BuildRequires:  libqxt-qt5-devel PythonQt-devel quazip-devel

%description
Take a screenshot using one of the 3 hotkeys or simply click the
ScreenCloud tray icon. You can choose where you want to save your screenshot.

If you choose to upload your screenshot to the screencloud website, a
link will automatically be copied to your clipboard. You can share
this link with your friends or colleagues via email or in an IM
conversation. All they have to do is click the link and look at your screenshot.

ScreenCloud also offers FTP and SFTP uploading if you want to use
your own server.

Authors:
--------
    Olav S. Thoresen <olav.s.th@gmail.com>

%prep
%setup -q

%build
export CXXFLAGS="-std=c++98 -fPIC"
%cmake .
%cmake_build
 
%install
%cmake_install
mkdir -p $RPM_BUILD_ROOT/usr/bin
ln -sf /opt/screencloud/screencloud.sh $RPM_BUILD_ROOT/usr/bin/screencloud

%files
%{_bindir}/%{name}*
%{_datadir}/applications/*.desktop
%{_docdir}/screencloud
%{_datadir}/icons/hicolor/*/apps/screencloud.*
%{_datadir}/metainfo/*.xml
%{_datadir}/screencloud/modules/ScreenCloud.py

%changelog
* Sun Apr 11 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.3
- Rebuilt for Fedora
* Sat Feb 14 2015 Olav Sortland Thoresen <olav.s.th@gmail.com> - 1.2.0
- Added screenshot editor
- Fixed audio output sometimes crashing the application
* Sun Mar 30 2014 Olav Sortland Thoresen <olav.s.th@gmail.com> - 1.1.6
- Fixed plugin list not loading (url has changed)
- Made more strings translatable
- Fixed running on startup not working on OS X
* Sun Mar 30 2014 Olav Sortland Thoresen <olav.s.th@gmail.com> - 1.1.5
- Fixed plugin update check
- Added changelog button to update notifications
* Sat Mar 22 2014 Olav Sortland Thoresen <olav.s.th@gmail.com> - 1.1.4
- Better multi monitor support
- Added check for plugin updates
- Better cli interface
* Sat Mar 1 2014 Olav Sortland Thoresen <olav.s.th@gmail.com> - 1.1.3
- New plugin format (python plugins)
- All URLs use https by default
- Removed various dependencies

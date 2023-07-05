Name:           linuxdcpp
Version:        1.1.0
Release:        13.2
License:        GPLv2
Summary:        A Linux port of the Direct Connect client DC++
URL:            https://launchpad.net/linuxdcpp
Group:          Productivity/Networking/File-Sharing
Source:         https://launchpad.net/linuxdcpp/1.1/%{version}/+download/%{name}-%{version}.tar.bz2
BuildRequires:  libpng-devel
BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  compat-openssl10-devel
BuildRequires:  pkgconfig
BuildRequires:	gtk2-devel
BuildRequires:	libglade2-devel
BuildRequires:	libnotify-devel
BuildRequires:  python2-scons

%description
LinuxDC++ is a Linux port of the Direct Connect client DC++. Though it is
primarily aimed at Linux, it has been shown to work on other Unix-based
operating systems as well. It is written in C++ and makes use of GTK+ for the
user-interface. LinuxDC++ is free and open source software licensed under the
GPL.

%prep
%setup -q
sed -i '190d' SConstruct

%build
CFLAGS="%{optflags}" CXXFLAGS="%{optflags} -std=gnu++98" scons FAKE_ROOT=$RPM_BUILD_ROOT PREFIX="%{_prefix}" release="true"

%install
scons install

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}
rm -rf $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/20x20

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc Changelog.txt Credits.txt License.txt Readme.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%exclude %{_datadir}/locale/*/LC_MESSAGES/*.mo

%changelog
* Mon May 07 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.0
- Rebuilt for Fedora
* Sun Jun  5 2011 tejas.guruswamy@opensuse.org
- Update to 1.1.0 release
  + Upgraded the DC++ core to 0.7091
  + Many bugfixes
* Mon Jan 10 2011 tejas.guruswamy@opensuse.org
- Update to bzr revision 403 from lp:linuxdcpp
* Sun Apr 25 2010 masterpatricko@gmail.com
- Update to bzr revision 366 from lp:linuxdcpp
* Sat Feb 20 2010 masterpatricko@gmail.com
- Add SuSEfirewall2 definition rules
  * To use, open the linuxdcpp settings and change on the Connection settings page
  Mode: Firewall / manual connection forward
  TCP port = 48494
  UDP port = 36732
* Sat Dec 12 2009 masterpatricko@gmail.com
- Initial build

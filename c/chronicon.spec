%global debug_package %{nil}

Name:    chronicon
Version: 0.2.6
Release: 14.1
Summary: Microblogging client for Twitter and StatusNet
License: GPLv2
Group:   Applications/Network
URL:     http://chronicon.sourceforge.net/
Source: %{name}-%{version}.tar.gz
Source2: %{name}.desktop
BuildRequires: libpng-devel
BuildRequires: pkgconfig(QtGui) >= 4.5
BuildRequires: pkgconfig(QtWebKit)
BuildRequires: pkgconfig(QJson)
BuildRequires: qca2-devel
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
Requires: qca-ossl

%description
An application to read and post on Twitter and StatusNet sites.

%prep
%setup -q

%build
sh configure --nonotify
make 

%install
rm -rf $RPM_BUILD_ROOT
install -p -d $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 bin/chronicon $RPM_BUILD_ROOT%{_bindir}
install -p -d $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m 755 %{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps
desktop-file-install                                    \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
%{SOURCE2}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
%doc COPYRIGHT
%doc chronicon/LICENSE
%doc chronicon/docu/helpman.html
%{_bindir}/chronicon
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Apr 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.6
- Rebuild for Fedora
* Tue Aug  9 2011 Bernd Stramm <bernd.stramm@gmail.com> - 0.2.6
- try to fix packaging issue

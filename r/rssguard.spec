Name:		rssguard
Version:	1.0.9
Release:	4.3
License:	GPL
Source:		%{name}-%{version}.tar.bz2
URL:		http://code.google.com/p/rss-guard/
Group:		Productivity/Networking/News/Utilities
Summary:	Qt-based RSS/Atom aggregator
BuildRequires:	gcc-c++, cmake, make, pkgconfig, pkgconfig(QtGui), pkgconfig(QtNetwork), pkgconfig(QtXml), pkgconfig(QtWebKit)
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%description
RSS Guard is useful and (very) tiny RSS 0.92/1.0/2.0 & ATOM 1.0 feed reader.
It can keep feeds organized in categories, update information from them
automatically and notice user if there is new message.

%prep
%setup -q

%build
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=release
make

%install
%{__rm} -rf $RPM_BUILD_ROOT
cd build
%{makeinstall} DESTDIR=$RPM_BUILD_ROOT

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
* Tue Aug 07 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.9
- Rebuilt for Fedora
* Mon Jan 16 2012 TI_Eugene <ti.eugene@gmail.com> 1.0.7
- Next version
- building with cmake
- standalone l10n files
* Wed Dec 28 2011 TI_Eugene <ti.eugene@gmail.com> 0.9.4
- Initital build in OBS

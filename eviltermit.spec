%global debug_package %{nil}

Name:		eviltermit
Version:	1.1.3.1
Release:	1
Summary:	Vte-based Terminal Emulator
Source:		http://www.calno.com/eviltermit/%{name}-%{version}.tar.gz
Source1:	eviltermit.desktop
URL:		http://www.calno.com/eviltermit/
Group:		System/Terminals
License:	GNU General Public License v2 (GPL)
BuildRequires:	vte-devel

%description
eviltermit is a VTE based, simplified termit terminal emulator.
Features:
* tabs
* right click to switch encoding
* configuration via editing config.h and recompilation (suck less style)

%prep
%setup -q
%__sed -i -e 's/KOI8-R/BIG5/' -e 's/CP866/EUC-TW/' -e 's/CP1251/GB2312/' src/config.h

%build
%configure
%__make

%install
%makeinstall
%__rm -rf "%{buildroot}%{_datadir}/doc"
%__install -D -m0644 "%{SOURCE1}" "%{buildroot}%{_datadir}/applications/eviltermit.desktop"

%clean
%__rm -rf "%{buildroot}"

%files
%doc Changelog COPYING TODO AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.3.1
- Rebuild for Fedora
* Fri Feb  8 2008 Pascal Bleser <guru@unixtech.be> 1.1.3
- monospace patch merged by upstream
- new upstream version
* Wed Jan 23 2008 Pascal Bleser <guru@unixtech.be> 1.1.2
- new upstream version
* Tue Dec 25 2007 Pascal Bleser <guru@unixtech.be> 1.1
- moved to openSUSE Build Service
- moved doc files from /usr/share/doc/eviltermit to /usr/share/doc/packages/eviltermit
- build changed to cmake
- new upstream version
* Tue Sep 25 2007 Pascal Bleser <guru@unixtech.be> 1.0.3-0.pm.1
- new upstream version
* Fri Sep  7 2007 Pascal Bleser <guru@unixtech.be> 1.0.2-0.pm.1
- moved to Packman
- new upstream version
* Tue Jul 17 2007 Pascal Bleser <guru@unixtech.be> 1.0.1-1
- new package

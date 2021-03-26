Name:           netsurf
Version:        3.9
Release:        1
Summary:        Lightweight Web Browser with its own layout and rendering engine
License:        GPL-2.0 and MIT
Group:          Productivity/Networking/Web/Browsers
Source0:        http://download.netsurf-browser.org/netsurf/releases/source-full/netsurf-all-%{version}.tar.gz
Source1:        netsurf.desktop
URL:            http://www.netsurf-browser.org/
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  gtk2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libglade2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmng-devel
BuildRequires:  openssl-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  zlib-devel
BuildRequires:  lcms-devel
BuildRequires:  gperf
BuildRequires:  check-devel
BuildRequires:  libidn-devel
BuildRequires:  perl-HTML-Parser

%description
NetSurf is a lightweight browser with its own layout and rendering engine 
entirely written from scratch. It is small and capable of handling many 
of the web standards in use today.

Authors:
--------
    Rob Kendrick <rjek@netsurf-browser.org>    

%prep
%setup -q -n netsurf-all-%{version}

%build
make PREFIX=/usr

%install
%make_install PREFIX=/usr
install -D -m0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Jul 23 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 3.9
- Rebuild for Fedora
* Sun May 13 2012 andreas.stieger@gmx.de
- update to upstream 2.9
  For a full list of changes, see:
  http://www.netsurf-browser.org/downloads/releases/ChangeLog.txt
- switch to full upstream source tarball with in-tree libraries
- move changelog to .changes file
- remove start script and use binary names as per upstream
- license is GPL-2.0 and MIT
- reformat spec file and add in-tree dependency libraries
- update patches to compile with flags
- add backported upstream netsurf-2.9-libcss-enum-compare.patch
  to compile without -Wno-error=enum-compare
- update .desktop file
* Fri Jun 19 2009 pascal.bleser@opensuse.org
- update to 2.1
* Fri May  1 2009 pascal.bleser@opensuse.org
- update to 2.0
- use latest lempar.c and lemon.c from sqlite
* Sun Mar 23 2008 guru@unixtech.be
- new package

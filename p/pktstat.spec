Name:           pktstat
Version:        1.8.5
Release:        1
License:        Public Domain
BuildRequires:  ncurses-devel libpcap-devel
Group:          Productivity/Security
Summary:        Real-time interface traffic viewer for curses
Source:         %{name}-%{version}.tar.gz

%description
Real-time interface traffic viewer for curses.

%prep
%setup -q

%build
autoreconf -fis
CFLAGS="%{optflags} -Wno-format-security"
CXXFLAGS="%{optflags} -Wno-format-security"
export CFLAGS
export CXXFLAGS
export LDFLAGS="-Wl,--as-needed"
%configure --disable-static --with-pic
%{__make} %{?jobs:-j%jobs}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%{_bindir}/pktstat
%doc %{_mandir}/man1/*

%changelog
* Mon Oct 07 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8.5
- Rebuild for Fedora
* Wed Aug  8 2007 crrodriguez@suse.de
- fix build in factory

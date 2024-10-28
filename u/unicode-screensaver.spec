Name:           unicode-screensaver
Version:        0.5
Release:        4.1
Summary:        Screensaver with a random Unicode Character
Source0:        https://www.joachim-breitner.de/archive/unicode-screensaver/%{name}-%{version}.tar.gz
Source1:        %{name}.png
URL:            https://www.joachim-breitner.de/projects
Group:          Amusements/Toys/Screensavers
License:        MIT/X
BuildRequires:  libX11-devel libXmu-devel libXft-devel
BuildRequires:  gcc make glibc-devel pkgconfig
BuildRequires:  autoconf automake libtool

%description
The unicode-screensaver is a simple screensaver application that repeatedly
randomly picks an unicode character and displays it in a very large font size
together with its unicode code point and the character name.

Authors:
--------
    Joachim Breitner <mail@joachim-breitner.de>

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure \
     --with-hackdir="%{_libdir}/xscreensaver" \
     --with-desktopdir="%{_datadir}/applications" \
     --with-configdir="%{_sysconfdir}/xscreensaver"

%__make %{?_smp_flags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
sed -i 's|^OnlyShowIn=.*|Icon=%{name}|' $RPM_BUILD_ROOT%{_datadir}/applications/unicode.desktop

%files
%doc README
%dir %{_sysconfdir}/xscreensaver
%config(noreplace) %{_sysconfdir}/xscreensaver/unicode.xml
%dir %{_libdir}/xscreensaver
%{_libdir}/xscreensaver/unicode
%{_datadir}/applications/unicode.desktop
%{_mandir}/man6/unicode.6*
%{_datadir}/pixmaps/%{name}.png

%changelog
* Fri Feb 26 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5
- Rebuilt for Fedora
* Mon Jun  6 2011 pascal.bleser@opensuse.org
- update to 0.4:
  * this version was updated for Unicode 6.0
* Mon Jun 21 2010 pascal.bleser@opensuse.org
- update to 0.3:
  * problems with the random number generator were fixed
* Thu Dec 17 2009 pascal.bleser@opensuse.org
- update to 0.2:
  * colors are configurable
* Thu Dec 10 2009 pascal.bleser@opensuse.org
- initial package (0.1)

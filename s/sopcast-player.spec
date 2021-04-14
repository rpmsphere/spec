Name:          sopcast-player
Version:       0.8.5
Release:       10.1
Group:         Applications/Internet
Summary:       A GUI front-end to SopCast
License:       GPLv2+
URL:           http://code.google.com/p/sopcast-player/
Source0:       http://sopcast-player.googlecode.com/files/%{name}-%{version}.tar.gz
BuildArch:     noarch
BuildRequires: gettext
BuildRequires: python2
BuildRequires: python2-setuptools
BuildRequires: desktop-file-utils
Requires:      vlc
Requires:      python2-vlc
Requires:      sopcast
Requires:      hicolor-icon-theme 
Requires:      pygtk2-libglade

%description
SopCast Player is designed to be an easy to use Linux GUI front-end for the p2p
streaming technology developed by SopCast. SopCast Player features an 
integrated video player, a channel guide, and bookmarks. Once SopCast Player is
installed it simply "just works" with no required configuration. 

%prep
%setup -q -n %{name}

%build
export PYTHON=/usr/bin/python2
make %{?_smp_flags}

%install
rm -fr $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
%find_lang %{name}

%clean
rm -fr $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc AUTHORS COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Mon Oct 07 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.5
- Rebuilt for Fedora
* Fri Jun 12 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.3.0-1
- New upstream release
* Sun Feb 22 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.2.1-2
- SPEC file revised for RPMFusion
* Tue Feb 17 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.2.1-1
- Initial build

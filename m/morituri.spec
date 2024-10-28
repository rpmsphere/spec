Name:           morituri
Version:        0.2.3
Release:        7.1
Summary:        CD ripper aiming for accuracy over speed
License:        GPLv3
Group:          Sound
URL:            https://thomas.apestaart.org/%{name}/trac
Source0:        https://thomas.apestaart.org/download/%{name}/%{name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  python2-setuptools
#BuildRequires: python2-gstreamer
#BuildRequires: python2-gobject
Requires:       cdparanoia
Requires:       cdrdao >= 1.2.3
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good >= 0.10.16
Requires:       python2-gstreamer
Requires:       python2-musicbrainz2
Requires:       python2-pycdio
Requires:       python2-pyxdg
Requires:       python2-CDDB
Requires:       python2-pkg-resources
Requires:       python2-setuptools

%description
Morituri is a CD ripper that aims for accuracy over speed. Its features are
modeled to compare with Exact Audio Copy on Windows.
It features support for:
* MusicBrainz for metadata lookup,
* AccurateRip verification,
* detection of sample read offset of drives,
* test and copy of a rip,
* the ability to detect and rip Hidden Track One Audio,
* templates for file and directory naming,
* lossless enconding and lossy enconding or re-encoding of rip images,
* tagging using GStreamer (including embedding MusicBrainz id's),
* retagging of rip images,
* plugins for logging.
Currently, only has a command line client.

%prep
%setup -q

%build
export PYTHON=/usr/bin/python2
%configure --sysconfdir=%{_sysconfdir}
make

%install
%make_install
mkdir -p %{buildroot}%{_libdir}/morituri/plugins

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/rip

%files
%doc README COPYING morituri.doap NEWS RELEASE ChangeLog
%{_bindir}/rip
%{_libdir}/morituri/plugins
%{_mandir}/man1/rip.1*
%{python2_sitelib}/morituri
%{_sysconfdir}/bash_completion.d/rip

%changelog
* Thu Oct 19 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.3
- Rebuilt for Fedora
* Fri Feb 17 2017 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.2.3-3
- (0932f4c) MassBuild#1257: Increase release tag

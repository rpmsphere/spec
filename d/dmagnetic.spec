%undefine _debugsource_packages

Name:           dmagnetic
Version:        0.32
Release:        1
Summary:        A Magnetic Scrolls Interpreter
License:        BSD-2-Clause
Group:          Amusements/Games/Other
URL:            http://dettus.net/dMagnetic/
Source0:        http://dettus.net/dMagnetic/dMagnetic_%{version}.tar.bz2

%description
Olay Textadventures from Magnetic Scrolls with glorious ANSI Art.

%prep
%setup -q -n dMagnetic_%{version}

%build
make all

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man6
mkdir -p %{buildroot}%{_mandir}/man5
mkdir -p %{buildroot}%{_datadir}/dMagnetic
install -m 755 dMagnetic %{buildroot}%{_bindir}/dMagnetic
install -m 644 dMagnetic.6 %{buildroot}%{_mandir}/man6/dMagnetic.6
install -m 644 dMagneticini.5 %{buildroot}%{_mandir}/man5/dMagneticini.5
install -m 644 dMagnetic.ini %{buildroot}%{_datadir}/dMagnetic/dMagnetic.ini

%files
%{_bindir}/dMagnetic
%{_mandir}/man6/dMagnetic.6*
%{_mandir}/man5/dMagneticini.5*
%{_datadir}/dMagnetic
%doc README.txt
%license LICENSE.txt

%changelog
* Sun Oct 24 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.32
- Rebuilt for Fedora
* Mon Jul 27 2020 Michael Vetter <mvetter@suse.com>
- Update to 0.25:
  * Internal RGB channels upgraded from 3 to 10 bit
* Mon Jul 13 2020 Michael Vetter <mvetter@suse.com>
- Update to 0.24:
  No changes provided
* Mon Jan 13 2020 Enno Gotthold <egotthold@suse.com>
- Align the desc to the authors wishes
* Thu Jan  2 2020 Enno Gotthold <egotthold@suse.com>
- Update to Version 0.19
- Remove unecessary dependency
* Tue Jul 16 2019 Enno Gotthold <egotthold@suse.com>
- Extended Specfile to perform an acutal build with the files.
* Tue Jul 16 2019 Enno Gotthold <egotthold@suse.com>
- Added project sources
- Added Specfile

%undefine _debugsource_packages

Name:           dMagnetic
Version:        0.37
Release:        1
Summary:        A Magnetic Scrolls Interpreter
License:        BSD-2-Clause
Group:          Amusements/Games/Other
URL:            https://dettus.net/dMagnetic/
Source0:        https://dettus.net/%{name}/%{name}_%{version}.tar.bz2

%description
Olay Textadventures from Magnetic Scrolls with glorious ANSI Art.

%prep
%setup -q -n %{name}_%{version}

%build
make all

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man6
mkdir -p %{buildroot}%{_mandir}/man5
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -m 644 %{name}.6 %{buildroot}%{_mandir}/man6/%{name}.6
install -m 644 %{name}ini.5 %{buildroot}%{_mandir}/man5/%{name}ini.5
install -m 644 %{name}.ini %{buildroot}%{_datadir}/%{name}/%{name}.ini

%files
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_mandir}/man5/%{name}ini.5*
%{_datadir}/%{name}
%doc README.txt
%license LICENSE.txt

%changelog
* Sun May 21 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.37
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

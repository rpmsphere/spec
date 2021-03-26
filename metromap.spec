Name:           metromap
Version:        0.1.4
Release:        9
Summary:        Simple program for finding paths in subway/metro maps
License:        GPL+
URL:            http://metromap.antex.ru/
Source0:        http://metromap.antex.ru/%{name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  python2
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
Requires:       pygtk2
Requires:       hicolor-icon-theme

%description
A simple pygtk+2 application for finding paths in metro (subway)
maps. Maps for Moscow, St. Petersburg, Kiev, London, and Berlin
are included. Others can be downloaded.

%prep
%setup -q
sed -i -e '/^#!\//, 1d' modules/{FindPath.py,MapDisplay.py,Interface.py,ReadMap.py}
# Convert to utf-8
for file in metromap.desktop; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done
sed -i 's|/usr/bin/python|/usr/bin/python2|' locale/pygettext.py metromap.py tests/test.py
sed -i 's|python|python2|' locale/Makefile

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}%{_prefix} INSTALL="install -p"
desktop-file-install                                    \
    --delete-original                                   \
    --remove-category="Gtk;Office;"                     \
    --remove-category="GTK;"                            \
    --dir=%{buildroot}%{_datadir}/applications          \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}

%files -f %{name}.lang
%doc doc/AUTHORS doc/COPYING doc/NEWS doc/READ* doc/TODO
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/

%changelog
* Thu Nov 19 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.4
- Rebuild for Fedora
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-8
- Remove obsolete scriptlets
* Tue Jan 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.4-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Sat Sep 07 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.4-1
- Bogus dates fixed
- Updated spec file
- Updated to new upstream version 0.1.4
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Sat Nov 12 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.3-1
- Updated spec file to reflect upstream changes
- Updated to new upstream version 0.1.3
* Fri Aug 12 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.2-7
- Rebuild (pygtk2)
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 0.1.2-5
- recompiling .py files against Python 2.7 (rhbz#623336)
* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Sat Mar 07 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.2-3
- Added russian translation to .desktop file
* Sat Mar 07 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.2-2
- Fixed Source URL
- Fixed License
* Fri Jan 30 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.2-1
- Initial package for Fedora

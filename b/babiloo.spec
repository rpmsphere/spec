Name:           babiloo
Version:        2.0.11
Release:        9.4
Summary:        Dictionary viewer with multi-languages support
License:        GPL-3.0+
Group:          Productivity/Office/Dictionary
URL:            https://www.babiloo-project.org/
Source:         https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.gz
Source1:        %{name}
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3-PyQt4-devel
Requires:       python3-PyQt4
BuildArch:      noarch

%description
Babiloo supports dictionaries in SDictionary and StarDict format
and HTML displaying for the supported dictionaries.
Babiloo allows the download of more dictionaries from Internet.
Features:
 * Support for many languages / fonts rendering.
 * Don't convert dictionaries, use originals.
 * Phonetic sounds.
 * Advanced search.
 * Collaborative dictionaries.
GUI written for python-qt4.
See https://bazaar.launchpad.net/~babiloo-developers/babiloo/trunk/changes

%prep
%setup -q
sed -i 's|print text|print(text)|' qt/Qt2Po.py

%build
make -C qt/ clean
make -C qt/ all

%install
LANGUAGES=`find locale/ -maxdepth 1 -mindepth 1 -type d -not -name \.svn -printf "%f "`
for lang in ${LANGUAGES}; do \
localedir=%{buildroot}/%{_datadir}/locale/${lang}/LC_MESSAGES; \
install -d -m 755 ${localedir}; \
msgfmt --directory=locale ${lang}/LC_MESSAGES/%{name}.po --output-file=${localedir}/%{name}.mo; \
done
install -d -m 755 %{buildroot}/%{_datadir}/%{name}
%__cp -a core dicts images qt %{buildroot}/%{_datadir}/%{name}
install -m 755 -t %{buildroot}/%{_datadir}/%{name} *.py
%find_lang %{name} %{?no_lang_C}
install -D -m 644 %{name}.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop 
install -D -m 644 images/%{name}.xpm %{buildroot}/%{_datadir}/pixmaps/%{name}.xpm
install -D -m 0755 %{SOURCE1} %{buildroot}/%{_bindir}/%{name}
%__gzip babiloo.1
install -D -m 644 babiloo.1.gz %{buildroot}/%{_mandir}/man1/%{name}.1.gz
%__chmod a-x ChangeLog

sed -i 's|/usr/bin/python|/usr/bin/python3|' %{buildroot}%{_datadir}/babiloo/core/dictionary/*.py
sed -i 's|/usr/bin/env python|/usr/bin/python3|' %{buildroot}%{_datadir}/babiloo/*.py

%files -f %{name}.lang
%doc ChangeLog COPYING README
%{_mandir}/man1/%{name}.1.gz
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm

%changelog
* Mon Jan 13 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.11
- Rebuilt for Fedora
* Sun Oct 28 2012 fa0sck@gmail.com
- Created package for babiloo (last) version 2.0.11

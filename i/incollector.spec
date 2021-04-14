Name:           incollector
Version:        1.2
Release:        18.1
Summary:        Information collector
Group:          Applications/Productivity
License:        GPLv2
URL:            http://www.incollector.devnull.pl/
Source0:        http://www.incollector.devnull.pl/download/sources/%{name}-%{version}.tar.gz
Patch0:         %{name}-mono.patch
Patch1:		%{name}-fixlib.patch
Patch2:		%{name}-%{version}-pixmaps-install.patch
BuildArch:	noarch
BuildRequires:  gtk-sharp2-devel gettext desktop-file-utils

%description
Incollector is an application to collect various kinds of information
(like notes, conversation logs, quotes, serial numbers, source code,
web addresses, words). All the entries can be tagged, so you can find
them very easily. There are also search folders which allows you to
search for entries by specified criteria. You can also export
(and import, of course) entries to an external file.

%prep
%setup -q
%patch0
#patch1
%patch2
chmod a-x README AUTHORS

%build
%configure --prefix=/usr --libdir=/usr/lib
#./configure --prefix=/usr
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"
%find_lang %{name}
sed -i 's|/usr/share/pixmaps/%{name}.png|%{name}|' $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%doc README COPYING AUTHORS
%{_bindir}/%{name}
/usr/lib/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Jun 09 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2
- Rebuilt for Fedora
* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Mon Jan 25 2010 Thomas Janssen <thomasj@fedoraproject.org> 1.2-4
- pushed release for missing tag the pixmaps patch
* Thu Dec 03 2009 Thomas Janssen <thomasj@fedoraproject.org> 1.2-3
- Changed the license to GPLv2
- Added pixmaps-install.patch
* Thu Dec 03 2009 Thomas Janssen <thomasj@fedoraproject.org> 1.2-2
- Changed sed to patch
- Removed pushd command
* Sun Nov 15 2009 Thomas Janssen <thomasj@fedoraproject.org> 1.2-1
- Updated to new upstream version 1.2
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Tue Apr 28 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 1.0-8
- Fix FTBFS: added incollector-mono.patch.
- Added explicit R: mono-core (resolves BZ#469602).
* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Fri Feb 08 2008 Krzysztof Kurzawski <kurzawax at gmail.com> - 1.0-6
- Correct install section
* Mon Feb 04 2008 Krzysztof Kurzawski <kurzawax at gmail.com> - 1.0-5
- Correct ExclusiveArch
* Mon Feb 04 2008 Krzysztof Kurzawski <kurzawax at gmail.com> - 1.0-4
- Correct install section
- Add ExclusiveArch
* Mon Feb 04 2008 Krzysztof Kurzawski <kurzawax at gmail.com> - 1.0-3
- Correct install section
* Mon Feb 04 2008 Krzysztof Kurzawski <kurzawax at gmail.com> - 1.0-2
- Fix BRs
- Fix Source 0
* Sun Feb 03 2008 Krzysztof Kurzawski <kurzawax at gmail.com> - 1.0-1
- First release

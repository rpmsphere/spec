Name:           dynamic-wallpaper
Version:        0.3.1
Release:        5.1
Summary:        Generates svg wallpaper based on current weather, season and others
Group:          Amusements/Graphics
License:        GPLv2
URL:            https://sourceforge.net/projects/dynwallpaper
Source0:        http://downloads.sf.net/sourceforge/dynwallpaper/%{name}031.tar.bz2
# COPYING file said that licence is LGPLv2+ but some files are GPLv2.
# According to author, the more conservative licence is GPLv2
Patch0:         %{name}-copying.patch
BuildArch:      noarch
BuildRequires:  desktop-file-utils
Requires:       pymetar

%description
Dynamic wallpaper is based on weather-wallpaper and generates svg wallpaper
based on current weather, season, time of day and others. It supports themes.

%prep
%setup -q -c
%patch0 -p0
find . -name '*~' -exec rm -f {} ';'
sed -i 's|install |install -p |' Makefile

%build

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install                                    \
        --delete-original                               \
        --vendor fedora                                 \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications   \
        $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
%{__chmod} a+x $RPM_BUILD_ROOT%{_bindir}/motor.py

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING NEWS README README-themes
%{_bindir}/%{name}
%{_bindir}/motor.py
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/applications/fedora-%{name}.desktop

%changelog
* Sun Jun 23 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.1
- Rebuild for Fedora
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Tue May 29 2009 Benoît Marcelin  <sereinity@online.fr> 0.3.1-1
- Update to 0.3.1
* Tue Apr 30 2009 Benoît Marcelin  <sereinity@online.fr> 0.3-1
- Initial build
